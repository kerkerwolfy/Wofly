import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

from scipy import sparse
eye = np.eye(4)
print("\neye:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("\nsparse CSR matrix:\n{}". format(sparse_matrix))

y = np.array([[2, 0, 0], [0, 3, 0], [0, 1, 4]])
sparse_matrix2 = sparse.csr_matrix(y)
print("\nsparse CSR matrix:\n{}". format(sparse_matrix2))

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = np.sin(x)

plt.plot(x, y, marker="x")
plt.show()

from IPython.display import display
import pandas as pd

data = {'Name': ["John", "Anna", "Peter", "Linda"],
        "Location": ["New York", "Paris", "Berlin", "London"],
        "Age": [24, 13, 53, 33]
        }

data_pandas = pd.DataFrame(data)

display("\n{}".format(data_pandas))

display("\n{}".format(data_pandas[data_pandas.Age > 30]))
