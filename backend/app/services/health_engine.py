def calculate_health_score(financial):
    score = 100

    # Debt ratio
    if financial.debt > financial.revenue * 0.6:
        score -= 25

    # Low cashflow
    if financial.cashflow < financial.expenses * 0.3:
        score -= 20

    # Profitability
    profit = financial.revenue - financial.expenses
    if profit < 0:
        score -= 30

    # Expense overload
    if financial.expenses > financial.revenue * 0.8:
        score -= 15

    return max(score, 0)
