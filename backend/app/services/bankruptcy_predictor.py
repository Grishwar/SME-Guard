def predict_bankruptcy(financial):

    profit = financial.revenue - financial.expenses
    debt_ratio = financial.debt / financial.revenue if financial.revenue else 1
    cash_burn = financial.expenses - financial.cashflow

    risk_score = 0

    # Profit check
    if profit < 0:
        risk_score += 40

    # Debt danger
    if debt_ratio > 0.8:
        risk_score += 35
    elif debt_ratio > 0.6:
        risk_score += 20

    # Cash burn
    if cash_burn > 50000:
        risk_score += 25

    # Final verdict
    if risk_score >= 70:
        status = "HIGH Bankruptcy Risk"
    elif risk_score >= 40:
        status = "Warning — Financial Stress Detected"
    else:
        status = "Financially Stable"

    return {
        "bankruptcy_risk_score": risk_score,
        "status": status
    }
