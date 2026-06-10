def detect_risk(financial):
    """
    Production-style SME Risk Analyzer
    """

    risks = []

    revenue = financial.revenue or 0
    debt = financial.debt or 0
    expenses = financial.expenses or 0
    cashflow = financial.cashflow or 0

    # Debt ratio
    if revenue > 0:
        debt_ratio = debt / revenue

        if debt_ratio > 0.7:
            risks.append("Extremely high debt compared to revenue.")
        elif debt_ratio > 0.5:
            risks.append("Moderately high debt load.")

    # Profit check
    profit = revenue - expenses

    if profit < 0:
        risks.append("Business is operating at a loss.")

    # Cashflow check
    if cashflow < 0:
        risks.append("Negative cashflow may cause liquidity crisis.")

    # Burn rate
    if expenses > revenue * 1.2:
        risks.append("Aggressive spending detected.")

    # Risk level logic
    if len(risks) == 0:
        level = "LOW"
    elif len(risks) <= 2:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "risk_level": level,
        "risks": risks
    }
