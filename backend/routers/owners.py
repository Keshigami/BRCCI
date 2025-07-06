from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return crud.create_owner(db=db, owner=owner)

@router.get("/", response_model=List[schemas.Owner])
def read_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    owners = crud.get_owners(db, skip=skip, limit=limit)
    return owners

@router.get("/{owner_id}", response_model=schemas.Owner)
def read_owner(owner_id: UUID, db: Session = Depends(get_db)):
    db_owner = crud.get_owner(db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner

@router.put("/{owner_id}", response_model=schemas.Owner)
def update_owner(owner_id: UUID, owner: schemas.OwnerUpdate, db: Session = Depends(get_db)):
    db_owner = crud.update_owner(db, owner_id=owner_id, owner=owner)
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner

@router.delete("/{owner_id}", response_model=schemas.Owner)
def delete_owner(owner_id: UUID, db: Session = Depends(get_db)):
    db_owner = crud.delete_owner(db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return db_owner
