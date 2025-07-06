from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime
from uuid import UUID

# Base Schemas (for common fields)
class PropertyBase(BaseModel):
    address: str
    city: str
    province: str
    zip_code: str
    property_type: str  # Consider Enum for validation
    owner_id: UUID
    acquisition_date: date
    market_value_php: float

class UnitBase(BaseModel):
    property_id: UUID
    unit_number: str
    floor_area_sqm: float
    unit_type: str  # Consider Enum for validation
    number_of_bedrooms: Optional[int] = None
    number_of_bathrooms: Optional[int] = None
    current_rental_rate_php: float
    status: str  # Consider Enum for validation

class TenantBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    id_type: str
    id_number: str
    date_of_birth: date
    nationality: str

class LeaseAgreementBase(BaseModel):
    unit_id: UUID
    tenant_id: UUID
    start_date: date
    end_date: date
    monthly_rent_php: float
    security_deposit_php: float
    advance_payment_php: float
    payment_due_day: int
    lease_status: str  # Consider Enum for validation
    last_rent_increase_date: Optional[date] = None
    next_rent_increase_date: Optional[date] = None
    rent_increase_percentage: Optional[float] = None

class PaymentBase(BaseModel):
    lease_id: UUID
    amount_php: float
    payment_date: datetime
    payment_type: str  # Consider Enum for validation
    status: str  # Consider Enum for validation
    description: Optional[str] = None
    receipt_number: Optional[str] = None

class MaintenanceRequestBase(BaseModel):
    unit_id: UUID
    tenant_id: UUID
    description: str
    category: str  # Consider Enum for validation
    date_submitted: datetime
    status: str  # Consider Enum for validation
    assigned_to: Optional[str] = None
    completion_date: Optional[datetime] = None
    cost_php: Optional[float] = None
    notes: Optional[str] = None

class FinancialTransactionBase(BaseModel):
    property_id: Optional[UUID] = None
    unit_id: Optional[UUID] = None
    transaction_type: str  # Consider Enum for validation
    amount_php: float
    transaction_date: date
    category: str
    description: Optional[str] = None
    related_payment_id: Optional[UUID] = None
    related_maintenance_id: Optional[UUID] = None

class OwnerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    bank_account_details: Optional[str] = None

class UserBase(BaseModel):
    username: str
    password_hash: str
    role: str  # Consider Enum for validation
    associated_entity_id: Optional[UUID] = None

# Create Schemas (for creating new entries)
class PropertyCreate(PropertyBase):
    pass

class UnitCreate(UnitBase):
    pass

class TenantCreate(TenantBase):
    pass

class LeaseAgreementCreate(LeaseAgreementBase):
    pass

class PaymentCreate(PaymentBase):
    pass

class MaintenanceRequestCreate(MaintenanceRequestBase):
    pass

class FinancialTransactionCreate(FinancialTransactionBase):
    pass

class OwnerCreate(OwnerBase):
    pass

class UserCreate(UserBase):
    pass

# Update Schemas (for updating existing entries)
class PropertyUpdate(PropertyBase):
    address: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    zip_code: Optional[str] = None
    property_type: Optional[str] = None
    owner_id: Optional[UUID] = None
    acquisition_date: Optional[date] = None
    market_value_php: Optional[float] = None

class UnitUpdate(UnitBase):
    property_id: Optional[UUID] = None
    unit_number: Optional[str] = None
    floor_area_sqm: Optional[float] = None
    unit_type: Optional[str] = None
    number_of_bedrooms: Optional[int] = None
    number_of_bathrooms: Optional[int] = None
    current_rental_rate_php: Optional[float] = None
    status: Optional[str] = None

class TenantUpdate(TenantBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    id_type: Optional[str] = None
    id_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    nationality: Optional[str] = None

class LeaseAgreementUpdate(LeaseAgreementBase):
    unit_id: Optional[UUID] = None
    tenant_id: Optional[UUID] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    monthly_rent_php: Optional[float] = None
    security_deposit_php: Optional[float] = None
    advance_payment_php: Optional[float] = None
    payment_due_day: Optional[int] = None
    lease_status: Optional[str] = None
    last_rent_increase_date: Optional[date] = None
    next_rent_increase_date: Optional[date] = None
    rent_increase_percentage: Optional[float] = None

class PaymentUpdate(PaymentBase):
    lease_id: Optional[UUID] = None
    amount_php: Optional[float] = None
    payment_date: Optional[datetime] = None
    payment_type: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    receipt_number: Optional[str] = None

class MaintenanceRequestUpdate(MaintenanceRequestBase):
    unit_id: Optional[UUID] = None
    tenant_id: Optional[UUID] = None
    description: Optional[str] = None
    category: Optional[str] = None
    date_submitted: Optional[datetime] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    completion_date: Optional[datetime] = None
    cost_php: Optional[float] = None
    notes: Optional[str] = None

class FinancialTransactionUpdate(FinancialTransactionBase):
    property_id: Optional[UUID] = None
    unit_id: Optional[UUID] = None
    transaction_type: Optional[str] = None
    amount_php: Optional[float] = None
    transaction_date: Optional[date] = None
    category: Optional[str] = None
    description: Optional[str] = None
    related_payment_id: Optional[UUID] = None
    related_maintenance_id: Optional[UUID] = None

class OwnerUpdate(OwnerBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    bank_account_details: Optional[str] = None

class UserUpdate(UserBase):
    username: Optional[str] = None
    password_hash: Optional[str] = None
    role: Optional[str] = None
    associated_entity_id: Optional[UUID] = None

# Response Schemas (for returning data)
class Property(PropertyBase):
    property_id: UUID

    class Config:
        from_attributes = True

class Unit(UnitBase):
    unit_id: UUID

    class Config:
        from_attributes = True

class Tenant(TenantBase):
    tenant_id: UUID

    class Config:
        from_attributes = True

class LeaseAgreement(LeaseAgreementBase):
    lease_id: UUID

    class Config:
        from_attributes = True

class Payment(PaymentBase):
    payment_id: UUID

    class Config:
        from_attributes = True

class MaintenanceRequest(MaintenanceRequestBase):
    request_id: UUID

    class Config:
        from_attributes = True

class FinancialTransaction(FinancialTransactionBase):
    transaction_id: UUID

    class Config:
        from_attributes = True

class Owner(OwnerBase):
    owner_id: UUID

    class Config:
        from_attributes = True

class User(UserBase):
    user_id: UUID

    class Config:
        from_attributes = True
