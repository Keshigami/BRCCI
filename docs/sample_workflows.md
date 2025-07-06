## Sample Workflows for a Commercial Property in Metro Manila

### Workflow 1: New Lease Agreement Creation (Commercial Showroom)

1.  **Property Manager Action:** Property Manager logs into the system.
2.  **System Action:** Navigates to the 'Lease Management' module.
3.  **Property Manager Action:** Clicks 'Create New Lease'.
4.  **System Action:** Presents a form for lease details.
5.  **Property Manager Action:** Enters `unit_id` (e.g., `uuid-unit-001` for Ground Floor Showroom), `tenant_id` (e.g., `uuid-tenant-001` for ABC Retail Inc.), `start_date` (`2024-01-01`), `end_date` (`2026-12-31`), `monthly_rent_php` (`150000.00`), `security_deposit_php` (`450000.00`), `advance_payment_php` (`300000.00`), and `payment_due_day` (`1`).
6.  **System Action:** (For commercial leases, rent increase calculations might differ or be subject to negotiation, so automated calculation based on Rent Control Act might not apply directly. The system would allow manual input or flag for review based on lease terms.)
7.  **Property Manager Action:** Uploads scanned copies of tenant company registration, authorized signatory IDs, and signed physical lease agreement.
8.  **System Action:** Saves the new lease agreement (`uuid-lease-001`) to the database, updates unit status to 'occupied'.
9.  **System Action:** Generates an automated welcome email to the tenant company with lease summary and payment instructions.

### Workflow 2: Monthly Rent Collection and Payment Tracking (Commercial Warehouse)

1.  **System Action (Automated):** On the 1st of each month, the system generates an invoice for active leases (e.g., for `uuid-lease-002`, July 2024 rent of `120000.00 PHP`).
2.  **System Action (Automated):** Sends an automated payment reminder email to the tenant (XYZ Logistics Co.) on the 10th of the month (assuming payment due on 15th).
3.  **Tenant Action:** XYZ Logistics Co. receives the reminder and makes an online payment of `120000.00 PHP` via the integrated payment gateway on `2024-07-14`.
4.  **System Action:** Payment gateway notifies the system of successful payment.
5.  **System Action:** Records the payment (`uuid-payment-003`) in the `Payment` table, linking it to `uuid-lease-002`. Updates payment status to 'paid'.
6.  **System Action:** Creates a corresponding `Financial Transaction` entry (`uuid-ft-003`) for 'Rent Income' of `120000.00 PHP`.
7.  **System Action:** Generates and sends an official receipt to the tenant company.
8.  **System Action (Automated):** If payment is not received by the due date (15th), the system flags the lease as 'overdue' and sends a late payment reminder. If configured, it calculates and applies late fees as per the commercial lease agreement.

### Workflow 3: Maintenance Request and Resolution (Commercial Property)

1.  **Tenant Action:** ABC Retail Inc. reports that the HVAC system in their showroom is not cooling effectively. They log into the tenant portal.
2.  **System Action:** Navigates to the 'Maintenance Tracking' module.
3.  **Tenant Action:** Clicks 'Submit New Request', selects `unit_id` (`uuid-unit-001`), enters `description` ('HVAC system not cooling effectively in showroom.'), and selects `category` ('electrical').
4.  **System Action:** Creates a new `Maintenance Request` entry (`uuid-maintenance-001`) with status 'new' and notifies the Property Manager.
5.  **Property Manager Action:** Property Manager reviews the request, assigns it to an HVAC technician, and updates the status to 'in_progress'.
6.  **Technician Action:** The HVAC technician completes the repair on `2024-07-15` and submits the cost of `8000.00 PHP` for parts and labor.
7.  **Property Manager Action:** Property Manager updates the `Maintenance Request` status to 'completed', enters `completion_date` (`2024-07-15`), and `cost_php` (`8000.00`).
8.  **System Action:** Creates a `Financial Transaction` entry for 'Repair Expense' of `8000.00 PHP` linked to `uuid-maintenance-001` and `uuid-property-001`.
9.  **System Action:** Notifies the tenant company that the request has been completed.

### Workflow 4: Lease Renewal and Rent Adjustment (Commercial Lease)

1.  **System Action (Automated):** Six months before `end_date` (e.g., `2026-06-30` for `uuid-lease-001`), the system flags the lease for renewal discussion.
2.  **Property Manager Action:** Property Manager initiates renewal discussions with ABC Retail Inc. and negotiates new terms, including a potential rent adjustment.
3.  **Property Manager Action:** Once new terms are agreed upon, the Property Manager updates the `monthly_rent_php` (e.g., to `165000.00 PHP` for a 10% increase) and `end_date` in the `Lease Agreement` table.
4.  **System Action:** Generates a new lease agreement or an addendum reflecting the updated terms.
5.  **System Action:** Updates `last_rent_increase_date` to the effective date of the new rent. (Note: Rent Control Act typically applies to residential leases. Commercial rent increases are usually governed by lease terms.)
