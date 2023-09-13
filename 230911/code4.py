import pandas as pd


def cal_save_likelihoods(index, data, save_name):
    '''
    (1) index, data를 입력받아 freq dataframe을 만들기
    (2) likelihood 계산
    (3) likelihood 저장하고, return 해주기
    '''
    severities = ['material damage', 'minor injuries',
                  'major injuries', 'fatal']

    freq_df = pd.DataFrame(columns=severities,
                           index=index, data=data)
    freq_sums = freq_df.sum(axis=0)
    likelihoods = freq_df / freq_sums

    likelihoods.to_csv(save_name)
    return likelihoods
