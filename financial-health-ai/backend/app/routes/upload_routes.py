import pandas as pd
import io
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from PyPDF2 import PdfReader
import openpyxl
from typing import Optional # ✅ Added for optional support

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    industry: Optional[str] = Form(None) # ✅ Changed to Optional
):
    contents = await file.read()
    filename = file.filename.lower()
    
    try:
        # ✅ Support for multiple file types
        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(io.BytesIO(contents))
        elif filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(contents))
            text = "".join([page.extract_text() for page in reader.pages])
            # Mocking data extraction from PDF for hackathon demo
            df = pd.DataFrame([{"revenue": 480000, "expenses": 260000, "debt": 115000, "cashflow": 220000}])
        else:
            raise HTTPException(status_code=400, detail="Unsupported format")

        # ✅ Return success even if industry is missing
        return {
            "status": "success", 
            "industry": industry if industry else "Not Specified", 
            "rows": len(df)
        }
    except Exception as e:
        # ✅ Detailed error logging for your Render logs
        print(f"UPLOAD ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Engine Error: {str(e)}")