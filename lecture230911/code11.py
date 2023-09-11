from code10 import update_bayesian_table
import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

bayesian = update_bayesian_table(prior, total_likelihood, 'bus')
print(bayesian)