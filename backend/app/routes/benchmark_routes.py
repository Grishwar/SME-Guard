from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.benchmark_engine import industry_benchmark

router = APIRouter()

@router.get("/benchmark")
def benchmark(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first."}

    insights = industry_benchmark(financial)

    return {
        "industry_benchmark": insights
    }
