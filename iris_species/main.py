import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
print(df)

classes = np.unique(df['Species'])
print(classes) # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
n_classes = len(classes) # 3개
df_X = df.iloc[:, 1:5]
print(df_X)
X = df_X.to_numpy() # SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm열을 ndarray로
print(X)
df_y = df.iloc[:, 5]
print(df_y)
y = df_y.to_numpy() # Species열을 ndarray로
print(y)

# 정확도
n_corrects = 0
preds = []
not_correct_index = []
# test_data와 dataset 안에 있는 모든 데이터 사이의 거리
for i in range(len(X)):
    dists = []
    print(X[i])
    for X_ in X:
        dist = np.sqrt(np.sum((X[i] - X_) ** 2))
        print(f"{X_} -> dist: {dist:.4f}")
        dists.append(dist)

    K = 15
    sorted_indices = np.argsort(dists)  # 거리가 가까운 순서대로 그 인덱스를 가져옴
    closest_indices = sorted_indices[:K]  # 거리가 가까운 순서대로 K개의 인덱스
    closest_classes = y[closest_indices]  # y의 해당 인덱스들의 값(클래스)
    print('가장 가까운 거리(dists)의 인덱스 K개 출력 : ', closest_indices)
    print('가장 가까운 K개의 dists를 가진 데이터가 속한 클래스 : ', closest_classes)

    uniques, cnts = np.unique(closest_classes,
                              return_counts=True)  # 거리가 가까운 클래스 종류(uniques)와, 그 횟수(cnts)

    print('closet_classes의 unique한 종류 : ', uniques)
    print('그 unique한 값들의 count 수 :', cnts)
    pred = uniques[np.argmax(cnts)]  # cnts에서 가장 큰 값의 인덱스로 uniques 값에 접근
    preds.append(pred)
    print(f'X의 {i}번째 index인 -> {X[i]}는 {pred}(으)로 분류됩니다.\n')


    #예측 분류 값과 실제 값이 일치할 때마다 n_corrects 증가
    if pred == y[i]:
        n_corrects += 1
    else:
        not_correct_index.append(i)

print('일치하지 않는 인덱스 번호 : ', not_correct_index)
acc = n_corrects / len(X)
print(f"Accuary: {acc:.4f}")