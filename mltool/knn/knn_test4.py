"""
Check the relations between model complexity and generalization
"""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def run_knn(neighbors_settings, X_train, y_train, X_test, y_test):

    training_accuracy = []
    test_accuracy = []

    for n_neighbors in neighbors_settings:
        # Build the model
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        # Record training set accuracy
        training_accuracy.append(clf.score(X_train, y_train))
        # Record generalization accuracy
        test_accuracy.append(clf.score(X_test, y_test))
    plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
    plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()
    plt.show()

cancer_dataset = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer_dataset.data, cancer_dataset.target,
                                                    stratify=cancer_dataset.target, random_state=66)

# Try n neighbors from 1 to 10
neighbors_settings = range(1, 11)

run_knn(neighbors_settings, X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test)
