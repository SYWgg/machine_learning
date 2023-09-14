import os
import pandas as pd

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_test.csv'), index_col=0)

labels = dataset['label']
images = dataset.iloc[:, 1:].copy()
images[images <= 100] = 0
images[images > 100] = 1

dataset = pd.concat([labels, images], axis=1)
dataset.to_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'))