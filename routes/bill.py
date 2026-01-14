from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.security import require_api_key
from db.session import get_db
from schemas.bill import BillCreate, BillOut
from services.bills import create_bill, list_bills

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.get("/bills", response_model=list[BillOut])
def get_list_bills(db: Session = Depends(get_db)):
    return list_bills(db)


@router.post("/bills", response_model=BillCreate, status_code=201)
def post_bill(payload: BillCreate, db: Session = Depends(get_db)):
    return create_bill(db, payload)
