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


def _load_model(model_path=None, transformer_path=None):
    if not model_path:
        model_path = "models/model.pkl"
    if not transformer_path:
        transformer_path = "models/text_transformer.pkl"

    with open(transformer_path, "rb") as text_transformer_file:
        text_transformer = pickle.load(text_transformer_file)

    with open(model_path, "rb") as estimator_file:
        estimator = pickle.load(estimator_file)

    return text_transformer, estimator


def evaluate_file(
    model_path=None, transformer_path=None, test_data_path=None, output_directory=None
):
    """Evaluate the accuracy of the trained model"""
    text_transformer, estimator = _load_model(model_path, transformer_path)

    if not test_data_path:
        test_data_path = "data/test.crash"

    with open(test_data_path, encoding="utf-8") as infile:
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
    if not output_directory:
        output_directory = "data/corpus"
    df.to_csv(output_directory + "/result.csv", index=False)


def evaluate_text(text: str, model_path=None, transformer_path=None) -> Prediction:
    text_transformer, estimator = _load_model(model_path, transformer_path)
    transformed_text = text_transformer.transform([text])

    prediction = estimator.predict_proba(transformed_text)[0]
    predicted_label = 0 if prediction[0] >= prediction[1] else 1
    confidence = round(max(prediction), 4)

    return Prediction(sentiment=predicted_label, confidence=confidence)
