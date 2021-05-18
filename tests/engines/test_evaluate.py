import os

from main.engines import evaluate_text, evaluate_file


def test_evaluate_text():
    prediction = evaluate_text("Tốt lắm")
    assert prediction.sentiment == 0


def test_evaluate_file():
    evaluate_file(output_directory="tests/test_data")

    assert "result.csv" in os.listdir("tests/test_data")
