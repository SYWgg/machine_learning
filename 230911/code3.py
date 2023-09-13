import pandas as pd

severities = ['material damage', 'minor injuries',
              'major injuries', 'fatal']

times = ['morning', 'noon', 'afternoon', 'night']

data = [[17, 20, 13, 3],
        [27, 35, 13, 1],
        [10, 14, 16, 1],
        [24, 56, 37, 6]]

time_freq_df = pd.DataFrame(columns=severities,
                            index=times,
                            data=data)

time_freq_sums = time_freq_df.sum(axis=0)

time_likelihoods = time_freq_df / time_freq_sums

time_likelihoods.to_csv('time_likelihood.csv')