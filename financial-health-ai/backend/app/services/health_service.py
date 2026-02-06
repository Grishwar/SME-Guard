def calculate_health(financial):

    score = 50

    if financial.revenue > financial.expenses:
        score += 20

    if financial.cashflow > 0:
        score += 15

    if financial.debt < financial.revenue * 0.5:
        score += 15

    verdict = "Excellent" if score > 80 else "Moderate" if score > 60 else "Risky"

    return {
        "health_score": score,
        "verdict": verdict
    }
