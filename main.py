# to run use: uv run uvicorn main:app
from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.base import Base
from db.session import engine
from routes.categories import router as categories_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    import models.bill  # noqa: F401
    import models.category  # noqa: F401

    # cria as tabelas, caso nao existam
    Base.metadata.create_all(bind=engine)

    # aplicacao roda no yield
    yield


app = FastAPI(title="APLI Dados Financeiros - Casal", lifespan=lifespan)


@app.get("/health")
def health():
    return {"ok": True, "status": "running"}


app.include_router(categories_router, tags=["categories"])
