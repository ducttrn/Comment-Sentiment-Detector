import sys
import os
import re
import string
import pickle
from os.path import dirname, abspath, join

import pandas as pd

cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))

PATTERN = r"(test_[0-9]{1,6}\n\"(.|\n)*?\")"


def _load_model():
    text_transformer_file = open(join(cwd, "../snapshots", "text_transformer.pkl"), "rb")
    text_transformer = pickle.load(text_transformer_file)

    estimator_file = open(join(cwd, "../snapshots", "model.pkl"), "rb")
    estimator = pickle.load(estimator_file)

    return text_transformer, estimator


def evaluate_file():
    """Evaluate the accuracy of the trained model"""
    text_transformer, estimator = _load_model()

    file = join(os.getcwd(), "../data", "test.crash")
    with open(file, encoding="utf-8") as infile:
        content = infile.read()

    content_list = re.findall(PATTERN, content)
    content_list = [i[0] for i in content_list]

    data = []
    for item in content_list:
        row = {}
        idx = item.split("\n")[0]
        texts = item.split("\n")[1:]
        text = " ".join([i for sublist in texts for i in sublist.split(" ")]).lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

        if len(text) > 2:
            row["id"] = idx
            x_tran = text_transformer.transform([text])
            y = estimator.predict(x_tran)
            row["label"] = str(y[0])
            data.append(row)

        else:
            row["id"] = idx
            row["label"] = "0"
            data.append(row)

    df = pd.DataFrame(data)
    submission_file = join(os.getcwd(), "../data", "corpus", "submission.csv")
    df.to_csv(submission_file, index=False)


def evaluate_text(text: str):
    pass


if __name__ == "__main__":
    evaluate_file()
