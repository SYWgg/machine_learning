from likelihood_util import return_likelihood
import os

import pandas as pd
dataset = pd.read_csv('PlayTennis.csv')

indexes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

for index in indexes:
    likelihood = return_likelihood(index)
    likelihood.to_csv(os.path.join('tennis_data', f'{index}_likelihood.csv'))