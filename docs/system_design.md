# Property Management System for the Philippines

## System Design

### 1. Architecture Overview
The system will follow a modular, web-based architecture, accessible via a secure web interface. It will consist of a frontend (user interface), a backend (business logic and API), and a database (data storage).

### 2. Core Modules

#### 2.1. Lease Management Module
- **Purpose:** To manage all aspects of property leases, from creation to termination.
- **Key Features:**
    - Lease agreement creation and digital signing.
    - Tenant information management (personal details, contact, identification).
    - Property unit assignment and tracking.
    - Lease term definition (start/end dates, duration).
    - Rent amount, due dates, and payment schedules.
    - Security deposit and advance payment tracking.
    - Automated rent increase calculation based on legal limits.
    - Lease renewal and termination workflows.
    - Document storage for lease agreements, IDs, etc.

#### 2.2. Rent Collection Module
- **Purpose:** To facilitate and track rent and other payment collections.
- **Key Features:**
    - Automated invoicing and payment reminders.
    - Multiple payment options (bank transfer, online payment gateways, cash).
    - Payment tracking and reconciliation.
    - Late payment penalties and interest calculation (compliant with laws).
    - Generation of official receipts.
    - Arrears management and reporting.

#### 2.3. Maintenance Tracking Module
- **Purpose:** To manage property maintenance requests, schedules, and costs.
- **Key Features:**
    - Tenant portal for submitting maintenance requests.
    - Categorization of maintenance issues (e.g., plumbing, electrical, structural).
    - Assignment of tasks to maintenance personnel or third-party contractors.
    - Tracking of maintenance status (pending, in progress, completed).
    - Cost tracking for repairs and maintenance.
    - History log of all maintenance activities per property unit.
    - Automated reminders for routine maintenance (e.g., AC cleaning).

#### 2.4. Financial Reporting Module
- **Purpose:** To provide comprehensive financial insights and reports.
- **Key Features:**
    - Income and expense tracking.
    - Generation of financial statements (e.g., income statements, balance sheets).
    - Rent roll reports.
    - Delinquency reports.
    - Owner statements (income, expenses, disbursements).
    - Tax reporting assistance (e.g., withholding tax on rent).
    - Customizable reporting periods.
    - All monetary values in Philippine Pesos (PHP).

### 3. Legal Compliance Features (Integrated)

#### 3.1. Automated Rent Increase Calculation
- System will automatically calculate and propose rent increases based on the Rent Control Act of 2009 (e.g., 7% in Metro Manila, 10% elsewhere), allowing for manual override with justification.

#### 3.2. Security Deposit Handling
- Dedicated fields for security deposit amount, date received, and clear policies for return conditions and deductions, in compliance with the Civil Code.

#### 3.3. Maintenance and Habitability Tracking
- Maintenance module ensures timely resolution of issues, documenting compliance with habitability requirements under the Civil Code and National Building Code.

#### 3.4. Eviction Procedures
- Workflow to document and track eviction processes, emphasizing the requirement for court orders and adherence to tenant protection laws. System will not initiate physical eviction.

#### 3.5. Documentation and Disclosure
- Centralized document storage for all legal documents (leases, notices, permits).
- Automated generation of disclosure statements for fees and charges.

### 4. Data Model Considerations (High-Level)

- **Property:** Property ID, Address, Type (residential, commercial), Owner ID.
- **Unit:** Unit ID, Property ID, Unit Number, Area, Rental Rate (PHP), Status.
- **Tenant:** Tenant ID, Name, Contact Info, ID Details, Lease History.
- **Lease Agreement:** Lease ID, Unit ID, Tenant ID, Start Date, End Date, Monthly Rent (PHP), Security Deposit (PHP), Advance Payment (PHP), Payment Due Date.
- **Payment:** Payment ID, Lease ID, Amount (PHP), Date Paid, Payment Type, Status.
- **Maintenance Request:** Request ID, Unit ID, Tenant ID, Description, Date Submitted, Status, Assigned To, Cost (PHP).
- **Financial Transaction:** Transaction ID, Type (income/expense), Amount (PHP), Date, Category, Description.

### 5. Technology Stack (Proposed)
- **Frontend:** React.js / Next.js (for server-side rendering and SEO)
- **Backend:** Node.js with Express.js or Python with FastAPI (RESTful API)
- **Database:** PostgreSQL (relational, robust, good for financial data)
- **Cloud Platform:** AWS / Azure / GCP (for scalability and security)
- **Payment Gateway Integration:** Local Philippine payment gateways (e.g., PayMongo, Dragonpay) for PHP transactions.
