def calculate_credit_score(financial):
    """
    Accepts Financial object OR dict
    """

    if isinstance(financial, dict):
        revenue = financial.get("revenue", 0)
        debt = financial.get("debt", 0)
        cashflow = financial.get("cashflow", 0)
    else:
        revenue = financial.revenue or 0
        debt = financial.debt or 0
        cashflow = financial.cashflow or 0

    score = 600

    if revenue > debt:
        score += 50

    if cashflow > 0:
        score += 50

    if debt > revenue:
        score -= 100

    return max(300, min(score, 900))
