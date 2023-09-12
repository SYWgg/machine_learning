import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

bayesian = prior.copy()
bayesian.rename(columns={'severity': 'prior'},
                inplace=True)
print(bayesian, '\n')

# 첫 번째 정보를 사용한 경우 (monday)
bayesian['likelihood'] = total_likelihood.loc['mon']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const

print(bayesian, '\n')

# 두 번째 정보를 사용한 경우 (morning)
bayesian['prior'] = bayesian['posterior']
bayesian['likelihood'] = total_likelihood.loc['morning']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const

print(bayesian, '\n')

# 세 번째 정보를 사용한 경우 (bus)
bayesian['prior'] = bayesian['posterior']
bayesian['likelihood'] = total_likelihood.loc['bus']
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const

print(bayesian, '\n')
print(len(bayesian.columns))