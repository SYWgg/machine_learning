import numpy as np
import matplotlib.pyplot as plt

from dataset_utils import make_dataset, vis_dataset

np.random.seed(0)

n_classes = 3

X, y = make_dataset(n_classes=n_classes)

# test_data를 좌표(-2, -0.5)에 생성
test_data = np.array([0.2, 1.2])

# test_data와 dataset 안에 있는 모든 데이터 사이의 거리
dists = []
for X_ in X:
    dist = np.sqrt(np.sum((test_data - X_) ** 2))
    print(f"{X_} -> dist: {dist:.4f}")
    dists.append(dist)

K = 5
sorted_indices = np.argsort(dists)  # 거리가 가까운 순서대로 그 인덱스를 가져옴
closest_indices = sorted_indices[:K]  # 거리가 가까운 순서대로 K개의 인덱스
closest_classes = y[closest_indices]  # y의 해당 인덱스들의 값(클래스)
print('가장 가까운 거리(dists)의 인덱스 K개 출력 : ', closest_indices)
print('가장 가까운 5개의 dists를 가진 데이터가 속한 클래스 : ', closest_classes)

uniques, cnts = np.unique(closest_classes,
                          return_counts=True)  # 거리가 가까운 클래스 종류(uniques)와, 그 횟수(cnts)

print('closet_classes의 unique한 종류 : ', uniques)
print('그 unique한 값들의 count 수 : ', cnts)
pred = uniques[np.argmax(cnts)]  # cnts에서 가장 큰 값의 인덱스로 uniques 값에 접근
print(f'test data -> {test_data}는 class{int(pred)}(으)로 분류됩니다.')

# 결과 시각화
closest_X = X[closest_indices]

# dataset
fig, ax = vis_dataset(X, y)

# test data의 외곽선을 분류된 class의 색으로 표현
ax.scatter(test_data[0], test_data[1], color='red', s=300,
           edgecolor=f'C{int(pred)}', linewidths=4)

# test data와 가장 가까운 data를 점선으로 연결
for closest_X_, closest_class in zip(closest_X, closest_classes):
    ax.plot([closest_X_[0], test_data[0]],  # x 좌표들
            [closest_X_[1], test_data[1]],  # y 좌표들
            color=f'C{int(closest_class)}',  # 색깔은 class를 보고 결정
            ls=':')  # 점선으로 그리기
plt.show()
