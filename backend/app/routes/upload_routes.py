from fastapi import APIRouter, UploadFile, File, Depends
import shutil
import os

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.utils.file_parser import parse_file
from app.services.credit_engine import calculate_credit_score
from app.services.risk_engine import detect_risk
from app.models.financial_model import Financial

router = APIRouter()

UPLOAD_FOLDER = "temp_uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Parse financial data
    data = parse_file(file_path)

    # Store in DB
    financial_entry = Financial(
        revenue=data["revenue"],
        debt=data["debt"],
        cashflow=data["cashflow"],
        expenses=data["expenses"]
    )

    db.add(financial_entry)
    db.commit()
    db.refresh(financial_entry)

    # Credit score
    credit_score = calculate_credit_score(financial_entry)

    # Risk detection
    risks = detect_risk(financial_entry)

    return {
        "message": "File processed successfully",
        "financial_data": data,
        "credit_score": credit_score,
        "risks": risks
    }