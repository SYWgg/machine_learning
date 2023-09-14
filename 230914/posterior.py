import os
import pandas as pd

from utils import get_all_evidences
from utils import update_bayesian_table

DATA_PATH = 'tennis_data'

prior = pd.read_csv(os.path.join(DATA_PATH, 'prior.csv'), index_col=0)
total_likelihood = pd.read_csv(os.path.join(DATA_PATH, 'total_likelihoods.csv'),
                               index_col=0)

hypotheses = ['No', 'Yes']
data_types = ['Outlook', 'Temperature', 'Humidity', 'Wind']

evidences = get_all_evidences()
columns = data_types + hypotheses
total_posterior = pd.DataFrame(columns=columns)

for row_idx, evidence in enumerate(evidences):
    bayesian = update_bayesian_table(prior, total_likelihood, evidence)
    posterior = bayesian['posterior'].tolist()

    row_data = list(evidence) + posterior
    total_posterior.loc[row_idx] = row_data

total_posterior.to_csv(os.path.join(DATA_PATH, 'total_posterior.csv'))
print(total_posterior)