import os

from main.engines import evaluate_text, evaluate_file


def test_evaluate_text():
    text = "Tốt lắm"
    prediction = evaluate_text(text)
    assert prediction.sentiment == 0

    # With cache
    prediction = evaluate_text(text)
    assert prediction.sentiment == 0


def test_evaluate_file():
    evaluate_file(test_data_path="data/test.crash", output_directory="tests/test_data")

    assert "result.csv" in os.listdir("tests/test_data")
