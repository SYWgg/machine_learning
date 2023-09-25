#로딩 너무 오래 걸림....
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = 'data'

train_data = os.path.join(DATA_PATH, 'mnist_train.csv')
test_data = os.path.join(DATA_PATH, 'mnist_test.csv')

train_df = pd.read_csv(train_data)
test_df = pd.read_csv(test_data)

train_y = train_df['label'].to_numpy()
train_X = train_df.iloc[:, 1:].to_numpy()
test_y = test_df['label'].to_numpy()
test_X = test_df.iloc[:, 1:].to_numpy()

n_corrects = 0
for train_X_, train_y_ in zip(train_X, train_y):
    dists = np.sum((train_X - train_X_)**2, axis=1)

    K = 5
    sorted_indices = np.argsort(dists)
    closest_indices = sorted_indices[:K]
    closest_classes = train_y[closest_indices]

    uniques, cnts = np.unique(closest_classes, return_counts=True)
    pred = uniques[np.argmax(cnts)]
    print(pred)
    if pred == train_y_: n_corrects += 1

acc = n_corrects / len(train_y)
print(f"Acc: {acc:.4f}")

