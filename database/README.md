# Database Setup

This directory contains the necessary files for setting up the PostgreSQL database for the Property Management System.

## Prerequisites

- PostgreSQL installed and running.
- `psql` command-line tool (optional, but useful for manual interaction).

## Setup Instructions

1.  **Create a PostgreSQL database:**

    First, ensure your PostgreSQL server is running. Then, create a new database and a user with appropriate permissions. You can do this via `psql` or a GUI tool like pgAdmin.

    ```bash
    # Connect to PostgreSQL as a superuser (e.g., postgres)
    psql -U postgres

    # Create a new database
    CREATE DATABASE pm_db;

    # Create a new user and set a password
    CREATE USER pm_user WITH PASSWORD 'your_password';

    # Grant all privileges on the database to the new user
    GRANT ALL PRIVILEGES ON DATABASE pm_db TO pm_user;

    # Exit psql
    \q
    ```

    **Note:** Replace `pm_db`, `pm_user`, and `your_password` with your desired values. Make sure these match the `DATABASE_URL` in your `backend/.env` file.

2.  **Run database migrations:**

    Navigate to the `backend` directory and run the Alembic migrations to create the tables defined in `models.py`.

    ```bash
    cd ../backend
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```

    This will create the necessary tables in your `pm_db` database.

## Database Schema

The database schema is defined by the SQLAlchemy models in `backend/models.py` and managed by Alembic migrations.

## Seed Data (Optional)

If you have sample data, you can add scripts here to populate your database for development or testing purposes.
