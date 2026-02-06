from fastapi import APIRouter
from app.services.benchmark_service import get_industry_benchmark

router = APIRouter()

@router.get("/benchmark/{industry}")
def benchmark(industry: str):
    return get_industry_benchmark(industry)
