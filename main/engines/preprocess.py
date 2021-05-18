import re
import string
from os.path import join

import pandas as pd

PATTERN = r"(train_[0-9]{1,6}\n\"(.|\n)*?\"\n[0|1])"


def preprocess(input_file_path, output_directory):
    """Load a text database into an excel file with 2 columns, text and label for binary classification"""
    # Load the train dataset
    with open(input_file_path, encoding="utf-8") as infile:
        content = infile.read()

    content_list = re.findall(PATTERN, content)
    content_list = [i[0] for i in content_list]
    data = []

    for item in content_list:
        row = {}
        label = int(item.split("\n")[-1])
        text = item.split("\n")[1:-1]
        text = " ".join([i for sublist in text for i in sublist.split(" ")]).lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

        if len(text) > 2:
            row["text"] = text.strip()
            row["label"] = label
            data.append(row)

    df = pd.DataFrame(data)
    preprocessed_data = join(output_directory, "train.csv")
    df.to_csv(preprocessed_data, index=False)
