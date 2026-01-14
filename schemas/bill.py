from datetime import date

from pydantic import BaseModel, Field

from models.bill import OwnerEnum


class BillCreate(BaseModel):
    description: str = Field(min_length=2, max_length=60, examples=["Internet"])
    amount: float = Field(gt=0, examples=[129.97])
    due_date: date
    payment_date: date | None = None
    owner: OwnerEnum
    category_id: int


class BillOut(BaseModel):
    id: int
    description: str
    amount: float
    due_date: date
    payment_date: date | None = None
    owner: OwnerEnum
    category_id: int
    paid: bool


class BillPay(BaseModel):
    payment_date: date = Field(default_factory=date.today)
