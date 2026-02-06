from app.services.security_service import decrypt_value


def auto_bookkeeping(financial):

    revenue = float(decrypt_value(financial.revenue))
    expenses = float(decrypt_value(financial.expenses))

    categorized = {
        "Operations": expenses * 0.35,
        "Marketing": expenses * 0.20,
        "Salaries": expenses * 0.30,
        "Misc": expenses * 0.15
    }

    anomalies = []

    if expenses > revenue * 0.8:
        anomalies.append("High expense ratio detected.")

    return {
        "expense_categories": categorized,
        "anomalies": anomalies
    }
