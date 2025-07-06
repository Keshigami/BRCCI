# Property Management System for the Philippines (BRCCI)

This repository contains the codebase for a Property Management System tailored for the Philippine context, incorporating legal compliance features.

## Project Structure

- `backend/`: Contains the server-side application logic (API).
- `frontend/`: Contains the user interface (web application).
- `database/`: Contains database schema, migrations, and seed data.
- `docs/`: Contains design documents, data models, and legal compliance notes. (This will be created soon)

## Setup and Installation

Detailed setup instructions for each component will be provided within their respective directories.

### Prerequisites

- Node.js and npm (for frontend)
- Python 3.13.5 (for backend)
- PostgreSQL (database)

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd BRCCI
    ```
2.  **Database Setup:**
    Refer to `database/README.md` for instructions on setting up your PostgreSQL database and running migrations.
3.  **Backend Setup:**
    Refer to `backend/README.md` for instructions.
4.  **Frontend Setup:**
    Refer to `frontend/README.md` for instructions.

## Running the Application

To run the full application, you need to start both the backend API and the frontend development server.

1.  **Start the Backend:**
    Open a new terminal, navigate to the `backend` directory, and run:
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    The backend API will be accessible at `http://localhost:8000`.

2.  **Start the Frontend:**
    Open another new terminal, navigate to the `frontend` directory, and run:
    ```bash
    cd frontend
    npm install
    npm start
    ```
    The frontend application will open in your browser, usually at `http://localhost:3000`.

## Core Modules

- Lease Management
- Rent Collection
- Maintenance Tracking
- Financial Reporting

## Legal Compliance

The system is designed with features to comply with Philippine laws, including:

- Rent Control Act of 2009
- Civil Code (Security Deposit, Habitability)
- National Building Code

## Contributing

Further details on contributing will be added.
