from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount = Column(Float)
    location = Column(String)
    status = Column(String)
    risk_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
