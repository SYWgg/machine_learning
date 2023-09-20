import pandas as pd
import os


def return_likelihood(attribute):
    dataset = pd.read_csv(os.path.join('tennis_data', 'PlayTennis.csv'))
    dataset_values = dataset[attribute].unique()  # 인자로 전달 받은 attribute가 가진 값의 종류 가져오기

    yes = dataset[dataset['Play Tennis'] == 'Yes']  # play tennis Yes인 행만 저장
    no = dataset[dataset['Play Tennis'] == 'No']  # play tennis No인 행만 저장

    yes_total = yes[attribute].count()  # yes일 때 전달 받은 attribute 행 개수
    no_total = no[attribute].count()  # no일 때 전달 받은 attribute 행 개수

    yes_likelihood = []
    no_likelihood = []
    likelihood_df = pd.DataFrame(columns=['T', 'not T'],
                                 index=dataset_values)

    for dataset_value in dataset_values:
        yes_case = (yes[attribute] == dataset_value).sum()
        yes_likelihood.append(yes_case / yes_total)

        no_case = (no[attribute] == dataset_value).sum()
        no_likelihood.append(no_case / no_total)

    likelihood_df['T'] = yes_likelihood
    likelihood_df['not T'] = no_likelihood

    return likelihood_df