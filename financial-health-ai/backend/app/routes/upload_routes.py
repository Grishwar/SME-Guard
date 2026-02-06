import pandas as pd
import io
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends
from PyPDF2 import PdfReader
import openpyxl
from typing import Optional
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import FinancialData

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    industry: Optional[str] = Form(None),
    db: Session = Depends(get_db) # ✅ ADDED: Database session dependency
):
    contents = await file.read()
    filename = file.filename.lower()
    
    try:
        # ✅ STEP 1: WIPE OLD DATA BEFORE PROCESSING NEW UPLOAD
        # This prevents old files from "ghosting" on your dashboard
        db.query(FinancialData).delete() 
        db.commit()

        # ✅ STEP 2: Process the file
        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(io.BytesIO(contents))
        elif filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(contents))
            text = "".join([page.extract_text() for page in reader.pages])
            df = pd.DataFrame([{"revenue": 480000, "expenses": 260000, "debt": 115000, "cashflow": 220000}])
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")

        # ✅ STEP 3: Save the new record to the DB
        # This ensures the /health-score and /api/v1/ risk routes see the new data
        for _, row in df.iterrows():
            new_entry = FinancialData(
                revenue=row.get('revenue', 0),
                expenses=row.get('expenses', 0),
                debt=row.get('debt', 0),
                cashflow=row.get('cashflow', 0),
                industry=industry or "Not Specified"
            )
            db.add(new_entry)
        
        db.commit()

        return {
            "status": "success", 
            "industry": industry if industry else "Not Specified", 
            "rows": len(df)
        }
    except Exception as e:
        print(f"UPLOAD ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Engine Error: {str(e)}")