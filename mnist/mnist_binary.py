import os
import pandas as pd

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_test.csv'))

labels = dataset['label']
# 앞의 : -> row는 전부
# 뒤의 1: -> 두 번째 column부터 끝까지
images = dataset.iloc[:, 1:].copy()
images[images <= 100] = 0
images[images > 100] = 1

dataset = pd.concat([labels, images], axis=1)
dataset.to_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'))