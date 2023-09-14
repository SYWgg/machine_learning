import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_INDEX = 0

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'),
                      index_col=0)

sample = dataset.iloc[SAMPLE_INDEX]
label = sample['label']
print(sample)
# Series를 (28, 28)의 행렬로 바꾸는 연산
img = np.array(sample.drop('label')).reshape(28, 28)

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img, cmap='gray')
ax.set_title(f"Class {label}", fontsize=30)
ax.axis('off')
plt.show()