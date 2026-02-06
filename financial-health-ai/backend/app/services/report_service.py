from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_investor_report(financial):

    # ✅ Ensure reports folder exists
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    file_path = os.path.join(reports_dir, "investor_report.pdf")

    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont("Helvetica", 12)

    y = 750

    c.drawString(180, y, "SME INVESTMENT READINESS REPORT")

    y -= 40

    revenue = financial.revenue
    debt = financial.debt
    expenses = financial.expenses
    cashflow = financial.cashflow

    profit = revenue - expenses

    c.drawString(50, y, f"Revenue: ₹{revenue}")
    y -= 20

    c.drawString(50, y, f"Debt: ₹{debt}")
    y -= 20

    c.drawString(50, y, f"Expenses: ₹{expenses}")
    y -= 20

    c.drawString(50, y, f"Cashflow: ₹{cashflow}")
    y -= 30

    c.drawString(50, y, f"Profit: ₹{profit}")
    y -= 40

    # Investment readiness logic
    if profit > 0 and debt < revenue * 0.5:
        verdict = "INVESTMENT READY ✅"
    else:
        verdict = "HIGH RISK ⚠️"

    c.drawString(50, y, f"Verdict: {verdict}")

    c.save()

    return file_path
