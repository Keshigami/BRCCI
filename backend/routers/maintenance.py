from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.MaintenanceRequest)
def create_maintenance_request(request: schemas.MaintenanceRequestCreate, db: Session = Depends(get_db)):
    return crud.create_maintenance_request(db=db, request=request)

@router.get("/", response_model=List[schemas.MaintenanceRequest])
def read_maintenance_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    requests = crud.get_maintenance_requests(db, skip=skip, limit=limit)
    return requests

@router.get("/{request_id}", response_model=schemas.MaintenanceRequest)
def read_maintenance_request(request_id: UUID, db: Session = Depends(get_db)):
    db_request = crud.get_maintenance_request(db, request_id=request_id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    return db_request

@router.put("/{request_id}", response_model=schemas.MaintenanceRequest)
def update_maintenance_request(request_id: UUID, request: schemas.MaintenanceRequestUpdate, db: Session = Depends(get_db)):
    db_request = crud.update_maintenance_request(db, request_id=request_id, request=request)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    return db_request

@router.delete("/{request_id}", response_model=schemas.MaintenanceRequest)
def delete_maintenance_request(request_id: UUID, db: Session = Depends(get_db)):
    db_request = crud.delete_maintenance_request(db, request_id=request_id)
    if db_request is None:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    return db_request
