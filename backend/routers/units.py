from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Unit)
def create_unit(unit: schemas.UnitCreate, db: Session = Depends(get_db)):
    return crud.create_unit(db=db, unit=unit)

@router.get("/", response_model=List[schemas.Unit])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = crud.get_units(db, skip=skip, limit=limit)
    return units

@router.get("/{unit_id}", response_model=schemas.Unit)
def read_unit(unit_id: UUID, db: Session = Depends(get_db)):
    db_unit = crud.get_unit(db, unit_id=unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit

@router.put("/{unit_id}", response_model=schemas.Unit)
def update_unit(unit_id: UUID, unit: schemas.UnitUpdate, db: Session = Depends(get_db)):
    db_unit = crud.update_unit(db, unit_id=unit_id, unit=unit)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit

@router.delete("/{unit_id}", response_model=schemas.Unit)
def delete_unit(unit_id: UUID, db: Session = Depends(get_db)):
    db_unit = crud.delete_unit(db, unit_id=unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit
