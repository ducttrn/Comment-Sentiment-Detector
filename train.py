import pickle
from os.path import dirname, join
from time import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from load_data import load_dataset


def save_model(filename, clf):
    """Train and save the model using training data"""
    pickle.dump(clf, open(filename, "wb"))


train_path = join(dirname(__file__), "data", "corpus", "train.xlsx")
serialization_dir = join(dirname(__file__), "snapshots")
print("Load data...")
X_train, y_train = load_dataset(train_path)

print("\nTraining model...")
t0 = time()
# Go through BOW to find the weight of each word
transformer = CountVectorizer()
X_train = transformer.fit_transform(X_train)

# Modeling using Logistic Regression -> estimator
model = LogisticRegression(max_iter=1000)
estimator = model.fit(X_train, y_train)
t1 = time() - t0
print("Train time: %0.3fs" % t1)

print("\nSave model...")
t0 = time()
save_model(serialization_dir + "/x_transformer.pkl", transformer)
save_model(serialization_dir + "/model.pkl", estimator)
t1 = time() - t0
print("Save model time: %0.3fs" % t1)
