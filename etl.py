import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Example: drop rows with missing values
    df_clean = df.dropna()
    # Example: remove outliers or do simple transformations if needed
    return df_clean

def feature_engineering(df):
    # Example: create a new column
    # e.g., df['total_amount'] = df['quantity'] * df['price']
    return df

if __name__ == "__main__":
    df = load_data("data/raw/villagers.csv")
    df = clean_data(df)
    df = feature_engineering(df)
    df.to_csv("data/processed/villagers_clean.csv", index=False)
    print("ETL pipeline completed successfully!")

#This file is "modified"