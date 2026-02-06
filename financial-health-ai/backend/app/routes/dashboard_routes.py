from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial

router = APIRouter(prefix="/api/v1", tags=["Dashboard"])

@router.get("/dashboard-summary")
def dashboard_summary(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "No financial data"}

    return {
        "revenue": float(financial.revenue),
        "expenses": float(financial.expenses),
        "debt": float(financial.debt),
        "cashflow": float(financial.cashflow)
    }
