import pandas as pd
import os

dataset = pd.read_csv('PlayTennis.csv')
tennis = dataset['Play Tennis'] == 'Yes'

n_total_cases = tennis.count()  # 14
n_play = tennis.sum()   # 9
n_no_play = n_total_cases - n_play  # 5

prior_probs = [n_play / n_total_cases,
               n_no_play / n_total_cases]

prior = pd.Series(index=['T', 'not T'],
                  name='prior',
                  data=prior_probs)

os.makedirs('tennis_data', exist_ok=True)
prior.to_csv(os.path.join('tennis_data', 'prior.csv'))
print(dataset)