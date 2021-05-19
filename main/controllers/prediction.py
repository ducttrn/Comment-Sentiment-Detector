from flask import render_template

from main.app import app
from main.engines import evaluate_translated_text
from main.schemas.prediction import PredictSentimentSchema
from main.utils import parse_form_with


@app.route("/sentiments/predict", methods=["POST"])
@parse_form_with(PredictSentimentSchema())
def predict_sentiment(args):
    text = args["text"]
    prediction = evaluate_translated_text(text)

    return render_template(
        "index.html",
        sentiment="Negative" if prediction.sentiment else "Positive",
        confidence=f"{round(prediction.confidence * 100, 2)}%",
    )
