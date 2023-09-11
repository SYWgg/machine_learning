import pandas as pd

# 상품에 대해 물어볼 때 상품을 구매할 확률
# bayesian table (T)
print('bayesian table (T)')

# empty dataframe
bayesian = pd.DataFrame(index=['B', 'not B'])
print(bayesian)

# prior probability 넣기
bayesian['prior'] = [0.1, 0.9]
print(bayesian)

# likelihood 넣기
bayesian['likelihood'] = [0.9, 0.3]
print(bayesian)

# joint probability 계산해서 넣기
bayesian['joint'] = bayesian['prior'] * bayesian['likelihood']
print(bayesian)

# posterior 계산해서 넣기
norm_const = bayesian['joint'].sum()
bayesian['posterior'] = bayesian['joint'] / norm_const
print(bayesian, '\n')

print('--------------------------------------------------\n')
# bayesian table (not T)
print('bayesian table (not T)')

# empty dataframe
bayesian2 = pd.DataFrame(index=['B', 'not B'])
print(bayesian2)

# prior
bayesian2['prior'] = [0.1, 0.9]
print(bayesian2)

# likelihood
bayesian2['likelihood'] = [0.1, 0.7]
print(bayesian2)

# joint
bayesian2['joint'] = bayesian2['prior'] * bayesian2['likelihood']
print(bayesian2)

# posterior
norm_const2 = bayesian2['joint'].sum()
bayesian2['posterior'] = bayesian2['joint'] / norm_const2
print(bayesian2, '\n')

# 쇼핑백을 들고 있을 때 상품을 구매할 확률
# bayesian table (S)

# empty dataframe
bayesian_S = pd.DataFrame(index=['B', 'not B'])

# prior probability 넣기
bayesian_S['prior'] = [0.1, 0.9]

# likelihood 넣기
bayesian_S['likelihood'] = [0.7, 0.4]

# joint probability 계산해서 넣기
bayesian_S['joint'] = bayesian_S['prior'] * bayesian_S['likelihood']

# posterior 계산해서 넣기
norm_const_S = bayesian_S['joint'].sum()
bayesian_S['posterior'] = bayesian_S['joint'] / norm_const_S

# bayesian table (not S)

# empty dataframe
bayesian_notS = pd.DataFrame(index=['B', 'not B'])

# prior probability 넣기
bayesian_notS['prior'] = [0.1, 0.9]

# likelihood 넣기
bayesian_notS['likelihood'] = [0.3, 0.6]

# joint probability 계산해서 넣기
bayesian_notS['joint'] = bayesian_notS['prior'] * bayesian_notS['likelihood']

# posterior 계산해서 넣기
norm_const_notS = bayesian_notS['joint'].sum()
bayesian_notS['posterior'] = bayesian_notS['joint'] / norm_const_notS

print('bayesian table (S)')
print(bayesian_S, '\n')

print('bayesian table (not S)')
print(bayesian_notS, '\n')