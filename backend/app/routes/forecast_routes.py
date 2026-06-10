from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial

router = APIRouter()


@router.get("/financial-forecast")
def financial_forecast(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first."}

    revenue = financial.revenue
    expenses = financial.expenses
    cashflow = financial.cashflow

    # Simple growth prediction logic
    projected_growth = revenue * 1.15
    projected_profit = projected_growth - expenses

    runway_months = 0
    if cashflow > 0:
        runway_months = (cashflow / expenses) * 12

    return {
        "forecasted_revenue": projected_growth,
        "projected_profit": projected_profit,
        "estimated_runway_months": runway_months
    }
