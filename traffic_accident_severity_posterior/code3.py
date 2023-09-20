import pandas as pd
import itertools
import os

hypotheses = ['material damage', 'minor injuries', 'major injuries', 'fatal']
data_types = ['Time', 'Day', 'Vehicle', 'Sex', 'Road', 'Surface']
columns = data_types + hypotheses

times = ['morning', 'noon', 'afternoon', 'night']
days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
vehicles = ['sedan', 'jeep', 'pickup', 'minibus', 'bus', 'truck']
sexes = ['man', 'woman']
roads = ['st_flat', 'st_des', 'st_asc', 'cuv_flat', 'cuv_des', 'cuv_asc']
surfaces = ['dry', 'wet', 'sandy']

prior = pd.read_csv('prior_probs.csv', index_col=0)
total_likelihood = pd.read_csv('total_likelihoods.csv', index_col=0)

total_posterior = []

evidences = list(itertools.product(times, days, vehicles, sexes, roads, surfaces))

for evidence in evidences:
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

    bayesian = update_bayesian_table(prior, total_likelihood, evidence)

    bayesian_posterior = bayesian['posterior'].tolist()
    total_posterior.append(list(evidence) + bayesian_posterior)

total_posterior_df = pd.DataFrame(data=total_posterior,
                                  columns=columns)
print(total_posterior_df)
total_posterior_df.to_csv(os.path.join('data', 'total_posterior_1.csv'))