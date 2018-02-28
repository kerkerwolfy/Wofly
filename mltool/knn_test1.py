from sklearn.datasets import load_iris
import numpy as np

iris_dataset = load_iris()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

from sklearn.neighbors import KNeighborsClassifier

# Building your first model: k nearest neighbors
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

print("\n")
print(knn)

# Make Predictions
X_new = np.array([[5, 2.9, 1, 0.2]])
print("\nShape of X_new: {}".format(X_new.shape))

# Evaluating the model
prediction = knn.predict(X_new)
print("\nPrediction: {}".format(prediction))
print("\nTarget Names: {}".format(iris_dataset["target_names"]))
print("\nPredicted Target Name: {}".format(iris_dataset["target_names"][prediction]))

test_set_prediction = knn.predict(X_test)
print("\nTest set predictions:\n {}".format(test_set_prediction))

print("\nTest set score: {:.2f}".format(np.mean(test_set_prediction == y_test)))

print("\nTest set score: {:.2f}".format(knn.score(X_test, y_test)))
