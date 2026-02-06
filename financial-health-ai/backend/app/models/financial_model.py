from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Financial(Base):
    __tablename__ = "financials"

    id = Column(Integer, primary_key=True, index=True)

    revenue = Column(String)
    expenses = Column(String)
    cashflow = Column(String)
    debt = Column(String)

    # ⭐ NEW — Industry Support
    industry = Column(String, nullable=True)
