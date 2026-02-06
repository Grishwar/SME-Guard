from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.credit_engine import calculate_credit_score

router = APIRouter(prefix="/api/v1", tags=["Credit"])

@router.get("/credit-score")
def get_credit_score(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "No financial data found"}

    score = calculate_credit_score(financial)

    return {"credit_score": score}
