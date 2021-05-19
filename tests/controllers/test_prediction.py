from urllib.parse import urlencode

from main.engines.translate import google_translator


def test_sentiment_prediction(client, mocker):
    mocker.patch.object(google_translator, "translate", return_value="Kém quá")

    data = {"text": "Kém quá"}

    response = client.post(
        "/sentiments/predict",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=urlencode(data),
    )

    assert response.status_code == 200

    data = {}

    response = client.post(
        "/sentiments/predict",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=urlencode(data),
    )

    assert response.status_code == 400
