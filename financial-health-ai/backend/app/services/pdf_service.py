from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(financial):

    file_path = "investor_report.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    c.drawString(50, 750, "Investor Financial Report")

    c.drawString(50, 720, f"Revenue: {financial.revenue}")
    c.drawString(50, 700, f"Expenses: {financial.expenses}")
    c.drawString(50, 680, f"Cashflow: {financial.cashflow}")
    c.drawString(50, 660, f"Debt: {financial.debt}")

    c.drawString(50, 620, "AI Recommendation:")
    c.drawString(50, 600, "Business is financially stable with growth potential.")

    c.save()

    return file_path
