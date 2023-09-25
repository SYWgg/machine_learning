import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset

K = 4
X = make_dataset(std=0.3)
n_samples = X.shape[0]

random_indices = np.arange(400)
np.random.shuffle(random_indices)
random_indices = random_indices[:K]
centroids = X[random_indices]  # 실제 존재하는 데이터에서 K개를 centroid로 설정

X_ = X.reshape(n_samples, 1, 2)  # (400, 1, 2)
for step in range(5):
    centroids_ = centroids.reshape(1, K, 2)  # (1, 4, 2)

    dists = np.sum((X_ - centroids_) ** 2, axis=2)  # (400 -> sample, 4 -> cluster)
    clustering_indices = np.argmin(dists, axis=1)  # 가까운 cluster의 인덱스

    clustering_dict = {} # key: cluster의 index / value: 해당 cluster와 가장 가까운 점들 → 행렬
    for k in range(K):
        cluster_X = X[clustering_indices == k]
        clustering_dict[k] = cluster_X

    centroids = []
    for k in range(K):
        centroid = np.mean(clustering_dict[k], axis=0)
        centroids.append(centroid)
    centroids = np.concatenate(centroids).reshape(K, 2)

# fig, ax = plt.subplots(figsize=(10, 10))
# ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
# ax.scatter(centroids[:, 0], centroids[:, 1],
#            color='red', marker='X', s=100)
# plt.show()