# O pytest injeta o 'client' automaticamente pq definimos no conftest.py
def test_criar_categoria_com_sucesso(client):
    # Arrange (Preparar os dados)
    payload = {"name": "Investimentos"}

    # Act (Fazer a requisição POST)
    # Note que não precisamos da URL completa (http://localhost...), só o caminho
    response = client.post("/categories", json=payload)

    # Assert (Verificar se deu certo)
    assert response.status_code == 201  # Esperamos Created
    data = response.json()
    assert data["name"] == "Investimentos"
    assert "id" in data  # Verifica se o banco gerou um ID


def test_criar_categoria_duplicada_deve_falhar(client):
    # 1. Cria a primeira vez
    client.post("/categories", json={"name": "Lazer"})

    # 2. Tenta criar a segunda vez igual
    response = client.post("/categories", json={"name": "Lazer"})

    # 3. Assert - Deve dar Conflito (409)
    assert response.status_code == 409
    assert response.json()["detail"] == "Categoria já existe"
