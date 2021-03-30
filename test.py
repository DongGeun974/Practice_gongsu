# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:24:48 2019

@author: USER
"""

import pandas as pd
import numpy.random as np
import matplotlib.pyplot as plt

#state/status/data(고객수)/date

np.seed(500)

def CreateDataSet(Number):
    Output = []
    
    for i in range(Number):
        rng = pd.date_range(start = '1/1/2009',\
                            end = '12/31/2012',\
                            freq = 'W-MON')
        
        data = np.randint(low = 25, high = 1000, \
                          size = len(rng))
        status = [1, 2, 3]
        random_status = [status[\
                         np.randint(\
                        low = 0, high = len(status))] \
                         for i in range(len(rng))]
        
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']
        
        random_states = [states[np.randint(\
                        low = 0, high = len(states))] \
                        for i in range(len(rng))]
        Output.extend(zip(random_states, random_status,\
                          data, rng))
        
    return Output

dataset = CreateDataSet(4)

df = pd.DataFrame(data = dataset, \
                  columns = ['State', 'Status',\
                             'CustomerCount', \
                             'StatusDate'])
print(df.head())
print(df.tail())
print(df.info())

"""
df.to_excel('Lesson3.xlsx', index = False)

Location = 'Lesson3.xlsx'

df = pd.read_excel(Location, 0, \
                   index_col = 'StatusDate')
"""
print(df.head())
print(df.dtypes)
print(df.index)
print(df.State.unique())
print(df['State'].unique())

#lambda argument : expression
x = lambda a : a + 10
y = lambda a, b : a*b
print(x(5))
print(y(3, 7))

df['State'] = df.State.apply(lambda x : x.upper())
print(df.State.unique())
print(df.head(10))

mask = df.Status == 1
print(mask)

df = df[mask]
print(df.head())

mask = df.State == 'NJ'
df['State'][mask] = 'NY'

print(df.State.unique())

"""
State, Status의 연도를 기준으로 그룹으로 구분한 후 
각 그룹에 있는 CustomerCount 에 대해서 
사분위수를 이용한 이상치 처리.
"""

# groupby; apply & transform

dftest = pd.DataFrame({'key' : \
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'data' : [0, 5, 10, 5, 10, 15, 10, 15, 20],
    'test' : [1, 1, 1, 1, 1, 1, 1, 1, 1]})

print(dftest)

print(dftest.groupby('key').sum())
print(dftest.groupby('key').data.apply(lambda x: x.sum()))
print(dftest.groupby('key').data.transform(lambda x: x.sum()))

print(df.head())
print(df.reset_index().head())

Daily = df.reset_index().groupby(\
                      ['StatusDate', 'State']).sum()

## 컬럼 지우기
del Daily['Status']
del Daily['index']
print(Daily.head(10))

#print(Daily.index)
#print(Daily.index.levels[0])
#print(Daily.index.get_level_values(1))


"""사분위수 이상치 처리
Q1 : 25% 
Q2 : 50%, 중앙값 
Q3 : 75%

사분위수 범위(IQR = Q3 - Q1)

수염 끝값 = Q3 + 1.5IQR, Q1 - 1.5IQR
벗어난 값은 이상치
"""
#사분위수 구하는 함수
"""
dftest1 = pd.DataFrame({'A' : [1,2,3,400,5,6,7,8,9,10]})
print(dftest1)
Q1 = dftest1.A.quantile(q=0.25)
Q2 = dftest1.A.quantile(q=0.5)
Q3 = dftest1.A.quantile(q=0.75)
IQR = Q3 - Q1

dftest1['lower'] = Q1 - 1.5*IQR
dftest1['upper'] = Q3 + 1.5*IQR
dftest1['Outlier'] = 

x = pd.Series([1,2,3,4,5])
y = pd.Series([5,5,5,5,5])
print(x > y)
print(x < y)
print((x > y) | (x == y))
"""

#컬럼 바꿈!#################################################
StateYear = Daily.groupby([Daily.index.get_level_values(0).year,Daily.index.get_level_values(1)])

Q1 = StateYear['CustomerCount'].quantile(q=0.25)
Q2 = StateYear['CustomerCount'].quantile(q=0.5)
Q3 = StateYear['CustomerCount'].quantile(q=0.75)
IQR = Q3 - Q1

Daily['Lower'] = StateYear['CustomerCount'].transform(lambda x : x.quantile(.25) - (1.5*((x.quantile(.75)) - x.quantile(.25))))
Daily['Upper'] = StateYear['CustomerCount'].transform(lambda x : x.quantile(.75) + (1.5*((x.quantile(.75)) - x.quantile(.25))))
Daily['Outlier'] = (Daily["CustomerCount"] < Daily["Lower"]) | (Daily["CustomerCount"] > Daily["Upper"])
print(Daily.head(20))
