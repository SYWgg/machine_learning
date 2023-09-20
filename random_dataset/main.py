import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset, vis_dataset

np.random.seed(0)

n_classes = 10

X, y = make_dataset(n_classes=n_classes)
fig, ax = vis_dataset(X, y)
plt.show()