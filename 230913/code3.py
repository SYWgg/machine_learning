import pandas as pd

dataset = pd.read_csv('PlayTennis.csv')
dataset_ = dataset.head()
print(dataset_)
print(dataset_[[True, False, True, False, True]], '\n')   # boolean indexing. True인 행만 출력한다.

yes = dataset[dataset['Play Tennis'] == 'Yes']  # Yes인 행만 저장
no = dataset[dataset['Play Tennis'] == 'No']    # No인 행만 저장
print(yes)

