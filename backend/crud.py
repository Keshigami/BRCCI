from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID

def get_property(db: Session, property_id: UUID):
    return db.query(models.Property).filter(models.Property.property_id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()

def create_property(db: Session, property: schemas.PropertyCreate):
    db_property = models.Property(**property.model_dump())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def update_property(db: Session, property_id: UUID, property: schemas.PropertyUpdate):
    db_property = db.query(models.Property).filter(models.Property.property_id == property_id).first()
    if db_property:
        for key, value in property.model_dump(exclude_unset=True).items():
            setattr(db_property, key, value)
        db.commit()
        db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: UUID):
    db_property = db.query(models.Property).filter(models.Property.property_id == property_id).first()
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property

# Unit CRUD operations
def get_unit(db: Session, unit_id: UUID):
    return db.query(models.Unit).filter(models.Unit.unit_id == unit_id).first()

def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unit).offset(skip).limit(limit).all()

def create_unit(db: Session, unit: schemas.UnitCreate):
    db_unit = models.Unit(**unit.model_dump())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

def update_unit(db: Session, unit_id: UUID, unit: schemas.UnitUpdate):
    db_unit = db.query(models.Unit).filter(models.Unit.unit_id == unit_id).first()
    if db_unit:
        for key, value in unit.model_dump(exclude_unset=True).items():
            setattr(db_unit, key, value)
        db.commit()
        db.refresh(db_unit)
    return db_unit

def delete_unit(db: Session, unit_id: UUID):
    db_unit = db.query(models.Unit).filter(models.Unit.unit_id == unit_id).first()
    if db_unit:
        db.delete(db_unit)
        db.commit()
    return db_unit

# Tenant CRUD operations
def get_tenant(db: Session, tenant_id: UUID):
    return db.query(models.Tenant).filter(models.Tenant.tenant_id == tenant_id).first()

def get_tenants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tenant).offset(skip).limit(limit).all()

def create_tenant(db: Session, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(**tenant.model_dump())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def update_tenant(db: Session, tenant_id: UUID, tenant: schemas.TenantUpdate):
    db_tenant = db.query(models.Tenant).filter(models.Tenant.tenant_id == tenant_id).first()
    if db_tenant:
        for key, value in tenant.model_dump(exclude_unset=True).items():
            setattr(db_tenant, key, value)
        db.commit()
        db.refresh(db_tenant)
    return db_tenant

def delete_tenant(db: Session, tenant_id: UUID):
    db_tenant = db.query(models.Tenant).filter(models.Tenant.tenant_id == tenant_id).first()
    if db_tenant:
        db.delete(db_tenant)
        db.commit()
    return db_tenant

# LeaseAgreement CRUD operations
def get_lease_agreement(db: Session, lease_id: UUID):
    return db.query(models.LeaseAgreement).filter(models.LeaseAgreement.lease_id == lease_id).first()

def get_lease_agreements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LeaseAgreement).offset(skip).limit(limit).all()

def create_lease_agreement(db: Session, lease_agreement: schemas.LeaseAgreementCreate):
    db_lease_agreement = models.LeaseAgreement(**lease_agreement.model_dump())
    db.add(db_lease_agreement)
    db.commit()
    db.refresh(db_lease_agreement)
    return db_lease_agreement

def update_lease_agreement(db: Session, lease_id: UUID, lease_agreement: schemas.LeaseAgreementUpdate):
    db_lease_agreement = db.query(models.LeaseAgreement).filter(models.LeaseAgreement.lease_id == lease_id).first()
    if db_lease_agreement:
        for key, value in lease_agreement.model_dump(exclude_unset=True).items():
            setattr(db_lease_agreement, key, value)
        db.commit()
        db.refresh(db_lease_agreement)
    return db_lease_agreement

def delete_lease_agreement(db: Session, lease_id: UUID):
    db_lease_agreement = db.query(models.LeaseAgreement).filter(models.LeaseAgreement.lease_id == lease_id).first()
    if db_lease_agreement:
        db.delete(db_lease_agreement)
        db.commit()
    return db_lease_agreement

# Payment CRUD operations
def get_payment(db: Session, payment_id: UUID):
    return db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()

def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def update_payment(db: Session, payment_id: UUID, payment: schemas.PaymentUpdate):
    db_payment = db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()
    if db_payment:
        for key, value in payment.model_dump(exclude_unset=True).items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: UUID):
    db_payment = db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment

# MaintenanceRequest CRUD operations
def get_maintenance_request(db: Session, request_id: UUID):
    return db.query(models.MaintenanceRequest).filter(models.MaintenanceRequest.request_id == request_id).first()

def get_maintenance_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MaintenanceRequest).offset(skip).limit(limit).all()

def create_maintenance_request(db: Session, request: schemas.MaintenanceRequestCreate):
    db_request = models.MaintenanceRequest(**request.model_dump())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def update_maintenance_request(db: Session, request_id: UUID, request: schemas.MaintenanceRequestUpdate):
    db_request = db.query(models.MaintenanceRequest).filter(models.MaintenanceRequest.request_id == request_id).first()
    if db_request:
        for key, value in request.model_dump(exclude_unset=True).items():
            setattr(db_request, key, value)
        db.commit()
        db.refresh(db_request)
    return db_request

def delete_maintenance_request(db: Session, request_id: UUID):
    db_request = db.query(models.MaintenanceRequest).filter(models.MaintenanceRequest.request_id == request_id).first()
    if db_request:
        db.delete(db_request)
        db.commit()
    return db_request

# FinancialTransaction CRUD operations
def get_financial_transaction(db: Session, transaction_id: UUID):
    return db.query(models.FinancialTransaction).filter(models.FinancialTransaction.transaction_id == transaction_id).first()

def get_financial_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FinancialTransaction).offset(skip).limit(limit).all()

def create_financial_transaction(db: Session, transaction: schemas.FinancialTransactionCreate):
    db_transaction = models.FinancialTransaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_financial_transaction(db: Session, transaction_id: UUID, transaction: schemas.FinancialTransactionUpdate):
    db_transaction = db.query(models.FinancialTransaction).filter(models.FinancialTransaction.transaction_id == transaction_id).first()
    if db_transaction:
        for key, value in transaction.model_dump(exclude_unset=True).items():
            setattr(db_transaction, key, value)
        db.commit()
        db.refresh(db_transaction)
    return db_transaction

def delete_financial_transaction(db: Session, transaction_id: UUID):
    db_transaction = db.query(models.FinancialTransaction).filter(models.FinancialTransaction.transaction_id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction

# Owner CRUD operations
def get_owner(db: Session, owner_id: UUID):
    return db.query(models.Owner).filter(models.Owner.owner_id == owner_id).first()

def get_owners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Owner).offset(skip).limit(limit).all()

def create_owner(db: Session, owner: schemas.OwnerCreate):
    db_owner = models.Owner(**owner.model_dump())
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def update_owner(db: Session, owner_id: UUID, owner: schemas.OwnerUpdate):
    db_owner = db.query(models.Owner).filter(models.Owner.owner_id == owner_id).first()
    if db_owner:
        for key, value in owner.model_dump(exclude_unset=True).items():
            setattr(db_owner, key, value)
        db.commit()
        db.refresh(db_owner)
    return db_owner

def delete_owner(db: Session, owner_id: UUID):
    db_owner = db.query(models.Owner).filter(models.Owner.owner_id == owner_id).first()
    if db_owner:
        db.delete(db_owner)
        db.commit()
    return db_owner

# User CRUD operations
def get_user(db: Session, user_id: UUID):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: UUID, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: UUID):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
