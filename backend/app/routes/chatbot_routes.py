from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.cfo_advisor import generate_cfo_advice

router = APIRouter()


class CFORequest(BaseModel):
    question: str
    language: str = "english"   # default


@router.post("/ask-cfo")
def ask_cfo(request: CFORequest, db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first."}

    advice = generate_cfo_advice(
        financial,
        request.question,
        request.language
    )

    return {
        "cfo_advice": advice
    }
