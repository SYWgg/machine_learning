import pandas as pd

def update_bayesian_table(prior, total_likelihoods, data):
    bayesian = prior.copy()
    print(bayesian)
    bayesian['likelihood'] = total_likelihoods.loc[data]
    print(bayesian)
    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const
    return bayesian


prior = pd.read_csv('tennis_data/prior.csv', index_col=0)
total_likelihood = pd.read_csv('tennis_data/total_likelihoods.csv', index_col=0)

bayesian = update_bayesian_table(prior, total_likelihood, 'Sunny')

print(bayesian)