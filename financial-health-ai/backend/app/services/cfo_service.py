from app.services.ai_service import ask_llm

def get_banking_recommendations(credit_rating):
    offers = {
        "AA+": [
            {"bank": "HDFC Bank", "product": "Business Growth Loan", "rate": "8.25%"},
            {"bank": "SBI", "product": "MSME Saksham Credit", "limit": "₹25 Lakhs"}
        ],
        "A": [
            {"bank": "ICICI Bank", "product": "Working Capital Finance", "rate": "9.5%"}
        ]
    }
    return offers.get(credit_rating, offers["A"])

def generate_cfo_advice(financial, question, language):
    context = (
        f"Financial Data: Revenue {financial.revenue}, Expenses {financial.expenses}, "
        f"Debt {financial.debt}, Cashflow {financial.cashflow}. "
        f"SME Owner Question: {question}. Provide a response in {language} "
        f"categorizing expenses into Operating and Capital expenditure."
    )
    return ask_llm(context)