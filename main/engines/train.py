import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def _load_dataset(path: str):
    """Method to load data from an Excel file to DataFrame format"""
    df = pd.read_csv(path)
    texts = list(df["text"])
    labels = df.drop("text", 1)
    return texts, labels


def _save_model(filepath, clf):
    """Save the model as a pickle file"""
    pickle.dump(clf, open(filepath, "wb"))


def train(training_data_path, model_directory):
    """Train a model based on training data"""
    texts, labels = _load_dataset(training_data_path)

    # Go through BOW to find the weight of each word
    transformer = CountVectorizer()
    texts = transformer.fit_transform(texts)

    # Modeling using Logistic Regression to get the estimator
    model = LogisticRegression(max_iter=1000)
    estimator = model.fit(texts, labels)

    _save_model(model_directory + "/text_transformer.pkl", transformer)
    _save_model(model_directory + "/model.pkl", estimator)
