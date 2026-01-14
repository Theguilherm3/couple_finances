import enum
from datetime import date

from sqlalchemy import Date, Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class OwnerEnum(str, enum.Enum):
    DELE = "DELE"
    DELA = "DELA"
    CASAL = "CASAL"


class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String(160), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    payment_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    owner: Mapped[OwnerEnum] = mapped_column(Enum(OwnerEnum), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )

    category = relationship("Category")

    @property
    def paid(self) -> bool:
        return self.payment_date is not None
