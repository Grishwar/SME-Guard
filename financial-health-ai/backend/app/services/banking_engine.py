import random

def analyze_banking(financial):

    avg_balance = financial.cashflow * random.uniform(3,6)

    emi_capacity = financial.cashflow * 0.4

    preapproved_loan = financial.revenue * 0.35

    credit_score = random.randint(700, 840)

    if credit_score > 780:
        rating = "Excellent"
    elif credit_score > 720:
        rating = "Good"
    else:
        rating = "Moderate"


    return {
        "average_bank_balance": round(avg_balance,2),
        "credit_score_estimate": credit_score,
        "credit_rating": rating,
        "emi_capacity": round(emi_capacity,2),
        "preapproved_loan_offer": round(preapproved_loan,2),
        "banking_health": "Strong"
    }
