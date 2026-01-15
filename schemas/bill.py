from datetime import date

from pydantic import BaseModel, Field, field_validator

from models.bill import OwnerEnum
from schemas.category import CategoryOut


class BillCreate(BaseModel):
    description: str = Field(min_length=2, max_length=60, examples=["Internet"])
    amount: float = Field(gt=0, examples=[129.97])
    due_date: date
    payment_date: date | None = None
    owner: OwnerEnum
    category_id: int

    @field_validator("description")
    @classmethod
    def format_description(cls, v: str) -> str:
        return v.title()


class BillOut(BaseModel):
    id: int
    description: str
    amount: float
    due_date: date
    payment_date: date | None = None
    owner: OwnerEnum
    category: CategoryOut | None = None
    paid: bool

    class Config:
        from_attributes = True


class BillPay(BaseModel):
    payment_date: date = Field(default_factory=date.today)


class BillUpdate(BaseModel):
    description: str | None = None
    amount: float | None = None
    due_date: date | None = None
    payment_date: date | None = None
    owner: OwnerEnum | None = None
    category_id: int | None = None
