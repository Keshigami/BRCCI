from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Property)
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db)):
    return crud.create_property(db=db, property=property)

@router.get("/", response_model=List[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    properties = crud.get_properties(db, skip=skip, limit=limit)
    return properties

@router.get("/{property_id}", response_model=schemas.Property)
def read_property(property_id: UUID, db: Session = Depends(get_db)):
    db_property = crud.get_property(db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@router.put("/{property_id}", response_model=schemas.Property)
def update_property(property_id: UUID, property: schemas.PropertyUpdate, db: Session = Depends(get_db)):
    db_property = crud.update_property(db, property_id=property_id, property=property)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@router.delete("/{property_id}", response_model=schemas.Property)
def delete_property(property_id: UUID, db: Session = Depends(get_db)):
    db_property = crud.delete_property(db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property
