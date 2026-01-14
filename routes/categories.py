from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from models.category import Category
from schemas.category import CategoryCreate, CategoryOut

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    # SELCT * FROM categories ORDER BY name;
    return db.query(Category).order_by(Category.name.asc()).all()


@router.post("/categories", response_model=CategoryOut, status_code=201)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Categoria já existe")

    # Cria o objeto
    category = Category(name=payload.name)

    # Salva o objeto e comita
    db.add(category)
    db.commit()
    db.refresh(category)

    return category
