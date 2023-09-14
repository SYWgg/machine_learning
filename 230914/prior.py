import os
import pandas as pd

DATA_PATH = 'tennis_data'
dataset = pd.read_csv(os.path.join(DATA_PATH, 'PlayTennis.csv'))

tennis = dataset['Play Tennis']
tennis_unique_values = tennis.unique()

prior_probs = dict()
n_total = tennis.count()

for unique_value in tennis_unique_values:
    hypo = (tennis == unique_value)
    n_hypo = hypo.sum()

    hypo_prior = n_hypo / n_total
    prior_probs[unique_value] = hypo_prior

prior_series = pd.Series(name='prior',
                         data=prior_probs)
prior_series.to_csv(os.path.join(DATA_PATH, 'prior.csv'))
print(prior_series)