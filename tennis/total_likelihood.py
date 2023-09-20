import pandas as pd
import os

file_names = ['Outlook_likelihood.csv', 'Temperature_likelihood.csv',
              'Humidity_likelihood.csv', 'Wind_likelihood.csv']
likelihoods = []

for file_name in file_names:
    df = pd.read_csv(os.path.join('tennis_data', file_name), index_col=0)
    likelihoods.append(df)

total_likelihood = pd.concat(likelihoods)
total_likelihood.to_csv(os.path.join('tennis_data', 'total_likelihoods.csv'))
print(total_likelihood)