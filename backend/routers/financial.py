from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.FinancialTransaction)
def create_financial_transaction(transaction: schemas.FinancialTransactionCreate, db: Session = Depends(get_db)):
    return crud.create_financial_transaction(db=db, transaction=transaction)

@router.get("/", response_model=List[schemas.FinancialTransaction])
def read_financial_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crud.get_financial_transactions(db, skip=skip, limit=limit)
    return transactions

@router.get("/{transaction_id}", response_model=schemas.FinancialTransaction)
def read_financial_transaction(transaction_id: UUID, db: Session = Depends(get_db)):
    db_transaction = crud.get_financial_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Financial transaction not found")
    return db_transaction

@router.put("/{transaction_id}", response_model=schemas.FinancialTransaction)
def update_financial_transaction(transaction_id: UUID, transaction: schemas.FinancialTransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = crud.update_financial_transaction(db, transaction_id=transaction_id, transaction=transaction)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Financial transaction not found")
    return db_transaction

@router.delete("/{transaction_id}", response_model=schemas.FinancialTransaction)
def delete_financial_transaction(transaction_id: UUID, db: Session = Depends(get_db)):
    db_transaction = crud.delete_financial_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Financial transaction not found")
    return db_transaction
