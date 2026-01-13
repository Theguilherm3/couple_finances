# to run use: uv run uvicorn main:app
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from db.base import Base
from db.session import engine, get_db
from models.category import Category

app = FastAPI(title="API Dados Financeiros - Casal")


@app.on_event("startup")
def on_startup():
    import models.bill  # noqa: F401
    import models.category  # noqa: F401

    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"ok": True, "status": "running"}


@app.get("/categories")
def list_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories
