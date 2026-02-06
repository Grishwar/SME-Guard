from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from pydantic import BaseModel
from app.services.cfo_service import generate_cfo_advice

router = APIRouter()

class CFORequest(BaseModel):
    question: str
    language: str

@router.post("/cfo/ask")
def ask_cfo(request: CFORequest, db: Session = Depends(get_db)):
    # ✅ FETCH THE FINANCIAL DATA THE SERVICE REQUIRES
    financial = db.query(Financial).order_by(Financial.id.desc()).first()
    
    if not financial:
        raise HTTPException(status_code=404, detail="No financial data found. Please upload a CSV first.")

    # ✅ PASS THE 'financial' ARGUMENT TO FIX THE TYPEERROR
    advice = generate_cfo_advice(
        financial=financial,
        question=request.question,
        language=request.language
    )
    return {"answer": advice}