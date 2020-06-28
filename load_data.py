import pandas as pd


def load_dataset(path):
    """Method to load data from an Excel file to DataFrame format"""
    df = pd.read_excel(path)
    X = list(df["text"])
    y = df.drop("text", 1)
    return X, y
