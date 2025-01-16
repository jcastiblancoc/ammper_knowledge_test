from fastapi import FastAPI
from app.api.v1.endpoints import users, transactions

app = FastAPI(title="My FastAPI App")

# Incluir las rutas
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["Transactions"])