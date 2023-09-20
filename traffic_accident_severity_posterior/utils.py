import itertools


def get_all_evidences():
    times = ['morning', 'noon', 'afternoon', 'night']
    days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
    vehicles = ['sedan', 'jeep', 'pickup', 'minibus', 'bus', 'truck']
    sexes = ['man', 'woman']
    roads = ['st_flat', 'st_des', 'st_asc', 'cuv_flat', 'cuv_des', 'cuv_asc']
    surfaces = ['dry', 'wet', 'sandy']

    evidences = list(itertools.product(times, days, vehicles,
                                       sexes, roads, surfaces))
    return evidences


def from_likelihood_to_posterior(bayesian, total_likelihood, single_data):
    bayesian['likelihood'] = total_likelihood.loc[single_data]
    bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
    norm_const = bayesian['joint'].sum()
    bayesian['posterior'] = bayesian['joint'] / norm_const
    return bayesian


def update_bayesian_table(prior, total_likelihood, data, verbose=False):
    bayesian = prior.copy()
    bayesian.rename(columns={'severity': 'prior'}, inplace=True)
    bayesian = from_likelihood_to_posterior(bayesian, total_likelihood,
                                            data[0])
    if verbose:
        print(f"===== Data: {data[0]} =====")
        print(bayesian, '\n')

    for single_data in data[1:]:
        bayesian['prior'] = bayesian['posterior']
        bayesian = from_likelihood_to_posterior(bayesian, total_likelihood,
                                                single_data)
        if verbose:
            print(f"===== Data: {single_data} =====")
            print(bayesian, '\n')
    return bayesian