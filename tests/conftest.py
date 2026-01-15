import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base
from db.session import get_db
from main import app

TEST_DATABASE_URL = "sqlite:///:memory:"

# StaticPool permite que a mesma conexão seja usada por várias threads (necessário para testes em memória)
engine = create_engine(TEST_DATABASE_URL, poolclass=StaticPool)

# Cria as tabelas
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Destroi as tabelas ao fim do teste para o próximo começar limpo
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    # A MÁGICA: Dependency Override
    # Dizemos ao FastAPI: "Quando a rota pedir 'get_db', USE 'override_get_db' em vez do original"
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db

    # Retorna o cliente simulando requisições
    with TestClient(app) as c:
        yield c
