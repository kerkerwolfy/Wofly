# Meet the data
from sklearn.datasets import load_iris

iris_dataset = load_iris()

print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))

print("\nDescription: \n{}".format(iris_dataset['DESCR']))
print("\nTarget: \n{}".format(iris_dataset['target']))
print('\nTarget Names: \n{}'.format(iris_dataset['target_names']))
print('\nFeature Names: \n{}'.format(iris_dataset['feature_names']))
print('\nData: \n{}'.format(iris_dataset['data']))

print('\nShape of Data: {}'.format(iris_dataset['data'].shape))
print('Shape of Target: {}'.format(iris_dataset['target'].shape))

# Measuring Success: Training and testing data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
print('\nShape of X_train: {}'.format(X_train.shape))
print('Shape of y_train: {}'.format(y_train.shape))
print('Shape of X_test: {}'.format(X_test.shape))
print('Shape of y_test: {}'.format(y_test.shape))

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import mglearn

# First things first: Look at your data
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                     marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

plt.show()
