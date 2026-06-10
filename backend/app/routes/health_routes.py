from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.health_engine import calculate_health_score


router = APIRouter()

@router.get("/health-score")
def health_score(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    score = calculate_health_score(financial)

    verdict = "Excellent" if score > 80 else \
              "Good" if score > 60 else \
              "Risky" if score > 40 else \
              "Critical"

    return {
        "health_score": score,
        "verdict": verdict
    }
