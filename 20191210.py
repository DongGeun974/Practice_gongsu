import pandas as pd

users = pd.read_table('user.txt', sep='|', index_col='user_id')

"""
1 처음부터 25개의 행 확인 head(25)
2 끝에서 10개의 행 확인 tail(10)
3 데이터의 관측치 몇개 shape[0]
4 열의 개수 len(users.columns)
5 열의 이름 users.columns
6 인덱스는 어떻게 되어있는가 users.index
7 각 열의 데이터타입은 어떻게 되어있는가 users.dtypes
8 occupation열만 출력 users['occupation']
9 데이터셋의 서로 다른 occupation은 몇 개인가 users['occupation'].unique
10 가장 많이 등장한 직업은? users['occupation'].value_counts()
11 데이터프레임을 요약
"""
print("1########################################################################")
print(users.head(25))
print("2########################################################################")
print(users.tail(10))
print("3########################################################################")
#print(users.info())
print(users.shape[0]) #0=행, 1=열
print("4########################################################################")
print(len(users.columns))
print("5########################################################################")
print(users.columns)
print("6########################################################################")
print(users.index)
print("7########################################################################")
#print(users.describe())
print(users.dtypes)
print("8########################################################################")
print(users['occupation'])
print("9########################################################################")
#print(len(users['occupation'].unique()))
print(users['occupation'].nunique())
print("10########################################################################")
"""
###########################################vaule_counts()############################################
"""
print(users['occupation'].value_counts()) #빈도수
print("11#######################################################################")
print(users.describe()) #기초통계량

#################################################################
data = {'A' : [1,2,3,4,5,6], 'B' : [0,2,4,6,8,10], 'C' : [2,2,2,2,2,2]}
df = pd.DataFrame(data)

print(df)
print(df.sum()) #열의 합
print(df.sum(axis=1)) #행의 합

import numpy as np
"""
1 A열에 인덱스 4, 5인 자료를 결측치로 변경
2 C열에 인덱스 2, 3, 4, 5인 자료를 결측치로 변경
3 각 열과 행에 결측치가 아닌 개수를 구하기
4 각 행에 nan가 아닌 값이 2개 이상인 데이터프레임의 일부를 출력
5 각 열에 nan이 아닌 값이 3개 이상인 데이터프레임의 일부를 출력
"""
#df['A'][4:6] = np.nan
df.loc[4:5,'A'] = np.nan #iloc랑 다름

df.loc[2:5,'C'] = np.nan
print(df)

print(df.notnull().sum())
print(df.notnull().sum(axis=1))

print(df.loc[df.notnull().sum(axis=1) > 1]) #행,렬

print(df.loc[:, df.notnull().sum() > 2]) #행,렬

"""
1 각 열에 nan이 아닌 값이 80% 이상이면 선택
"""
print(df.loc[:, df.notnull().sum() > len(df)*0.8])

# dropna 결측치 버림
print(df.dropna(axis=1))
print(df.dropna())
print(df.dropna(thresh= 0.8*len(df), axis=1))