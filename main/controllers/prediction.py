from flask import jsonify

from main import app
from main.schemas.prediction import PredictSentimentSchema, PredictionResultSchema
from main.utils import parse_args_with
from main.engines import evaluate_text


@app.route("/sentiments/predict", methods=["POST"])
@parse_args_with(PredictSentimentSchema())
def predict_sentiment(args):
    text = args["text"]
    prediction = evaluate_text(text)
    return jsonify(PredictionResultSchema().dump(prediction))
