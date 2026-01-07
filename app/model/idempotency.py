from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.core.database import Base

class IdempotencyKey(Base):
    __tablename__ = "idempotency_keys"

    key = Column(String, primary_key=True)
    response = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
