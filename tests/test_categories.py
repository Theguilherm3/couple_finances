from fastapi.testclient import TestClient


def test_criar_categoria_com_sucesso(client: TestClient):
    payload = {"name": "Investimentos"}

    response = client.post("/categories", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Investimentos"
    assert "id" in data


def test_criar_categoria_duplicada_deve_falhar(client):
    client.post("/categories", json={"name": "Lazer"})

    response = client.post("/categories", json={"name": "Lazer"})

    assert response.status_code == 409
    assert response.json()["detail"] == "Categoria já existe"


def test_get_bills(client: TestClient):
    response = client.get("/bills")

    assert response.status_code == 200
