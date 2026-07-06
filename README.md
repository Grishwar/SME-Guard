🚀 FinPilot AI – Intelligent Financial Copilot for SMEs

AI-powered Financial Intelligence Platform for Small & Medium Enterprises (SMEs)

📌 Overview

FinPilot AI is an AI-powered Financial Copilot that helps SMEs analyze their financial health using uploaded financial statements. The system generates business insights, predicts financial risks, evaluates loan eligibility, calculates credit scores, provides GST compliance insights, and enables users to interact with an AI CFO assistant in both English and Tamil.

The project combines Machine Learning, Generative AI, Business Intelligence, and Financial Analytics into one dashboard.

✨ Features
📂 CSV Upload & Analysis
Upload financial CSV files
Automatic financial data extraction
Real-time dashboard generation
📊 Financial Dashboard
Revenue
Expenses
Cash Flow
Debt
Profit Overview
📈 Interactive Charts
Bar Chart
Pie Chart
Line Chart
Area Chart
💳 Credit Score Prediction
AI-generated business credit score
Financial health assessment
⚠ Risk Analysis
Low Risk
Medium Risk
High Risk prediction
🏦 Loan Eligibility
Loan approval prediction
Recommended loan amount
Eligibility score
💼 Banking Intelligence
Monthly inflow/outflow
Average balance
Cash flow analysis
Banking health
📄 Investor Report Generator
Download professional PDF report
Investor-ready financial summary
🧾 GST Compliance Analysis
GST insights
Tax analysis
Compliance recommendations
🤖 AI CFO Advisor

Supports:

English
Tamil

Users can ask questions like:

Should I take a loan?
How can I improve cash flow?
Reduce business expenses
Improve profitability
Investment advice

Powered using Groq LLM.

🛠 Tech Stack
Frontend
Next.js 15
React
TypeScript
Axios
Recharts
Tailwind CSS
Backend
FastAPI
Python
SQLAlchemy
Pydantic
PostgreSQL
ReportLab
AI & ML
Groq API
Llama 3
Scikit-learn
Financial Analytics
Database
PostgreSQL
📁 Project Structure
financial-health-ai
│
├── backend
│   ├── app
│   │   ├── routes
│   │   ├── services
│   │   ├── models
│   │   ├── database
│   │   └── main.py
│   │
│   ├── reports
│   ├── temp_uploads
│   └── requirements.txt
│
├── frontend
│   └── smeguard
│       ├── app
│       ├── services
│       ├── components
│       ├── public
│       └── package.json
│
└── database
    └── schema.sql
⚙ Installation
Clone Repository
git clone https://github.com/yourusername/financial-health-ai.git

cd financial-health-ai
Backend Setup
cd backend

python -m venv venv

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run backend

uvicorn app.main:app --reload

Backend runs at

http://127.0.0.1:8000

Swagger API

http://127.0.0.1:8000/docs
Frontend Setup
cd frontend/smeguard

npm install

npm run dev

Frontend

http://localhost:3000
Environment Variables

Create a .env file inside the backend folder.

DATABASE_URL=postgresql://username:password@localhost/dbname

GROQ_API_KEY=YOUR_GROQ_API_KEY
API Endpoints
Upload CSV
POST /upload
AI CFO
POST /ask-cfo
Dashboard Summary
GET /api/v1/dashboard-summary
Credit Score
GET /api/v1/credit-score
Risk Analysis
GET /api/v1/risk-analysis
Banking Insights
GET /banking-insights
Loan Eligibility
GET /loan-eligibility
Bankruptcy Check
GET /bankruptcy-check
Health Score
GET /health-score
Investor Report
GET /investor-report
GST Analysis
POST /analyze-gst
Sample AI CFO Questions
English
Should I take a business loan?
Analyze my financial health.
How can I improve cash flow?
Reduce business expenses.
Is my company financially stable?
Give investment advice.
Improve my credit score.
How can I increase profit?
Tamil
என் நிறுவனத்தின் நிதி நிலையை பகுப்பாய்வு செய்.
நான் கடன் வாங்கலாமா?
என் லாபத்தை எப்படி அதிகரிப்பது?
செலவுகளை எப்படி குறைப்பது?
என் Cash Flow எப்படி உள்ளது?
முதலீடு செய்யலாமா?
Deployment
Frontend

Deploy on Vercel

vercel
Backend

Deploy on

Render
Railway
Future Enhancements
Multi-user authentication
Role-based dashboards
Real-time banking API integration
UPI transaction analysis
AI financial forecasting
Mobile application
Voice-enabled AI CFO
Multi-language support
Advanced ML prediction models
Contributors

Grishwar S V

BE Computer Science and Engineering

Sri Ramakrishna Engineering College

License

This project is developed for educational purposes and hackathon participation.

⭐ Key Highlights
AI-powered SME Financial Copilot
Interactive Business Intelligence Dashboard
Financial Health Scoring
Credit Score Prediction
Loan Eligibility Analysis
Bankruptcy Risk Assessment
Banking Insights
GST Compliance Analysis
AI CFO Advisor (English & Tamil)
Investor-Ready PDF Report Generation
FastAPI + Next.js + PostgreSQL + Groq LLM + Recharts

This README is suitable for a GitHub repository, hackathon submission, and portfolio showcase.
