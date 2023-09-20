import numpy as np
from numpy.random import normal, uniform
import matplotlib.pyplot as plt

def make_dataset(n_classes=4, n_classes_samples=100,
                 std=0.5, means=None, shuffle=True):

    if means ==None:
        means = uniform(-5, 5, (n_classes, 2))
        print('means :\n', means)

    X, y = [], []
    for class_idx in range(n_classes):
        mean = means[class_idx]

        X_class = normal(loc=mean, scale=std, size=(n_classes_samples, 2))
        y_class = class_idx * np.ones(n_classes_samples)

        X.append(X_class)
        y.append(y_class)
        print('인덱스에 때른 X 출력\n', X)
        print('인덱스에 때른 y 출력\n', y)

    X, y = np.vstack(X), np.concatenate(y)
    print('vstack X : \n', X)
    print('concatenate y : \n', y)

    if shuffle:
        indices = np.arange(len(y))
        np.random.shuffle(indices)

        X, y = X[indices], y[indices]
        print('X인덱스 셔플링\n', X)
        print('y인덱스 셔플링\n', y)
    return X, y

def vis_dataset(X, y):
    n_classes = len(np.unique(y))

    fig, ax = plt.subplots(figsize=(10, 10))
    for class_idx in range(n_classes):
        X_class = X[y == class_idx]
        ax.scatter(X_class[:, 0], X_class[:, 1],
                   label=f"class {class_idx}",
                   alpha=0.5)

    ax.legend(fontsize=15)
    ax.axhline(y=0, color='gray')
    ax.axvline(x=0, color='gray')

    ax.tick_params(labelsize=15)
    return fig, ax