import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
print("LOADED KEY:", os.getenv("GROQ_API_KEY"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_cfo_advice(financial, question, language="english"):

    revenue = financial.revenue
    debt = financial.debt
    expenses = financial.expenses
    cashflow = financial.cashflow

    # Language Control
    if language.lower() == "tamil":
        language_instruction = "Respond fully in Tamil language using professional financial vocabulary."
    else:
        language_instruction = "Respond fully in English."

    prompt = f"""
You are an expert Chief Financial Officer (CFO) AI helping small and medium businesses.

Financial Data:
Revenue: {revenue}
Debt: {debt}
Expenses: {expenses}
Cashflow: {cashflow}

User Question:
{question}

Instructions:
- Analyze financial health
- Identify risks
- Suggest cost optimizations
- Recommend growth strategies
- Be practical and business-focused
- Keep response structured and professional
- {language_instruction}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # ✅ Active Groq model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return completion.choices[0].message.content
