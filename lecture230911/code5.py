from code4 import cal_save_likelihoods

days = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']

data = [[11, 15, 10, 1],
        [10, 22, 11, 2],
        [13, 9, 11, 3],
        [18, 20, 7, 2],
        [12, 19, 12, 1],
        [8, 24, 16, 1],
        [6, 16, 12, 1]]

save_name = 'day_likelihoods.csv'
likelihood = cal_save_likelihoods(index=days,
                                   data=data,
                                   save_name=save_name)
print(likelihood)