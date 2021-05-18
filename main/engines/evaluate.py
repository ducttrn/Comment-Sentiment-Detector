import os
import pickle
import re
import string
import sys
from os.path import dirname, abspath, join

import pandas as pd

cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))

PATTERN = r"(test_[0-9]{1,6}\n\"(.|\n)*?\")"


class Prediction:
    def __init__(self, sentiment, confidence):
        self.sentiment = sentiment
        self.confidence = confidence


def _load_model():
    text_transformer_file = open(
        join(cwd, "../../models", "text_transformer.pkl"), "rb"
    )
    text_transformer = pickle.load(text_transformer_file)

    estimator_file = open(join(cwd, "../../models", "model.pkl"), "rb")
    estimator = pickle.load(estimator_file)

    return text_transformer, estimator


def evaluate_file():
    """Evaluate the accuracy of the trained model"""
    text_transformer, estimator = _load_model()

    file = join(os.getcwd(), "../../data", "test.crash")
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
            transformed_text = text_transformer.transform([text])
            predicted_label = estimator.predict(transformed_text)
            row["label"] = str(predicted_label[0])
            data.append(row)

        else:
            row["id"] = idx
            row["label"] = "0"
            data.append(row)

    df = pd.DataFrame(data)
    result_file = join(os.getcwd(), "../../data", "corpus", "result.csv")
    df.to_csv(result_file, index=False)


def evaluate_text(text: str) -> Prediction:
    text_transformer, estimator = _load_model()
    transformed_text = text_transformer.transform([text])

    prediction = estimator.predict_proba(transformed_text)[0]
    predicted_label = 0 if prediction[0] >= prediction[1] else 1
    confidence = max(prediction)

    return Prediction(sentiment=predicted_label, confidence=confidence)


if __name__ == "__main__":
    evaluate_file()
    evaluate_text("Kém quá")
