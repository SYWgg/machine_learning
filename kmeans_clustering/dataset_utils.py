import numpy as np
from numpy.random import uniform, normal

np.random.seed(0)

def make_dataset(n_classes=4, n_class_samples=100,
                 std=0.5, means=None, shuffle=True):
    if means == None:
        means = uniform(-5, 5, (n_classes, 2))

    X = []
    for class_idx in range(n_classes):
        mean = means[class_idx]

        X_class = normal(loc=mean, scale=std,
                         size=(n_class_samples, 2))

        X.append(X_class)

    X = np.vstack(X)
    return X