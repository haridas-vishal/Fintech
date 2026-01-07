from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class FraudRule(Base):
    __tablename__ = "fraud_rules"

    id = Column(Integer, primary_key=True)
    rule_type = Column(String)
    threshold = Column(Float)
