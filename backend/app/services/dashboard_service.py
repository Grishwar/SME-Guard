from app.services.health_engine import calculate_health_score

from app.services.risk_engine import detect_risk
from app.services.loan_predictor import predict_loan_eligibility

from app.services.bankruptcy_predictor import predict_bankruptcy


def build_dashboard(financial):

    health = calculate_health_score(financial)
    risk = detect_risk(financial)
    loan = predict_loan_eligibility(financial)
    bankruptcy = predict_bankruptcy(financial)

    profit = financial.revenue - financial.expenses

    return {
        "revenue": financial.revenue,
        "expenses": financial.expenses,
        "profit": profit,
        "debt": financial.debt,
        "cashflow": financial.cashflow,

        "health_score": health,
        "risk_analysis": risk,
        "loan_eligibility": loan,
        "bankruptcy_prediction": bankruptcy
    }
