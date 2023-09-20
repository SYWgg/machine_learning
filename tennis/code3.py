'''boolean indexing으로 play tennis 행을 값에 따라 분류'''
import pandas as pd
import os

dataset = pd.read_csv(os.path.join('tennis_data', 'PlayTennis.csv'))
dataset_ = dataset.head()
print(dataset_)
print(dataset_[[True, False, True, False, True]], '\n')   # boolean indexing. True인 행만 출력한다.

yes = dataset[dataset['Play Tennis'] == 'Yes']  # Yes인 행만 저장
no = dataset[dataset['Play Tennis'] == 'No']    # No인 행만 저장
print(yes)
print(no)

