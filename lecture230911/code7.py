import pandas as pd

file_names = ['time_likelihood.csv', 'day_likelihoods.csv', 'vehicle_likelihoods.csv',
              'sex_likelihoods.csv', 'road_likelihoods.csv', 'surface_likelihoods.csv']

likelihoods = []

for file_name in file_names:
    df = pd.read_csv(file_name, index_col=0)
    likelihoods.append(df)

total_likelihood = pd.concat(likelihoods)
total_likelihood.to_csv('total_likelihoods.csv')
print(total_likelihood)