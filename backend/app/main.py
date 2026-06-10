from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine, Base

from app.models.financial_model import Financial
from app.models.user_model import User

from app.routes import (
    upload_routes,
    chatbot_routes,
    credit_routes,
    risk_routes,
    forecast_routes,
    banking_routes,
    benchmark_routes,
    report_routes,
    gst_routes,
    health_routes,
    loan_routes,
    bankruptcy_routes,
    dashboard_routes,
)

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FinPilot AI")

# -----------------------------
# CORS FIX
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# ROUTES
# -----------------------------
app.include_router(upload_routes.router)
app.include_router(chatbot_routes.router)
app.include_router(credit_routes.router)
app.include_router(risk_routes.router)
app.include_router(forecast_routes.router)
app.include_router(banking_routes.router)
app.include_router(benchmark_routes.router)
app.include_router(report_routes.router)
app.include_router(gst_routes.router)
app.include_router(health_routes.router)
app.include_router(loan_routes.router)
app.include_router(bankruptcy_routes.router)
app.include_router(dashboard_routes.router)

@app.get("/")
def home():
    return {
        "message": "FinPilot AI running successfully 🚀"
    }