from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.dashboard_service import build_dashboard

router = APIRouter()

@router.get("/dashboard-summary")
def dashboard_summary(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    data = build_dashboard(financial)

    return data
