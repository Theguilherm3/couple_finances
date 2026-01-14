from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from models.bill import Bill
from models.category import Category
from schemas.bill import BillCreate, BillOut

router = APIRouter()


@router.get("/bills", response_model=list[BillOut])
def list_bills(db: Session = Depends(get_db)):
    return db.query(Bill).order_by(Bill.description.desc()).all()


@router.post("/bills", response_model=BillCreate, status_code=201)
def create_bill(payload: BillCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.id == payload.category_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")

    bill = Bill(
        description=payload.description,
        amount=payload.amount,
        due_date=payload.due_date,
        payment_date=payload.payment_date,
        owner=payload.owner,
        category_id=payload.category_id,
    )

    db.add(bill)
    db.commit()
    db.refresh(bill)

    return bill
