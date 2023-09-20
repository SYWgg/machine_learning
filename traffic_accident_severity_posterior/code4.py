import pandas as pd
import os

from utils import get_all_evidences
from utils import update_bayesian_table

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

hypotheses = ['material damage', 'minor injuries', 'major injuries', 'fatal']
data_types = ['Time', 'Day', 'Vehicle', 'Sex', 'Road', 'Surface']

columns = data_types + hypotheses
total_posterior = pd.DataFrame(columns=columns)
evidences = get_all_evidences()

for row_idx, evidence in enumerate(evidences):
    bayesian = update_bayesian_table(prior, total_likelihood, evidence)
    posterior = bayesian['posterior'].tolist()

    row_data = list(evidence) + posterior  # evidence의 각 요소는 튜플 -> list()처리
    total_posterior.loc[row_idx] = row_data

total_posterior.to_csv(os.path.join('data', 'total_posterior.csv'))
print(total_posterior)