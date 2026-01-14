from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category
from schemas.category import CategoryUpdate


def create_category(db: Session, name: str) -> Category:
    existing = db.query(Category).filter(Category.name == name).first()

    if existing:
        raise HTTPException(status_code=409, detail="Categoria já existe")

    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def category_delete(db: Session, category_id: int):
    existing = db.query(Category).filter(Category.id == category_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    db.delete(existing)
    db.commit()


def category_update(db: Session, category_id: int, category_name: CategoryUpdate):
    existing = db.query(Category).filter(Category.id == category_id).first()

    if not existing:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    existing.name = name = category_name.name
    db.commit()
    db.refresh(existing)
    return existing
