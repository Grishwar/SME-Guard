import pandas as pd


def analyze_gst(file_path):

    df = pd.read_csv(file_path)

    total_sales = float(df["sales"].sum())
    total_tax = float(df["gst_paid"].sum())
    total_input_credit = float(df["input_credit"].sum())

    net_tax_liability = total_tax - total_input_credit

    risk = "LOW"

    if net_tax_liability > total_sales * 0.18:
        risk = "HIGH"

    if net_tax_liability < 0:
        risk = "GST REFUND EXPECTED"

    return {
        "total_sales": total_sales,
        "gst_paid": total_tax,
        "input_credit": total_input_credit,
        "net_tax_liability": net_tax_liability,
        "compliance_risk": risk
    }
