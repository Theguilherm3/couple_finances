run uvicorn:
uv run uvicorn main:app --reload

alembic:
uv add alembic
uv run alembic init alembic

alembic.ini:
sqlalchemy.url = sqlite:///./finance.db

alembic env.py
from db.base import Base
target_metadata = Base.metadata

def run_migrations_offline() -> None:
import models.category # noqa: F401
import models.bill # noqa: F401

def run_migrations_online() -> None:
import models.category # noqa: F401
import models.bill # noqa: F401

uv run alembic revision --autogenerate -m "mensagem curta aqui"

uv run alembic upgrade head

github passo a passo usando main:
git status (Verificar as mudanças)
git add . (adicionar todas as mudanças, dos arquivos listados)
git commit -m "" (comitar mudanças da branch)
git push (enviar as mudanças pro github)
