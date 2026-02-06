from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.gst_engine import analyze_gst

router = APIRouter()


@router.post("/analyze-gst")
def gst_analysis(file: UploadFile = File(...)):

    file_location = f"reports/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_gst(file_location)

    return result
