def predict_loan_eligibility(financial):

    profit = financial.revenue - financial.expenses
    debt_ratio = financial.debt / financial.revenue if financial.revenue else 1
    cash_ratio = financial.cashflow / financial.expenses if financial.expenses else 0

    score = 0

    # Profitability
    if profit > 0:
        score += 30
    else:
        score -= 20

    # Debt health
    if debt_ratio < 0.4:
        score += 30
    elif debt_ratio < 0.7:
        score += 10
    else:
        score -= 25

    # Cash strength
    if cash_ratio > 0.5:
        score += 25
    else:
        score -= 10

    # Final Decision
    if score >= 60:
        status = "Highly Eligible"
        loan_amount = financial.revenue * 0.5

    elif score >= 35:
        status = "Eligible"
        loan_amount = financial.revenue * 0.3

    else:
        status = "Risky — Manual Review Required"
        loan_amount = financial.revenue * 0.1

    return {
        "loan_status": status,
        "eligibility_score": score,
        "recommended_loan_amount": round(loan_amount, 2)
    }
