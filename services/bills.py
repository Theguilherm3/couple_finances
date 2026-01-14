from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.bill import Bill
from models.category import Category
from schemas.bill import BillCreate


def create_bill(db: Session, bill: BillCreate):
    existing = db.query(Category).filter(Category.id == Bill.category_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")

    # bill = Bill(
    #     description=bill.description,
    #     amount=bill.amount,
    #     due_date=bill.due_date,
    #     payment_date=bill.payment_date,
    #     owner=bill.owner,
    #     category_id=bill.category_id,
    # )

    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


def list_bills(db: Session):
    return db.query(Bill).order_by(Bill.description.desc()).all()
