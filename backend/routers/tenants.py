from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Tenant)
def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    return crud.create_tenant(db=db, tenant=tenant)

@router.get("/", response_model=List[schemas.Tenant])
def read_tenants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tenants = crud.get_tenants(db, skip=skip, limit=limit)
    return tenants

@router.get("/{tenant_id}", response_model=schemas.Tenant)
def read_tenant(tenant_id: UUID, db: Session = Depends(get_db)):
    db_tenant = crud.get_tenant(db, tenant_id=tenant_id)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant

@router.put("/{tenant_id}", response_model=schemas.Tenant)
def update_tenant(tenant_id: UUID, tenant: schemas.TenantUpdate, db: Session = Depends(get_db)):
    db_tenant = crud.update_tenant(db, tenant_id=tenant_id, tenant=tenant)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant

@router.delete("/{tenant_id}", response_model=schemas.Tenant)
def delete_tenant(tenant_id: UUID, db: Session = Depends(get_db)):
    db_tenant = crud.delete_tenant(db, tenant_id=tenant_id)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant
