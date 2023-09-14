from likelihood_utils import return_likelihood
import os
import pandas as pd

DATASET_PATH = 'mnist_data'
dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_binary.csv'), index_col=0)

pixels = []

for i in dataset.columns[2:]:
    pixels.append(i)

likelihoods = []

for pixel in pixels:
    likelihood_df = return_likelihood(pixel)
    likelihoods.append(likelihood_df)

total_likelihood = pd.concat(likelihoods)
total_likelihood.to_csv(os.path.join(DATASET_PATH, 'total_likelihoods.csv'))