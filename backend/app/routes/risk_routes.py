from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.risk_engine import detect_risk

router = APIRouter()


@router.get("/risk-analysis")
def risk_analysis(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first."}

    return detect_risk(financial)
