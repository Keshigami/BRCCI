## Data Model with PHP Currency

All monetary values in the system will be stored and displayed in Philippine Pesos (PHP).

### 1. Property Table
- `property_id` (PK, UUID)
- `address` (TEXT)
- `city` (TEXT)
- `province` (TEXT)
- `zip_code` (TEXT)
- `property_type` (ENUM: 'residential', 'commercial', 'condominium')
- `owner_id` (FK, UUID)
- `acquisition_date` (DATE)
- `market_value_php` (DECIMAL(15, 2)) - *PHP*

### 2. Unit Table
- `unit_id` (PK, UUID)
- `property_id` (FK, UUID)
- `unit_number` (TEXT)
- `floor_area_sqm` (DECIMAL(10, 2))
- `unit_type` (ENUM: 'showroom', 'warehousing', 'office', 'retail')
- `number_of_bedrooms` (INTEGER, NULLABLE)
- `number_of_bathrooms` (INTEGER, NULLABLE)
- `current_rental_rate_php` (DECIMAL(15, 2)) - *PHP*
- `status` (ENUM: 'occupied', 'vacant', 'under_maintenance')

### 3. Tenant Table
- `tenant_id` (PK, UUID)
- `first_name` (TEXT)
- `last_name` (TEXT)
- `email` (TEXT)
- `phone_number` (TEXT)
- `id_type` (TEXT: e.g., 'Passport', 'Driver's License')
- `id_number` (TEXT)
- `date_of_birth` (DATE)
- `nationality` (TEXT)

### 4. Lease Agreement Table
- `lease_id` (PK, UUID)
- `unit_id` (FK, UUID)
- `tenant_id` (FK, UUID)
- `start_date` (DATE)
- `end_date` (DATE)
- `monthly_rent_php` (DECIMAL(15, 2)) - *PHP*
- `security_deposit_php` (DECIMAL(15, 2)) - *PHP*
- `advance_payment_php` (DECIMAL(15, 2)) - *PHP*
- `payment_due_day` (INTEGER: 1-31)
- `lease_status` (ENUM: 'active', 'expired', 'terminated')
- `last_rent_increase_date` (DATE)
- `next_rent_increase_date` (DATE)
- `rent_increase_percentage` (DECIMAL(5, 2))

### 5. Payment Table
- `payment_id` (PK, UUID)
- `lease_id` (FK, UUID)
- `amount_php` (DECIMAL(15, 2)) - *PHP*
- `payment_date` (DATETIME)
- `payment_type` (ENUM: 'bank_transfer', 'online_gateway', 'cash', 'check')
- `status` (ENUM: 'paid', 'pending', 'failed', 'overdue')
- `description` (TEXT: e.g., 'July 2025 Rent', 'Late Fee')
- `receipt_number` (TEXT)

### 6. Maintenance Request Table
- `request_id` (PK, UUID)
- `unit_id` (FK, UUID)
- `tenant_id` (FK, UUID)
- `description` (TEXT)
- `category` (ENUM: 'plumbing', 'electrical', 'structural', 'appliance', 'other')
- `date_submitted` (DATETIME)
- `status` (ENUM: 'new', 'in_progress', 'completed', 'cancelled')
- `assigned_to` (TEXT: e.g., 'John Doe - Plumber')
- `completion_date` (DATETIME)
- `cost_php` (DECIMAL(15, 2)) - *PHP*
- `notes` (TEXT)

### 7. Financial Transaction Table
- `transaction_id` (PK, UUID)
- `property_id` (FK, UUID, NULLABLE)
- `unit_id` (FK, UUID, NULLABLE)
- `transaction_type` (ENUM: 'income', 'expense')
- `amount_php` (DECIMAL(15, 2)) - *PHP*
- `transaction_date` (DATE)
- `category` (TEXT: e.g., 'Rent Income', 'Utilities Expense', 'Repair Expense', 'Management Fee')
- `description` (TEXT)
- `related_payment_id` (FK, UUID, NULLABLE)
- `related_maintenance_id` (FK, UUID, NULLABLE)

### 8. Owner Table
- `owner_id` (PK, UUID)
- `first_name` (TEXT)
- `last_name` (TEXT)
- `email` (TEXT)
- `phone_number` (TEXT)
- `bank_account_details` (TEXT)

### 9. User Table (for system access)
- `user_id` (PK, UUID)
- `username` (TEXT)
- `password_hash` (TEXT)
- `role` (ENUM: 'admin', 'property_manager', 'tenant', 'owner')
- `associated_entity_id` (FK, UUID, NULLABLE: links to tenant_id, owner_id, etc.)
