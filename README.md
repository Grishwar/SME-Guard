FinPilot AI — SME Financial Copilot
FinPilot AI is an end-to-end financial intelligence platform designed to help Small and Medium Enterprises (SMEs) assess their investment readiness and financial health. Built for the HCL GUVI Hackathon 2026, this tool uses AI to bridge the gap between complex financial data and actionable business strategy.

🚀 Key Features
Financial Health & Risk Scoring: Generates a comprehensive Health Score (0-100) and predicts Bankruptcy risk levels (Stable/Warning).

Banking Health Engine: Analyzes average balances to categorize business health (Excellent, Good, Moderate) and simulates realistic Credit Scores.

Smart Loan Recommendations: Calculates EMI Capacity (30-35% of inflow) to suggest pre-approved loan amounts up to 20x capacity.

Bilingual AI CFO Advisor: A specialized chatbot powered by Llama 3.3 that provides strategic advice in both English and Tamil (தமிழ்).

Automated Bookkeeping: Categorizes raw transaction data into Operating and Capital expenditures while estimating GST Due.

Interactive Visualizations: High-fidelity charts (Area, Bar, Pie) with permanent data labels for instant trend analysis.

🛠️ Tech Stack
Frontend
Framework: Next.js (React).

Design: Tailwind CSS with Glassmorphism UI.

Charts: Recharts with static label support.

Backend
Framework: FastAPI (Python).

Database: PostgreSQL for secure storage of financial records.

AI Engine: Groq API (Llama 3.3 70B Versatile).

📊 Business Logic Examples
EMI Capacity Calculation
Python
# Calculates the sustainable loan repayment capacity
emi_capacity = int(monthly_inflow * 0.35)
recommended_loan = emi_capacity * 20
Banking Health Logic
Balance > 7L: Health = Excellent | Credit Score = 750-820.

Balance > 4L: Health = Good | Credit Score = 680-749.

Balance < 4L: Health = Moderate | Credit Score = 600-679.

📂 Project Structure
Bash
financial-health-ai/
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI Core
│   │   ├── routes/           # AI, Banking, and Risk Endpoints
│   │   └── services/         # Health & Loan Logic
├── frontend/
│   └── smeguard/
│       ├── app/
│       │   └── page.tsx      # Main Dashboard
│       └── lib/
│           └── api.ts        # Backend Communication
└── README.md
🎯 HCL Hackathon Compliance
This project fulfills all requirements for the SME Financial Health & Investment Readiness problem statement:

Deployment: Hosted live for public access.

Multilingual: Tamil support for regional accessibility.

Data Security: Implemented with PostgreSQL for persistent data handling.
