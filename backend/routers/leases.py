from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.LeaseAgreement)
def create_lease_agreement(lease: schemas.LeaseAgreementCreate, db: Session = Depends(get_db)):
    return crud.create_lease_agreement(db=db, lease_agreement=lease)

@router.get("/", response_model=List[schemas.LeaseAgreement])
def read_lease_agreements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leases = crud.get_lease_agreements(db, skip=skip, limit=limit)
    return leases

@router.get("/{lease_id}", response_model=schemas.LeaseAgreement)
def read_lease_agreement(lease_id: UUID, db: Session = Depends(get_db)):
    db_lease = crud.get_lease_agreement(db, lease_id=lease_id)
    if db_lease is None:
        raise HTTPException(status_code=404, detail="Lease agreement not found")
    return db_lease

@router.put("/{lease_id}", response_model=schemas.LeaseAgreement)
def update_lease_agreement(lease_id: UUID, lease: schemas.LeaseAgreementUpdate, db: Session = Depends(get_db)):
    db_lease = crud.update_lease_agreement(db, lease_id=lease_id, lease_agreement=lease)
    if db_lease is None:
        raise HTTPException(status_code=404, detail="Lease agreement not found")
    return db_lease

@router.delete("/{lease_id}", response_model=schemas.LeaseAgreement)
def delete_lease_agreement(lease_id: UUID, db: Session = Depends(get_db)):
    db_lease = crud.delete_lease_agreement(db, lease_id=lease_id)
    if db_lease is None:
        raise HTTPException(status_code=404, detail="Lease agreement not found")
    return db_lease
