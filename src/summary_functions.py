def customer_summary(df):
    customer_totals = df.groupby("customer_id")["amount"].sum().reset_index()
    customer_totals = customer_totals.sort_values(by="amount", ascending=False)
    return customer_totals
