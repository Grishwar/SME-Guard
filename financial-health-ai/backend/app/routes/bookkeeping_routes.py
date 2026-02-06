from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.bookkeeping_service import auto_bookkeeping

router = APIRouter()


@router.get("/auto-bookkeeping")
def bookkeeping(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"message": "Upload data first"}

    return auto_bookkeeping(financial)
