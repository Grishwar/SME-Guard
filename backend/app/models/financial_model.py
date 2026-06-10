from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.database.database import Base


class Financial(Base):
    __tablename__ = "financials"

    id = Column(Integer, primary_key=True, index=True)
    revenue = Column(Float)
    debt = Column(Float)
    cashflow = Column(Float)
    expenses = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
