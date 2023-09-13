import pandas as pd

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

print(prior, '\n')
print(total_likelihood, '\n')

bayesian = prior.copy()
bayesian.rename(columns={'severity': 'prior'},
                inplace=True)
print(bayesian, '\n')

# 이 [현상]일 때, 사고가 일어날 확률을 구할 수 있다 (여기서는 [bus]일 때)
bayesian['likelihood'] = total_likelihood.loc['bus']
print(bayesian, '\n')

bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')