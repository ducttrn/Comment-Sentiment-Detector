import sys
import os
from os.path import dirname, abspath, join
from time import time
import re
import string
import pandas as pd
import pickle

cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))

PATTERN = r"(test_[0-9]{1,6}\n\"(.|\n)*?\")"

t0 = time()
x_transformer_file = open(join(cwd, "snapshots", "x_transformer.pkl"), "rb")
x_transformer = pickle.load(x_transformer_file)
estimator_file = open(join(cwd, "snapshots", "model.pkl"), "rb")
estimator = pickle.load(estimator_file)
duration = time() - t0
print("Load model time: %0.3fs" % duration)

file = join(os.getcwd(), "data", "test.crash")
with open(file, encoding="utf-8") as infile:
    content = infile.read()
content_list = re.findall(PATTERN, content)
content_list = [i[0] for i in content_list]
data = []
for item in content_list:
    row = {}
    idx = item.split("\n")[0]
    texts = item.split("\n")[1:]
    text = " ".join([i for sublist in texts for i in sublist.split(" ")]).lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    if len(text) > 2:
        row["id"] = idx
        x_tran = x_transformer.transform([text])
        y = estimator.predict(x_tran)
        row["label"] = str(y[0])
        data.append(row)
    else:
        row["id"] = idx
        row["label"] = "0"
        data.append(row)
df = pd.DataFrame(data)
submission_file = join(os.getcwd(), "data", "corpus", "submission.csv")
df.to_csv(submission_file, index=None)
