"""
Try and visualize KNN algorithm results with different n neighbors.
"""
import mglearn
import matplotlib.pyplot as plt

mglearn.plots.plot_knn_classification(n_neighbors=1)
plt.show()

mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()

mglearn.plots.plot_knn_classification(n_neighbors=9)
plt.show()