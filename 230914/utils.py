import itertools

def get_all_evidences():
    Outlook = ['Sunny', 'Overcast', 'Rain']
    Temperature = ['Hot', 'Mild', 'Cool']
    Humidity = ['High', 'Normal']
    Wind = ['Weak', 'Strong']

    evidences = list(itertools.product(Outlook, Temperature, Humidity, Wind))
    return evidences


def update_bayesian_table(prior, total_likelihood, data, verbose=False):
    def from_likelihood_to_posterior(bayesian, total_likelihood, single_data):
        bayesian['likelihood'] = total_likelihood.loc[single_data]
        bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
        norm_const = bayesian['joint'].sum()
        bayesian['posterior'] = bayesian['joint'] / norm_const
        return bayesian

    bayesian = prior.copy()
    bayesian = from_likelihood_to_posterior(bayesian, total_likelihood, data[0])
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