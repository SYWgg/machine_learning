import numpy as np
from numpy.random import normal
from numpy.random import uniform

import matplotlib.pyplot as plt
# 좌표를 가지고 있는 X, 레이블을 가지고 있는 y

def make_dataset(n_classes=4, n_class_samples=100,
                 std=0.5, means=None, shuffle=True):
    if means == None:
        means = uniform(-5, 5, (n_classes, 2))

    X, y = [], []
    for class_idx in range(n_classes):
        mean = means[class_idx]

        X_class = normal(loc=mean, scale=std,
                         size=(n_class_samples, 2))
        y_class = class_idx * np.ones(n_class_samples)

        X.append(X_class)
        y.append(y_class)

    X, y = np.vstack(X), np.concatenate(y)

    # 0~n까지의 index를 먼저 만들고, 이 index를 섞어준다.
    # 랜덤하게 섞인 index로 X, y를 인덱싱해주면 pair는 깨지지 않는다.
    if shuffle:
        indices = np.arange(len(y))
        np.random.shuffle(indices)
        print(np.arange(len(y)))
        X, y = X[indices], y[indices]
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