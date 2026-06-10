from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.bankruptcy_predictor import predict_bankruptcy

router = APIRouter()

@router.get("/bankruptcy-check")
def bankruptcy_check(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    result = predict_bankruptcy(financial)

    return result
