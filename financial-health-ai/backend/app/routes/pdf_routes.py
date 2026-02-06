from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.financial_model import Financial
from app.services.pdf_service import generate_pdf   # ✅ IMPORTANT

router = APIRouter()


@router.get("/investor-report")
def investor_report(db: Session = Depends(get_db)):

    financial = db.query(Financial).order_by(Financial.id.desc()).first()

    if not financial:
        return {"error": "Upload financial data first"}

    file_path = generate_pdf(financial)

    return FileResponse(
        path=file_path,
        media_type='application/pdf',
        filename="Investor_Report.pdf"
    )
