def detect_risk(financial):

    if isinstance(financial, dict):
        revenue = financial.get("revenue", 0)
        debt = financial.get("debt", 0)
        cashflow = financial.get("cashflow", 0)
        expenses = financial.get("expenses", 0)
    else:
        revenue = financial.revenue or 0
        debt = financial.debt or 0
        cashflow = financial.cashflow or 0
        expenses = financial.expenses or 0

    risks = []

    if debt > revenue:
        risks.append("High Debt Risk")

    if cashflow < 0:
        risks.append("Negative Cashflow")

    if expenses > revenue:
        risks.append("Operational Loss Risk")

    if not risks:
        risks.append("Low Risk")

    return risks
