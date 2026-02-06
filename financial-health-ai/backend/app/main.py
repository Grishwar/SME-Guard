from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import traceback

# ✅ Database
from app.database.database import Base, engine

# ✅ Import routers
from app.routes import (
    upload_routes, chatbot_routes, credit_routes, risk_routes,
    forecast_routes, banking_routes, benchmark_routes, report_routes,
    gst_routes, health_routes, loan_routes, bankruptcy_routes,
    dashboard_routes, cfo_routes
)

app = FastAPI(
    title="FinPilot AI — Financial Copilot",
    version="1.0",
    debug=True # Set to True to help catch startup issues
)

# ✅ Auto Create Tables
Base.metadata.create_all(bind=engine)

# ✅ RECTIFIED CORS: Explicitly allow your Vercel domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://sme-guard.vercel.app",  # Your primary deployment
        "https://smeguard.netlify.app", # Your backup deployment
        "http://localhost:3000"          # For local testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ RECTIFIED ERROR HANDLER: Shows real errors for debugging
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # This prints the full error track to your Render logs
    print(f"CORE ENGINE ERROR: {traceback.format_exc()}")
    
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Core Engine Error",
            "detail": str(exc) # Shows the real error to the frontend
        },
    )

# ✅ Register Routers
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
app.include_router(cfo_routes.router)

@app.get("/")
def home():
    return {"status": "FinPilot AI running successfully 🚀"}