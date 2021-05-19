from flask import jsonify

from main.app import app
from main.engines import evaluate_translated_text
from main.schemas.prediction import PredictionResultSchema, PredictSentimentSchema
from main.utils import parse_args_with


@app.route("/api/v1/sentiments/predict", methods=["POST"])
@parse_args_with(PredictSentimentSchema())
def predict_sentiment_api(args):
    text = args["text"]
    prediction = evaluate_translated_text(text)

    return jsonify(PredictionResultSchema().dump(prediction))
