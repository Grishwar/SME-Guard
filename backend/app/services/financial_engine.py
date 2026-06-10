def calculate_metrics(df):

    revenue = df['revenue'].sum() if 'revenue' in df.columns else 0
    expenses = df['expenses'].sum() if 'expenses' in df.columns else 0
    debt = df['debt'].sum() if 'debt' in df.columns else 0

    if 'cash' in df.columns:
        cash = df['cash'].sum()
    elif 'cashflow' in df.columns:
        cash = df['cashflow'].sum()
    else:
        cash = 0

    profit = revenue - expenses

    profit_margin = (profit / revenue * 100) if revenue else 0
    debt_ratio = (debt / revenue) if revenue else 0
    cash_runway = (cash / (expenses / 12)) if expenses else 0

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "profit_margin": round(profit_margin, 2),
        "debt_ratio": round(debt_ratio, 2),
        "cash_runway_months": round(cash_runway, 1)
    }