import pandas as pd

severities = ['material damage', 'minor injuries',
              'major injuries', 'fatal']

severity_freq_df = pd.Series(name='severity',
                             index=severities,
                             data=[78, 125, 79, 11])

total_freqs = severity_freq_df.sum()
prior_probs = severity_freq_df / total_freqs


import os
save_file_name = os.path.join('prior_probs.csv')
prior_probs.to_csv(save_file_name)

