# 💰 Couple Finances API

Uma API RESTful profissional desenvolvida para gerenciamento financeiro de casais, permitindo o controle de contas compartilhadas, categorias de gastos e status de pagamentos.

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework:** FastAPI
- **Banco de Dados:** SQLite (com SQLAlchemy ORM)
- **Validação:** Pydantic V2
- **Gerenciador de Pacotes:** uv
- **Testes:** Pytest
- **Containerização:** Docker

## ✨ Funcionalidades

- **CRUD de Contas:** Criar, listar, editar e remover contas a pagar.
- **Categorias Dinâmicas:** Gerenciamento de categorias de despesas.
- **Filtros e Paginação:** Listagem otimizada com `skip` e `limit`, além de filtros por dono (ELE/ELA/CASAL).
- **Segurança:** Proteção de rotas via API Key (`x-api-key`).
- **Sanitização de Dados:** Formatação automática de textos (ex: títulos capitalizados).

---

## 🛠️ Como Rodar Localmente (Desenvolvimento)

### Pré-requisitos

Tenha o [uv](https://github.com/astral-sh/uv) instalado.

### 1. Instalação

Clone o repositório e instale as dependências:

```bash
git clone [https://github.com/SEU_USUARIO/couple_finances.git](https://github.com/SEU_USUARIO/couple_finances.git)
cd couple_finances
uv sync

2. Configuração (.env)

Altere o arquivo .env na raiz do projeto para configurar sua chave de segurança:
API_TOKEN=sua_senha_secreta_aqui

3. Rodando a API

Inicie o servidor de desenvolvimento:
uv run uvicorn main:app --reload

4. Rodando os Testes

Para executar a bateria de testes automatizados:
uv run pytest




🐳 Como Rodar com Docker

Para rodar a aplicação em um container isolado (produção):
1. Construir a Imagem
docker build -t couple-finances-img .


2. Rodar o Container
docker run -d -p 8000:8000 --name app-financeiro couple-finances-img
A API estará disponível em http://localhost:8000.



📂 Estrutura do Projeto
couple_finances/
├── core/           # Configurações e Segurança
├── db/             # Conexão com Banco e Sessão
├── models/         # Tabelas do Banco de Dados (SQLAlchemy)
├── routes/         # Rotas da API (Endpoints)
├── schemas/        # Validação de Dados (Pydantic)
├── services/       # Lógica de Negócio (CRUD)
├── tests/          # Testes Automatizados
├── main.py         # Entrada da Aplicação
├── Dockerfile      # Configuração da Imagem Docker
└── pyproject.toml  # Dependências do Projeto
```
