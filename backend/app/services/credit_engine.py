def calculate_credit_score(financial):
    """
    Bank-style SME credit scoring logic.
    Score Range: 300 - 900
    """

    score = 600  # Base score for SMEs

    revenue = financial.revenue
    debt = financial.debt
    expenses = financial.expenses
    cashflow = financial.cashflow

    # ✅ Debt-to-Revenue Ratio
    debt_ratio = debt / revenue if revenue else 0

    if debt_ratio < 0.3:
        score += 120
    elif debt_ratio < 0.6:
        score += 60
    else:
        score -= 80

    # ✅ Profitability
    profit = revenue - expenses

    if profit > 0:
        score += 100
    else:
        score -= 120

    # ✅ Cashflow Strength
    if cashflow > 0:
        score += 80
    else:
        score -= 100

    # Clamp score
    score = max(300, min(score, 900))

    # Rating Tier
    if score > 750:
        rating = "Excellent"
    elif score > 650:
        rating = "Good"
    elif score > 550:
        rating = "Moderate Risk"
    else:
        rating = "High Risk"

    return {
        "credit_score": score,
        "rating": rating,
        "debt_ratio": round(debt_ratio, 2),
        "profit": profit
    }
