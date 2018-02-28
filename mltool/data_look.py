import mglearn
import matplotlib.pyplot as plt

X, y = mglearn.datasets.make_forge()

mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
print("Shape of X: {}".format(X.shape))
print("Shape of y: {}".format(y.shape))
plt.show()

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")
plt.show()

from sklearn.datasets import load_breast_cancer
import numpy as np

cancer_dataset = load_breast_cancer()
print("\nKeys of cancer dataset: {}".format(cancer_dataset.keys()))
print("\nShape of cancer dataset: {}".format(cancer_dataset.data.shape))
print("\nSample counts per class: {}".format(
    {n: v for n, v in zip(cancer_dataset.target_names, np.bincount(cancer_dataset.target))}))
print("\nFeatures of cancer dataset: \n{}".format(cancer_dataset.feature_names))

from sklearn.datasets import load_boston

boston_dataset = load_boston()
print("\nKeys of boston dataset: {}".format(boston_dataset.keys()))
print("\nShape of boston dataset: {}".format(boston_dataset.data.shape))

X, y = mglearn.datasets.load_extended_boston()
print("\nShape of extended boston dataset: {}".format(X.shape))
