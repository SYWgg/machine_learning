import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm

DATA_PATH = 'data'
TRAIN_DATA_FILE_NAME = 'mnist_train.csv'
TEST_DATA_FILE_NAME = 'mnist_test.csv'

train_data_file = os.path.join(DATA_PATH, TRAIN_DATA_FILE_NAME)
test_data_file = os.path.join(DATA_PATH, TEST_DATA_FILE_NAME)
print(f"File existence test -> {os.path.exists(train_data_file)} / "
      f"{os.path.exists(test_data_file)}")

train_dataset_df = pd.read_csv(train_data_file, index_col=0)
train_y = train_dataset_df.index.to_numpy()
train_X = train_dataset_df.to_numpy()
print(train_y.shape)
print(train_X.shape)
test_dataset_df = pd.read_csv(test_data_file, index_col=0)
test_y = test_dataset_df.index.to_numpy()
test_X = test_dataset_df.to_numpy()
print(test_y.shape)
print(test_y.shape)


K = 10

n_corrects = 0
for idx in tqdm(range(len(train_y))):
  X_, y_ = train_X[idx], train_y[idx]
  dists = np.sum((train_X - X_)**2, axis=1)

  sorted_indices = np.argsort(dists)
  closest_indices = sorted_indices[:K]
  closest_classes = train_y[closest_indices]

  uniques, cnts = np.unique(closest_classes, return_counts=True)
  pred = uniques[np.argmax(cnts)]

  if pred == y_: n_corrects += 1

acc = n_corrects / len(train_y)
print(f"Train Acc: {acc:.4f}")