from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.bill import Bill
from models.category import Category
from schemas.bill import BillCreate, BillPay


def create_bill(db: Session, bill: BillCreate):
    existing = db.query(Category).filter(Category.id == bill.category_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")

    new_bill = Bill(**bill.model_dump())

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill


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


def update_bill(db: Session, id, bill_data: BillCreate):
    existis = db.query(Bill).filter(Bill.id == id).first()

    if not existis:
        raise HTTPException(status_code=401, detail="Despesa não encontrada")

    for campo, valor in bill_data.model_dump(exclude_unset=True).items():
        setattr(existis, campo, valor)

    db.commit()
    db.refresh(existis)
    return existis
