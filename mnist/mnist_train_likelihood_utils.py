import pandas as pd
import os

DATASET_PATH = 'mnist_data'


def return_likelihood(pixel):
    dataset = pd.read_csv(os.path.join(DATASET_PATH, 'mnist_train_binary.csv'), index_col=0)
    dataset_values = [0, 1]

    label0 = dataset[dataset['label'] == 0]
    label1 = dataset[dataset['label'] == 1]
    label2 = dataset[dataset['label'] == 2]
    label3 = dataset[dataset['label'] == 3]
    label4 = dataset[dataset['label'] == 4]
    label5 = dataset[dataset['label'] == 5]
    label6 = dataset[dataset['label'] == 6]
    label7 = dataset[dataset['label'] == 7]
    label8 = dataset[dataset['label'] == 8]
    label9 = dataset[dataset['label'] == 9]

    label0_total = label0[pixel].count()
    label1_total = label1[pixel].count()
    label2_total = label2[pixel].count()
    label3_total = label3[pixel].count()
    label4_total = label4[pixel].count()
    label5_total = label5[pixel].count()
    label6_total = label6[pixel].count()
    label7_total = label7[pixel].count()
    label8_total = label8[pixel].count()
    label9_total = label9[pixel].count()

    label0_likelihood = []
    label1_likelihood = []
    label2_likelihood = []
    label3_likelihood = []
    label4_likelihood = []
    label5_likelihood = []
    label6_likelihood = []
    label7_likelihood = []
    label8_likelihood = []
    label9_likelihood = []

    likelihood_df = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                 index=dataset_values)

    for dataset_value in dataset_values:
        label0_case = (label0[pixel] == dataset_value).sum()
        label0_likelihood.append(label0_case / label0_total)

        label1_case = (label1[pixel] == dataset_value).sum()
        label1_likelihood.append(label1_case / label1_total)

        label2_case = (label2[pixel] == dataset_value).sum()
        label2_likelihood.append(label2_case / label2_total)

        label3_case = (label3[pixel] == dataset_value).sum()
        label3_likelihood.append(label3_case / label3_total)

        label4_case = (label4[pixel] == dataset_value).sum()
        label4_likelihood.append(label4_case / label4_total)

        label5_case = (label5[pixel] == dataset_value).sum()
        label5_likelihood.append(label5_case / label5_total)

        label6_case = (label6[pixel] == dataset_value).sum()
        label6_likelihood.append(label6_case / label6_total)

        label7_case = (label7[pixel] == dataset_value).sum()
        label7_likelihood.append(label7_case / label7_total)

        label8_case = (label8[pixel] == dataset_value).sum()
        label8_likelihood.append(label8_case / label8_total)

        label9_case = (label9[pixel] == dataset_value).sum()
        label9_likelihood.append(label9_case / label9_total)

    likelihood_df[0] = label0_likelihood
    likelihood_df[1] = label1_likelihood
    likelihood_df[2] = label2_likelihood
    likelihood_df[3] = label3_likelihood
    likelihood_df[4] = label4_likelihood
    likelihood_df[5] = label5_likelihood
    likelihood_df[6] = label6_likelihood
    likelihood_df[7] = label7_likelihood
    likelihood_df[8] = label8_likelihood
    likelihood_df[9] = label9_likelihood

    return likelihood_df
