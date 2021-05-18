import os

from main.engines import train


def test_train():
    train(
        training_data_path="tests/test_data/train.csv",
        model_directory="tests/test_data",
    )

    assert all(
        file in os.listdir("tests/test_data")
        for file in ["model.pkl", "text_transformer.pkl"]
    )
