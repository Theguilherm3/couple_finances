from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base é a classe "mãe" de todos os Models.

    Quando você cria:
        class Category(Base):
            ...

    o SQLAlchemy entende que Category deve virar uma tabela no banco.
    """

    pass
