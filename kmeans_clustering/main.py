import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset

K = 4
X = make_dataset(std=0.3)

centroids = np.random.uniform(-3, 3, (K, 2))

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(X[:, 0], X[:, 1])
ax.scatter(centroids[:, 0], centroids[:, 1],
           color='red', marker='X', s=100)

ax.tick_params(labelsize=15)
plt.show()