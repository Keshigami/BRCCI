from fastapi import FastAPI
from .routers import leases, tenants, properties, units, payments, maintenance, financial, owners, users

app = FastAPI(
    title="Property Management System API",
    description="API for managing properties, leases, tenants, payments, and maintenance requests in the Philippine context.",
    version="0.1.0",
)

app.include_router(properties.router, prefix="/properties", tags=["properties"])
app.include_router(units.router, prefix="/units", tags=["units"])
app.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
app.include_router(leases.router, prefix="/leases", tags=["leases"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["maintenance"])
app.include_router(financial.router, prefix="/financial", tags=["financial"])
app.include_router(owners.router, prefix="/owners", tags=["owners"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Property Management System API"}
