from app.services.security_service import decrypt_value


def build_dashboard(financial):

    revenue = float(decrypt_value(financial.revenue))
    expenses = float(decrypt_value(financial.expenses))
    cashflow = float(decrypt_value(financial.cashflow))
    debt = float(decrypt_value(financial.debt))

    return {
        "revenue": revenue,
        "expenses": expenses,
        "cashflow": cashflow,
        "debt": debt,
        "industry": financial.industry,

        "chart_data": [
            {"name": "Revenue", "value": revenue},
            {"name": "Expenses", "value": expenses},
            {"name": "Cashflow", "value": cashflow},
            {"name": "Debt", "value": debt},
        ]
    }
