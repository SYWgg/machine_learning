import pandas as pd

dataset = pd.read_csv('PlayTennis.csv')

tennis = dataset['Play Tennis']
tennis_values = tennis.unique()
print(tennis, '\n')
print(tennis_values)

prior_probs = dict()
n_total_case = tennis.count()

for tennis_value in tennis_values:
    n_case = (tennis == tennis_value).sum()
    prior = n_case / n_total_case
    prior_probs[tennis_value] = prior

print(prior_probs, '\n')

prior_series = pd.Series(prior_probs, name='prior')
print(prior_series)
