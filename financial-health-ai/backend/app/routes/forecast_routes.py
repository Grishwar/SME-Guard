from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
# ✅ FIX: Changed 'financial' to 'financial_model' to match your file name
from app.models.financial_model import Financial 
from app.services.risk_service import detect_risks

router = APIRouter(prefix="/api/v1", tags=["Risk"])

@router.get("/risk-analysis")
def risk_analysis(db: Session = Depends(get_db)):
    # Querying the database using the corrected model import
    financial = db.query(Financial).order_by(Financial.id.desc()).first()
    
    if not financial:
        return {"status": "error", "message": "No financial data found"}
    
    # Example logic using the imported service
    risks = detect_risks(financial)
    return {"data": financial, "risks": risks}