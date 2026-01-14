from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.security import require_api_key
from db.session import get_db
from models.category import Category
from schemas.category import CategoryCreate, CategoryOut, CategoryUpdate
from services.categories import category_delete, category_update, create_category

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    # SELCT * FROM categories ORDER BY name;
    return db.query(Category).order_by(Category.name.asc()).all()


@router.post("/categories", response_model=CategoryOut, status_code=201)
def post_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, payload.name)


@router.delete("/categories/{id}/delete", status_code=204)
def delete_category(id: int, db: Session = Depends(get_db)):
    category_delete(db, id)


@router.patch("/categories/{id}/update", response_model=CategoryOut, status_code=201)
def set_update_category(
    id: int, payload: CategoryUpdate, db: Session = Depends(get_db)
):
    return category_update(db, id, payload)
