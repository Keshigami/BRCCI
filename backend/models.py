from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from .database import Base

class Property(Base):
    __tablename__ = "properties"

    property_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    province = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    property_type = Column(Enum('residential', 'commercial', 'condominium', name='property_type_enum'), nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("owners.owner_id"), nullable=False)
    acquisition_date = Column(Date, nullable=False)
    market_value_php = Column(DECIMAL(15, 2), nullable=False)

    owner = relationship("Owner", back_populates="properties")
    units = relationship("Unit", back_populates="property")

class Unit(Base):
    __tablename__ = "units"

    unit_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.property_id"), nullable=False)
    unit_number = Column(String, nullable=False)
    floor_area_sqm = Column(DECIMAL(10, 2), nullable=False)
    unit_type = Column(Enum('showroom', 'warehousing', 'office', 'retail', name='unit_type_enum'), nullable=False)
    number_of_bedrooms = Column(Integer, nullable=True)
    number_of_bathrooms = Column(Integer, nullable=True)
    current_rental_rate_php = Column(DECIMAL(15, 2), nullable=False)
    status = Column(Enum('occupied', 'vacant', 'under_maintenance', name='unit_status_enum'), nullable=False)

    property = relationship("Property", back_populates="units")
    lease_agreements = relationship("LeaseAgreement", back_populates="unit")
    maintenance_requests = relationship("MaintenanceRequest", back_populates="unit")

class Tenant(Base):
    __tablename__ = "tenants"

    tenant_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    id_type = Column(String, nullable=False)
    id_number = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    nationality = Column(String, nullable=False)

    lease_agreements = relationship("LeaseAgreement", back_populates="tenant")
    maintenance_requests = relationship("MaintenanceRequest", back_populates="tenant")

class LeaseAgreement(Base):
    __tablename__ = "lease_agreements"

    lease_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.unit_id"), nullable=False)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.tenant_id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    monthly_rent_php = Column(DECIMAL(15, 2), nullable=False)
    security_deposit_php = Column(DECIMAL(15, 2), nullable=False)
    advance_payment_php = Column(DECIMAL(15, 2), nullable=False)
    payment_due_day = Column(Integer, nullable=False)
    lease_status = Column(Enum('active', 'expired', 'terminated', name='lease_status_enum'), nullable=False)
    last_rent_increase_date = Column(Date, nullable=True)
    next_rent_increase_date = Column(Date, nullable=True)
    rent_increase_percentage = Column(DECIMAL(5, 2), nullable=True)

    unit = relationship("Unit", back_populates="lease_agreements")
    tenant = relationship("Tenant", back_populates="lease_agreements")
    payments = relationship("Payment", back_populates="lease_agreement")

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lease_id = Column(UUID(as_uuid=True), ForeignKey("lease_agreements.lease_id"), nullable=False)
    amount_php = Column(DECIMAL(15, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    payment_type = Column(Enum('bank_transfer', 'online_gateway', 'cash', 'check', name='payment_type_enum'), nullable=False)
    status = Column(Enum('paid', 'pending', 'failed', 'overdue', name='payment_status_enum'), nullable=False)
    description = Column(String, nullable=True)
    receipt_number = Column(String, nullable=True)

    lease_agreement = relationship("LeaseAgreement", back_populates="payments")
    financial_transactions = relationship("FinancialTransaction", back_populates="payment")

class MaintenanceRequest(Base):
    __tablename__ = "maintenance_requests"

    request_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.unit_id"), nullable=False)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.tenant_id"), nullable=False)
    description = Column(String, nullable=False)
    category = Column(Enum('plumbing', 'electrical', 'structural', 'appliance', 'other', name='maintenance_category_enum'), nullable=False)
    date_submitted = Column(DateTime, nullable=False)
    status = Column(Enum('new', 'in_progress', 'completed', 'cancelled', name='maintenance_status_enum'), nullable=False)
    assigned_to = Column(String, nullable=True)
    completion_date = Column(DateTime, nullable=True)
    cost_php = Column(DECIMAL(15, 2), nullable=True)
    notes = Column(String, nullable=True)

    unit = relationship("Unit", back_populates="maintenance_requests")
    tenant = relationship("Tenant", back_populates="maintenance_requests")
    financial_transactions = relationship("FinancialTransaction", back_populates="maintenance_request")

class FinancialTransaction(Base):
    __tablename__ = "financial_transactions"

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.property_id"), nullable=True)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.unit_id"), nullable=True)
    transaction_type = Column(Enum('income', 'expense', name='transaction_type_enum'), nullable=False)
    amount_php = Column(DECIMAL(15, 2), nullable=False)
    transaction_date = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    related_payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.payment_id"), nullable=True)
    related_maintenance_id = Column(UUID(as_uuid=True), ForeignKey("maintenance_requests.request_id"), nullable=True)

    payment = relationship("Payment", back_populates="financial_transactions")
    maintenance_request = relationship("MaintenanceRequest", back_populates="financial_transactions")

class Owner(Base):
    __tablename__ = "owners"

    owner_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    bank_account_details = Column(String, nullable=True)

    properties = relationship("Property", back_populates="owner")

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum('admin', 'property_manager', 'tenant', 'owner', name='user_role_enum'), nullable=False)
    associated_entity_id = Column(UUID(as_uuid=True), nullable=True) # Can link to tenant_id, owner_id, etc.
