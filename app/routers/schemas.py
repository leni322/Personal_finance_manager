from pydantic import BaseModel
from datetime import datetime

from app.models import Transction


class TransactionBase(BaseModel):
    amount: float
    category: str
    timestamp: datetime
    description: str | None = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True