import pandas as pd

"""Method to load data from an Excel file to DataFrame format"""
def load_dataset(path):
    df = pd.read_excel(path)
    X = list(df["text"])
    # X = [normalize_text(x) for x in X]
    y = df.drop("text", 1)  # get rid of text column
    # columns = y.columns  # return all the column labels
    # temp = y.apply(lambda item: item > 0)
    # y = list(temp.apply(lambda item: list(columns[item.values]), axis=1))
    return X, y
