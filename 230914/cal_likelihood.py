import os
import pandas as pd

DATA_PATH = 'tennis_data'
dataset = pd.read_csv(os.path.join(DATA_PATH, 'PlayTennis.csv'))

tennis = dataset['Play Tennis']
tennis_unique_values = tennis.unique()


def cal_likelihoods(df, target_attribute):
    attribute = df[target_attribute]

    n_total = attribute.count()
    evidences = attribute.unique()
    likelihoods = dict()

    for evidence in evidences:
        n_cases = (attribute == evidence).sum()
        prior = n_cases / n_total
        likelihoods[evidence] = prior

    likelihoods = pd.Series(data=likelihoods)
    return likelihoods


def combine_likelihoods(target_attribute):
    yes = dataset[(tennis == 'Yes')]
    no = dataset[(tennis == 'No')]

    yes_likelihoods = cal_likelihoods(yes, target_attribute)
    no_likelihoods = cal_likelihoods(no, target_attribute)

    likelihoods = pd.concat([yes_likelihoods, no_likelihoods],
                            axis=1)
    likelihoods.columns = ['Yes', 'No']
    return likelihoods


def get_total_likelihoods(dataset):
    total_likelihoods = []
    attributes = dataset.columns[:-1]

    for attribute in attributes:
        likelihoods = combine_likelihoods(attribute)
        total_likelihoods.append(likelihoods)

    total_likelihoods = pd.concat(total_likelihoods,
                                  axis=0)
    return total_likelihoods


total_likelihoods = get_total_likelihoods(dataset).fillna(0)
print(total_likelihoods)
total_likelihoods.to_csv(os.path.join('tennis_data', 'total_likelihoods.csv'))