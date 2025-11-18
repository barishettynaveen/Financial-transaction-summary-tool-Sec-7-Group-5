import pandas as pd

def load_and_clean_data("C:\Users\prasa\OneDrive\Documents\Term 4\Agile\financial_transactions.csv"):
    df = pd.read_csv("C:\Users\prasa\OneDrive\Documents\Term 4\Agile\financial_transactions.csv")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['type'] = df['type'].str.lower().str.strip()
    return df

