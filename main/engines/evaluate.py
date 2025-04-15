import json
import logging
import re
import string
import sys
from os.path import abspath, dirname

import pandas as pd

from main.configs import config
from main.engines.translate import translate_to_training_language
from main.libs.memcache import memcache_client
import fickling

cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))

PATTERN = r"(test_[0-9]{1,6}\n\"(.|\n)*?\")"


class Prediction:
    def __init__(self, sentiment, confidence):
        self.sentiment = sentiment
        self.confidence = confidence


def _load_model(model_path: str = None, transformer_path: str = None):
    if not model_path:
        model_path = "models/model.pkl"
    if not transformer_path:
        transformer_path = "models/text_transformer.pkl"

    with open(transformer_path, "rb") as text_transformer_file:
        text_transformer = fickling.load(text_transformer_file)

    with open(model_path, "rb") as estimator_file:
        estimator = fickling.load(estimator_file)

    return text_transformer, estimator


def evaluate_file(
    test_data_path: str,
    output_directory: str,
    model_path: str = None,
    transformer_path: str = None,
) -> None:
    """
    Evaluate the sentiments of texts in a file
    """
    text_transformer, estimator = _load_model(model_path, transformer_path)
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
    df.to_csv(output_directory + "/result.csv", index=False)


def evaluate_text(
    text: str, model_path: str = None, transformer_path: str = None
) -> Prediction:
    """
    Evaluate the sentiment of a text
    """
    cached_value = memcache_client.get(text)
    if cached_value:
        return Prediction(**json.loads(cached_value))

    text_transformer, estimator = _load_model(model_path, transformer_path)
    transformed_text = text_transformer.transform([text])

    prediction = estimator.predict_proba(transformed_text)[0]
    predicted_label = 0 if prediction[0] >= prediction[1] else 1
    confidence = round(max(prediction), 4)

    memcache_client.set(
        key=text,
        value=json.dumps({"sentiment": predicted_label, "confidence": confidence}),
        time=config.CACHE_TIME_OUT,
    )

    return Prediction(sentiment=predicted_label, confidence=confidence)


def evaluate_translated_text(text: str) -> Prediction:
    """
    Translate and evaluate the sentiment of a text
    """
    try:
        translated_text = translate_to_training_language(text)
    except Exception as e:
        logging.exception(e)
        translated_text = text

    prediction = evaluate_text(translated_text)

    return prediction
