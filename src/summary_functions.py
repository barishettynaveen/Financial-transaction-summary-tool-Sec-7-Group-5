
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
    customer_totals = df.groupby("customer_id")["amount"].sum().reset_index()
    customer_totals = customer_totals.sort_values(by="amount", ascending=False)
    return customer_totals
