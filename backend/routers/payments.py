from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)

@router.get("/", response_model=List[schemas.Payment])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = crud.get_payments(db, skip=skip, limit=limit)
    return payments

@router.get("/{payment_id}", response_model=schemas.Payment)
def read_payment(payment_id: UUID, db: Session = Depends(get_db)):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.put("/{payment_id}", response_model=schemas.Payment)
def update_payment(payment_id: UUID, payment: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = crud.update_payment(db, payment_id=payment_id, payment=payment)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.delete("/{payment_id}", response_model=schemas.Payment)
def delete_payment(payment_id: UUID, db: Session = Depends(get_db)):
    db_payment = crud.delete_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
