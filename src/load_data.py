
import pandas as pd

def load_and_clean_data(file_path):
    
    #Loads the financial transactions CSV file and cleans it.
  
    # Load CSV
    df = pd.read_csv(file_path)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Standardize transaction type
    df["type"] = df["type"].str.lower().str.strip()

    # Keep only valid types
    df = df[df["type"].isin(["credit", "debit"])]

    return df
