def detect_risks(financial):

    risks = []

    if financial.expenses > financial.revenue * 0.7:
        risks.append("High Expense Ratio")

    if financial.cashflow < 0:
        risks.append("Negative Cashflow")

    if financial.debt > financial.revenue:
        risks.append("Debt Overexposure")

    if not risks:
        risks.append("Low Financial Risk")

    return {"risks": risks}
