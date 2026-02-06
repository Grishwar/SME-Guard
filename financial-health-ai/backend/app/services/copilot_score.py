def copilot_score(financial):

    score = 0

    if financial.revenue > 100000:
        score += 25

    if financial.cashflow > 0:
        score += 25

    if financial.debt < financial.revenue:
        score += 25

    if financial.expenses < financial.revenue * 0.6:
        score += 25

    return {
        "copilot_score": score,
        "status": "Strong" if score > 75 else "Average"
    }
