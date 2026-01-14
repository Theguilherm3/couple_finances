from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.security import require_api_key
from db.session import get_db
from models.category import Category
from schemas.category import CategoryCreate, CategoryOut
from services.categories import create_category

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    # SELCT * FROM categories ORDER BY name;
    return db.query(Category).order_by(Category.name.asc()).all()


@router.post("/categories", response_model=CategoryOut, status_code=201)
def post_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, payload.name)
