from fastapi import FastAPI, APIRouter, Request
from belvo.belvo import get_bank_list, get_transactions

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_banks():
    data = get_bank_list()
    return data

app.include_router(router)

@app.get("/bank/{account_id}")
async def show_kpi(request: Request, account_id: str):
    # Obtener movimientos y calcular el KPI
    transactions = get_transactions(account_id)["results"]

    return transactions