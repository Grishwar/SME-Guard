from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.loan_predictor import predict_loan_eligibility

router = APIRouter()

@router.get("/loan-eligibility")
def loan_eligibility(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    result = predict_loan_eligibility(financial)

    return result
