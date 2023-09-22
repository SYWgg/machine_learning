'''prior probability 구하기 필요없음'''
import pandas as pd
import os

DATASET_PATH = 'mnist_data'

dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_train_binary.csv'), index_col=0)

label0 = dataset['label'] == 0
label1 = dataset['label'] == 1
label2 = dataset['label'] == 2
label3 = dataset['label'] == 3
label4 = dataset['label'] == 4
label5 = dataset['label'] == 5
label6 = dataset['label'] == 6
label7 = dataset['label'] == 7
label8 = dataset['label'] == 8
label9 = dataset['label'] == 9

total_label_count = label0.count()

n_label0 = label0.sum()
n_label1 = label1.sum()
n_label2 = label2.sum()
n_label3 = label3.sum()
n_label4 = label4.sum()
n_label5 = label5.sum()
n_label6 = label6.sum()
n_label7 = label7.sum()
n_label8 = label8.sum()
n_label9 = label9.sum()

prior_probs = [n_label0 / total_label_count, n_label1 / total_label_count,
               n_label2 / total_label_count, n_label3 / total_label_count,
               n_label4 / total_label_count, n_label5 / total_label_count,
               n_label6 / total_label_count, n_label7 / total_label_count,
               n_label8 / total_label_count, n_label9 / total_label_count]

prior = pd.Series(index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  name='prior',
                  data=prior_probs)

prior.to_csv(os.path.join(DATASET_PATH, 'mnist_train_prior.csv'))