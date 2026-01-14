from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category


def create_category(db: Session, name: str) -> Category:
    existing = db.query(Category).filter(Category.name == name).first()

    if existing:
        raise HTTPException(status_code=409, detail="Categoria já existe")

    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
