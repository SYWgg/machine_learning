import pandas as pd

def return_likelihood(index):
    dataset = pd.read_csv('PlayTennis.csv')
    dataset_values = dataset[index].unique()

    yes = dataset[dataset['Play Tennis'] == 'Yes']  # play tennis Yes인 행만 저장
    no = dataset[dataset['Play Tennis'] == 'No']  # play tennis No인 행만 저장

    yes_total = yes[index].count()
    no_total = no[index].count()

    yes_likelihood = []
    no_likelihood = []
    likelihood_df = pd.DataFrame(columns=['T', 'not T'],
                                 index=dataset_values)

    for dataset_value in dataset_values:
        yes_case = (yes[index] == dataset_value).sum()
        yes_likelihood.append(yes_case / yes_total)
        no_case = (no[index] == dataset_value).sum()
        no_likelihood.append(no_case / no_total)

    likelihood_df['T'] = yes_likelihood
    likelihood_df['not T'] = no_likelihood

    return likelihood_df