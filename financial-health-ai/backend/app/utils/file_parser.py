import pandas as pd


def parse_file(path):

    if path.endswith(".csv"):
        df = pd.read_csv(path)

    elif path.endswith(".xlsx"):
        df = pd.read_excel(path)

    else:
        raise ValueError("Unsupported file format")

    required_columns = ["revenue", "debt", "cashflow", "expenses"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return {
        "revenue": float(df["revenue"].sum()),
        "debt": float(df["debt"].sum()),
        "cashflow": float(df["cashflow"].sum()),
        "expenses": float(df["expenses"].sum())
    }
