import random


def fetch_bank_data():

    avg_balance = random.randint(200000, 900000)
    inflow = random.randint(150000, 600000)
    outflow = random.randint(80000, 300000)

    cashflow = inflow - outflow

    # ✅ Banking Health Logic
    if avg_balance > 700000:
        bank_health = "Excellent"
        credit_score = random.randint(750, 820)
    elif avg_balance > 400000:
        bank_health = "Good"
        credit_score = random.randint(680, 749)
    else:
        bank_health = "Moderate"
        credit_score = random.randint(600, 679)

    # ✅ EMI Capacity Calculation
    emi_capacity = int(inflow * 0.35)

    # ✅ Risk Signal
    risk_flag = "Low" if cashflow > 50000 else "Medium" if cashflow > 0 else "High"

    # ✅ Smart Loan Recommendation
    recommended_loan = emi_capacity * 20

    return {

        "bank": "HDFC Mock Bank",

        "average_balance": avg_balance,

        "monthly_inflow": inflow,

        "monthly_outflow": outflow,

        "net_cashflow": cashflow,

        "bank_health": bank_health,

        "credit_score_estimate": credit_score,

        "emi_capacity": emi_capacity,

        "risk_signal": risk_flag,

        "recommended_business_loan": recommended_loan,

        "preapproved_loans": [
            {
                "bank": "HDFC",
                "amount": random.randint(300000, 900000),
                "interest": "10.5%",
                "tenure": "36 months"
            },
            {
                "bank": "ICICI",
                "amount": random.randint(200000, 700000),
                "interest": "11%",
                "tenure": "48 months"
            }
        ]
    }
