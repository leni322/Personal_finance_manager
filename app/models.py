from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, index=True)
    timestamp = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
