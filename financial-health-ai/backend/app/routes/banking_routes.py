from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.banking_engine import analyze_banking

router = APIRouter()

@router.get("/banking-insights")
def banking_insights(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    result = analyze_banking(financial)

    return result
