import json


def test_sentiment_prediction(client):
    data = {"text": "Kém quá"}

    response = client.post(
        "/sentiments/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
    )

    assert response.status_code == 200
    assert response.json["sentiment"] == 1

    data = {}

    response = client.post(
        "/sentiments/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
    )

    assert response.status_code == 400
