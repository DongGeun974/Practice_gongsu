import pandas as pd
users = pd.read_table('user.txt', sep = '|', index_col = 'user_id')

print(users.head())
print(users.info())

users_age = users[['age','occupation']]
print(users_age.head())
#전체 나이에 대한 이상치 처리 - 정규분포, 95%
#앞의 10개 행
#이상치의 개수
#이상치를 0으로 변경
#이상치를 age의 평균으로 변경
users_age['x-mean'] = abs(users_age['age'] - users_age['age'].mean())
users_age['1.96*std'] = 1.96*users_age['age'].std()
users_age['Outlier'] = users_age['x-mean'] > users_age['1.96*std']

print(users_age.head(10))

mask = users_age['Outlier'] == True
"""
print(len(users_age['Outlier'][mask]))
"""
print(users_age['Outlier'].value_counts())

"""
users_age['age'][mask] = 0
print(users_age['age'][mask])
"""
users_age.loc[users_age['Outlier'] == True, 'age'] = 0
print(users_age[users_age["Outlier"] == True])

users_age['age'][mask] = round(users_age['age'].mean()) #round() 반올림 함수
print(users_age['age'][mask])

#결측치 != 이상치 : 데이터가 없는 거
#nan(not a number)
import numpy as np
#np.nan
users_age.loc[users_age['Outlier'] == True, 'age'] = np.nan

print(users_age[users_age["Outlier"] == True])

print(pd.isnull(users_age))
print(pd.notnull(users_age))

print(pd.isnull(users_age).sum())
print(pd.notnull(users_age).sum())

print(users_age['age'].isnull().sum())
print(users_age['age'].notnull().sum())

#결측치 처리
users_age0 = users_age.fillna(round(users_age['age'].mean())) #결측치만 변경
print(users_age0.head(30))

#직업별 나이에 대한 이상치 처리
#이상치를 결측치로
#결측치를 직업별 평균나이의 반올림값으로 변경
"""
_group = users_age.groupby("occupation")
users_age['oc_x-mean'] = _group['age'].transform(lambda x : x - x.mean)
"""
users_age = users[['occupation', 'age']]
occup_gp = users_age.groupby('occupation')

users_age['x-mean'] = occup_gp.age.transform(lambda x : abs(x - x.mean()))
users_age['1.96*std'] = occup_gp['age'].transform(lambda x : 1.96*x.std())
users_age['outlier'] = users_age['x-mean'] > users_age['1.96*std']

print(users_age['outlier'].value_counts())

users_age.loc[users_age['outlier'] == True, 'age'] = np.nan
"""
users_age['age'][users_age['outlier'] == True] = np.nan
print(users_age.head(30))
"""

users_age['age'] = occup_gp['age'].transform(lambda x : x.fillna(round(x.mean())))
print(users_age.head(30))