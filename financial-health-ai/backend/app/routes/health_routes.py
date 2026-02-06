from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.health_service import calculate_health

router = APIRouter()

@router.get("/health-score")
def health(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    return calculate_health(financial)
