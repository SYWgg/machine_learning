def update_bayesian_table(prior, total_likelihoods, data):
    bayesian = prior.copy()
    bayesian.columns = ['prior']

    bayesian['likelihood'] = total_likelihoods.loc[data]

    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const
    return bayesian