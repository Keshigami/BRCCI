## Sample Data for a Commercial Property in Metro Manila (All values in PHP)

### 1. Owner Data
- **Owner 1:**
    - `owner_id`: `uuid-owner-001`
    - `first_name`: `Maria`
    - `last_name`: `Santos`
    - `email`: `maria.santos@example.com`
    - `phone_number`: `+639171234567`
    - `bank_account_details`: `BDO Savings 123-456-789`

### 2. Property Data
- **Property 1 (Commercial Building in Quezon City):**
    - `property_id`: `uuid-property-001`
    - `address`: `123 Commercial Ave, Brgy. San Roque`
    - `city`: `Quezon City`
    - `province`: `Metro Manila`
    - `zip_code`: `1109`
    - `property_type`: `commercial`
    - `owner_id`: `uuid-owner-001`
    - `acquisition_date`: `2018-05-20`
    - `market_value_php`: `80000000.00`

### 3. Unit Data
- **Unit 1 (Ground Floor Showroom):**
    - `unit_id`: `uuid-unit-001`
    - `property_id`: `uuid-property-001`
    - `unit_number`: `Ground Floor Showroom`
    - `floor_area_sqm`: `250.00`
    - `unit_type`: `showroom`
    - `number_of_bedrooms`: `NULL`
    - `number_of_bathrooms`: `2`
    - `current_rental_rate_php`: `150000.00`
    - `status`: `occupied`
- **Unit 2 (Second Floor Warehouse):**
    - `unit_id`: `uuid-unit-002`
    - `property_id`: `uuid-property-001`
    - `unit_number`: `Second Floor Warehouse`
    - `floor_area_sqm`: `300.00`
    - `unit_type`: `warehousing`
    - `number_of_bedrooms`: `NULL`
    - `number_of_bathrooms`: `1`
    - `current_rental_rate_php`: `120000.00`
    - `status`: `occupied`
- **Unit 3 (Third Floor Office/Showroom):**
    - `unit_id`: `uuid-unit-003`
    - `property_id`: `uuid-property-001`
    - `unit_number`: `Third Floor Office/Showroom`
    - `floor_area_sqm`: `200.00`
    - `unit_type`: `showroom`
    - `number_of_bedrooms`: `NULL`
    - `number_of_bathrooms`: `2`
    - `current_rental_rate_php`: `100000.00`
    - `status`: `vacant`

### 4. Tenant Data
- **Tenant 1 (Showroom Tenant):**
    - `tenant_id`: `uuid-tenant-001`
    - `first_name`: `ABC Retail Inc.`
    - `last_name`: `(Company)`
    - `email`: `leasing@abcretail.com`
    - `phone_number`: `+63281234567`
    - `id_type`: `SEC Registration`
    - `id_number`: `CS201012345`
    - `date_of_birth`: `NULL`
    - `nationality`: `Filipino Corporation`
- **Tenant 2 (Warehouse Tenant):**
    - `tenant_id`: `uuid-tenant-002`
    - `first_name`: `XYZ Logistics Co.`
    - `last_name`: `(Company)`
    - `email`: `info@xyzlogistics.ph`
    - `phone_number`: `+63289876543`
    - `id_type`: `DTI Registration`
    - `id_number`: `0123456789`
    - `date_of_birth`: `NULL`
    - `nationality`: `Filipino Corporation`

### 5. Lease Agreement Data
- **Lease 1 (ABC Retail Inc. for Ground Floor Showroom):**
    - `lease_id`: `uuid-lease-001`
    - `unit_id`: `uuid-unit-001`
    - `tenant_id`: `uuid-tenant-001`
    - `start_date`: `2024-01-01`
    - `end_date`: `2026-12-31`
    - `monthly_rent_php`: `150000.00`
    - `security_deposit_php`: `450000.00` (3 months rent)
    - `advance_payment_php`: `300000.00` (2 months rent)
    - `payment_due_day`: `1`
    - `lease_status`: `active`
    - `last_rent_increase_date`: `NULL`
    - `next_rent_increase_date`: `NULL`
    - `rent_increase_percentage`: `NULL`
- **Lease 2 (XYZ Logistics Co. for Second Floor Warehouse):**
    - `lease_id`: `uuid-lease-002`
    - `unit_id`: `uuid-unit-002`
    - `tenant_id`: `uuid-tenant-002`
    - `start_date`: `2023-07-01`
    - `end_date`: `2025-06-30`
    - `monthly_rent_php`: `120000.00`
    - `security_deposit_php`: `360000.00` (3 months rent)
    - `advance_payment_php`: `240000.00` (2 months rent)
    - `payment_due_day`: `15`
    - `lease_status`: `active`
    - `last_rent_increase_date`: `NULL`
    - `next_rent_increase_date`: `NULL`
    - `rent_increase_percentage`: `NULL`

### 6. Payment Data
- **Payment 1 (Jan 2024 Rent - ABC Retail Inc.):**
    - `payment_id`: `uuid-payment-001`
    - `lease_id`: `uuid-lease-001`
    - `amount_php`: `150000.00`
    - `payment_date`: `2024-01-01 09:00:00`
    - `payment_type`: `bank_transfer`
    - `status`: `paid`
    - `description`: `January 2024 Rent - Ground Floor Showroom`
    - `receipt_number`: `RCPT-20240101-001`
- **Payment 2 (Security Deposit - ABC Retail Inc.):**
    - `payment_id`: `uuid-payment-002`
    - `lease_id`: `uuid-lease-001`
    - `amount_php`: `450000.00`
    - `payment_date`: `2023-12-20 11:00:00`
    - `payment_type`: `bank_transfer`
    - `status`: `paid`
    - `description`: `Security Deposit - Ground Floor Showroom`
    - `receipt_number`: `RCPT-20231220-001`
- **Payment 3 (July 2024 Rent - XYZ Logistics Co.):**
    - `payment_id`: `uuid-payment-003`
    - `lease_id`: `uuid-lease-002`
    - `amount_php`: `120000.00`
    - `payment_date`: `2024-07-14 16:00:00`
    - `payment_type`: `online_gateway`
    - `status`: `paid`
    - `description`: `July 2024 Rent - Second Floor Warehouse`
    - `receipt_number`: `RCPT-20240714-001`

### 7. Maintenance Request Data
- **Maintenance Request 1 (HVAC Repair - Showroom):**
    - `request_id`: `uuid-maintenance-001`
    - `unit_id`: `uuid-unit-001`
    - `tenant_id`: `uuid-tenant-001`
    - `description`: `HVAC system not cooling effectively in showroom.`
    - `category`: `electrical`
    - `date_submitted`: `2024-07-05 14:00:00`
    - `status`: `new`
    - `assigned_to`: `NULL`
    - `completion_date`: `NULL`
    - `cost_php`: `NULL`
    - `notes`: `Tenant reported issue.`
- **Maintenance Request 2 (Loading Dock Door Repair - Warehouse):**
    - `request_id`: `uuid-maintenance-002`
    - `unit_id`: `uuid-unit-002`
    - `tenant_id`: `uuid-tenant-002`
    - `description`: `Loading dock roll-up door is stuck.`
    - `category`: `structural`
    - `date_submitted`: `2024-07-01 10:30:00`
    - `status`: `in_progress`
    - `assigned_to`: `Mang Tonyo - General Contractor`
    - `completion_date`: `NULL`
    - `cost_php`: `NULL`
    - `notes`: `Awaiting parts for repair.`

### 8. Financial Transaction Data
- **Transaction 1 (Rent Income - Showroom):**
    - `transaction_id`: `uuid-ft-001`
    - `property_id`: `uuid-property-001`
    - `unit_id`: `uuid-unit-001`
    - `transaction_type`: `income`
    - `amount_php`: `150000.00`
    - `transaction_date`: `2024-01-01`
    - `category`: `Rent Income`
    - `description`: `Monthly rent from ABC Retail Inc. (Ground Floor Showroom)`
    - `related_payment_id`: `uuid-payment-001`
    - `related_maintenance_id`: `NULL`
- **Transaction 2 (Security Deposit Income - Showroom):**
    - `transaction_id`: `uuid-ft-002`
    - `property_id`: `uuid-property-001`
    - `unit_id`: `uuid-unit-001`
    - `transaction_type`: `income`
    - `amount_php`: `450000.00`
    - `transaction_date`: `2023-12-20`
    - `category`: `Security Deposit`
    - `description`: `Security deposit from ABC Retail Inc. (Ground Floor Showroom)`
    - `related_payment_id`: `uuid-payment-002`
    - `related_maintenance_id`: `NULL`
- **Transaction 3 (Rent Income - Warehouse):**
    - `transaction_id`: `uuid-ft-003`
    - `property_id`: `uuid-property-001`
    - `unit_id`: `uuid-unit-002`
    - `transaction_type`: `income`
    - `amount_php`: `120000.00`
    - `transaction_date`: `2024-07-14`
    - `category`: `Rent Income`
    - `description`: `Monthly rent from XYZ Logistics Co. (Second Floor Warehouse)`
    - `related_payment_id`: `uuid-payment-003`
    - `related_maintenance_id`: `NULL`

