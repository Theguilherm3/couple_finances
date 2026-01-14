from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.bill import Bill
from models.category import Category
from schemas.bill import BillCreate, BillPay


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


def pay_bill(db: Session, id: int, billpayment: BillPay):
    bill = db.query(Bill).filter(Bill.id == id).first()

    if not bill:
        raise HTTPException(status_code=401, detail="Despesa não encontrada")

    elif bill.payment_date:
        raise HTTPException(status_code=409, detail="Despesa já está como paga!")

    bill.payment_date = billpayment.payment_date
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


def get_bill_by_id(db: Session, bill_id):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()

    if not bill:
        raise HTTPException(status_code=401, detail="Despesa não encontrada")

    return bill


def delete_bill(db: Session, bill_id):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()

    if not bill:
        raise HTTPException(status_code=401, detail="Despesa não encontrada")

    db.delete(bill)
    db.commit()
