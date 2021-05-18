import logging
import pickle
from os.path import dirname, join
from time import time

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def _load_dataset(path: str):
    """Method to load data from an Excel file to DataFrame format"""
    df = pd.read_excel(path)
    texts = list(df["text"])
    labels = df.drop("text", 1)
    return texts, labels


def _save_model(filename, clf):
    """Save the model as a pickle file"""
    pickle.dump(clf, open(filename, "wb"))


def train():
    """Train a model based on training data"""
    train_path = join(dirname(__file__), "../../data", "corpus", "train.xlsx")
    serialization_dir = join(dirname(__file__), "../../models")
    logging.info("Load data...")
    texts, labels = _load_dataset(train_path)

    logging.info("Training model...")
    t0 = time()
    # Go through BOW to find the weight of each word
    transformer = CountVectorizer()
    texts = transformer.fit_transform(texts)

    # Modeling using Logistic Regression -> estimator
    model = LogisticRegression(max_iter=1000)
    estimator = model.fit(texts, labels)
    t1 = time() - t0
    logging.info("Train time: %0.3fs" % t1)

    logging.info("Save model...")
    t0 = time()
    _save_model(serialization_dir + "/text_transformer.pkl", transformer)
    _save_model(serialization_dir + "/model.pkl", estimator)
    t1 = time() - t0
    logging.info("Save model time: %0.3fs" % t1)


if __name__ == "__main__":
    train()
