import pandas as pd

def load_transactions(path="financial_transactions.csv"):
    print("US-01: Loading transactions...")
    df = pd.read_csv(path)
    return df
