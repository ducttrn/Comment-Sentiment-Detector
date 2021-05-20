import os

from main.engines import evaluate_file, evaluate_text, evaluate_translated_text


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


def test_evaluate_text_with_exception(mocker):
    mocker.patch(
        "main.engines.evaluate.translate_to_training_language", side_effect=Exception
    )

    assert evaluate_translated_text("Tốt quá").sentiment == 0
