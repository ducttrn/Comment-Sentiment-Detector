import pandas as pd

from main.engines import preprocess


def test_preprocess():
    preprocess(
        input_file_path="tests/test_data/data.crash", output_directory="tests/test_data"
    )

    df = pd.read_csv("tests/test_data/train.csv")
    assert {"text", "label"}.issubset(df.columns)
