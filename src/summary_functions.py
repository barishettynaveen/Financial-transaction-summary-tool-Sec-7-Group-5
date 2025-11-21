
def calculate_income_expense(df):
    """
    Calculates total income (credit) and total expenses (debit).
    """

    income = df[df["type"] == "credit"]["amount"].sum()
    expense = df[df["type"] == "debit"]["amount"].sum()

    return {
        "total_income": income,
        "total_expense": expense
    }

def customer_summary(df):
    """
    Creates a customer-level spending summary.
    """

    summary = (
        df.groupby("customer_id")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return summary



