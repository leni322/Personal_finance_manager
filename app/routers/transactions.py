from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Transaction)
async def create_transaction(
        transction: schemas.TransactionCreate,
        db: AsyncSession =Depends(get_db)
):
    new_transaction = models.Transaction(**transction.dict())
    db.add(new_transaction)
    await db.commit()
    await db.refresh(new_transaction)
    return new_transaction