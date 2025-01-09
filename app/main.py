from fastapi import FastAPI
from app.routers import transactions
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Personal Finance Manager API!"}

app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
