from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.security import require_api_key
from db.session import get_db
from models.bill import OwnerEnum
from schemas.bill import BillCreate, BillOut, BillPay, BillUpdate
from services.bills import (
    create_bill,
    delete_bill,
    get_bill_by_id,
    list_bills,
    pay_bill,
    update_bill,
)

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/bills", response_model=list[BillOut])
def get_list_bills(
    db: Session = Depends(get_db),
    owner: OwnerEnum | None = None,
    show_paid: bool = True,
):
    return list_bills(db, owner, show_paid)


@router.get("/bills/{id}", response_model=BillOut)
def get_bill_id(id: int, db: Session = Depends(get_db)):
    return get_bill_by_id(db, id)


@router.post("/bills", response_model=BillOut, status_code=201)
def post_bill(payload: BillCreate, db: Session = Depends(get_db)):
    return create_bill(db, payload)


@router.patch(
    "/bills/pay/{id}",
    response_model=BillOut,
    description="Lança o pagamento de uma despesa",
)
def patch_bill(id: int, payload: BillPay, db: Session = Depends(get_db)):
    return pay_bill(db, id, payload)


@router.patch(
    "/bills/{id}",
    response_model=BillOut,
    description="Atualiza as informações de uma despesa",
)
def bill_changes(id, payload: BillUpdate, db=Depends(get_db)):
    return update_bill(db, id, payload)


@router.delete("/bills/{id}", status_code=204)
def delete_a_bill(id, db: Session = Depends(get_db)):
    delete_bill(db, id)
