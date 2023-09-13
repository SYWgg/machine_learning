'''
import pandas as pd

def update_bayesian_table(prior, total_likelihood, data_list, verbose=False):
    bayesian = prior.copy()
    bayesian.rename(columns={'severity': 'prior'},
                    inplace=True)
    for data_lists in data_list:
        if len(bayesian.columns) == 4:
            bayesian['prior'] = bayesian['posterior']
        bayesian['likelihood'] = total_likelihood.loc[data_lists]
        bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
        norm_const = bayesian['joint'].sum()
        bayesian['posterior'] = bayesian['joint'] / norm_const
        if verbose:
            print(f'===== DATA : {data_lists} =====')
            print(bayesian, '\n')
    return bayesian

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

data_list = ['mon', 'morning', 'sedan', 'dry']
bayesian = update_bayesian_table(prior, total_likelihood, data_list)
print('===== FINAL RESULT =====\n', bayesian)
'''
'''
import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

data = ['mon', 'morning', 'sedan']
bayesian = prior.copy()
bayesian.rename(columns={'severity': 'prior'}, inplace=True)

bayesian['likelihood'] = total_likelihood.loc[data[0]]
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const

for single_data in data[1:]:
    bayesian['prior'] = bayesian['posterior']
    bayesian['likelihood'] = total_likelihood.loc[single_data]
    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const

print(bayesian)
'''
import pandas as pd

def update_bayesian_table(prior, total_likelihood, data):
    def from_likelihood_to_posterior(bayesian, total_likelihood, single_data):
        bayesian['likelihood'] = total_likelihood.loc[single_data]
        bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
        norm_const = bayesian['joint'].sum()
        bayesian['posterior'] = bayesian['joint'] / norm_const
        return bayesian

    bayesian = prior.copy()
    bayesian.rename(columns={'severity': 'prior'}, inplace=True)
    bayesian = from_likelihood_to_posterior(bayesian, total_likelihood, data[0])

    for single_data in data[1:]:
        bayesian['prior'] = bayesian['posterior']
        bayesian = from_likelihood_to_posterior(bayesian, total_likelihood, single_data)
    return bayesian

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

data = ['morning', 'sat', 'jeep', 'man', 'st_asc', 'wet']
bayesian = update_bayesian_table(prior, total_likelihood, data)
print(bayesian)