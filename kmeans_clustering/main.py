import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset

K = 4
X = make_dataset(std=0.3)
n_samples = X.shape[0]

random_indices = np.arange(400)
np.random.shuffle(random_indices)
random_indices = random_indices[:K]
centroids = X[random_indices] # 실제 존재하는 데이터에서 K개를 centroid로 설정

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
ax.scatter(centroids[:, 0], centroids[:, 1],
           color='red', marker='X', s=100)
plt.show()