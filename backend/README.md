# Backend (FastAPI)

This directory contains the backend application for the Property Management System, built using FastAPI.

## Setup and Installation

1.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

## Project Structure

- `main.py`: Main FastAPI application file.
- `database.py`: Database connection and session management.
- `models.py`: SQLAlchemy models for database tables.
- `schemas.py`: Pydantic schemas for request and response validation.
- `crud.py`: Create, Read, Update, Delete (CRUD) operations.
- `routers/`: Directory for API routers (e.g., `leases.py`, `tenants.py`).
- `alembic/`: Database migrations.

## Dependencies

- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg2 (for PostgreSQL)
- python-dotenv
- Alembic (for database migrations)
