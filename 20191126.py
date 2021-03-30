# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:24:48 2019

@author: USER
"""

import pandas as pd
import numpy.random as np
import matplotlib.pyplot as plt

# state/status/data(고객수)/date

np.seed(500)


def CreateDataSet(Number):
    Output = []

    for i in range(Number):
        rng = pd.date_range(start='1/1/2009', \
                            end='12/31/2012', \
                            freq='W-MON')

        data = np.randint(low=25, high=1000, \
                          size=len(rng))
        status = [1, 2, 3]
        random_status = [status[ \
                             np.randint( \
                                 low=0, high=len(status))] \
                         for i in range(len(rng))]

        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']

        random_states = [states[np.randint( \
            low=0, high=len(states))] \
                         for i in range(len(rng))]
        Output.extend(zip(random_states, random_status, \
                          data, rng))

    return Output


dataset = CreateDataSet(4)

df = pd.DataFrame(data=dataset, columns= \
    ['State', 'Status', \
     'CustomerCount', 'StatusDate'])

print(df.head())
print(df.tail())
print(df.info())


print(df.head())
print(df.dtypes)

print(df.State.unique())
print(df['State'].unique())

# lambda argument : expression
"""
x = lambda a : a + 10
print(x(9))
y = lambda a, b : a*b
print(y(13, 2))
"""

df.State = df.State.apply(lambda x: x.upper())
print(df.State.unique())

mask = df.Status == 1
df = df[mask]

print(df.head())

mask = df.State == 'NJ'
df['State'][mask] = 'NY'
print(df.State.unique())

"""
State와 StatusDate의 연도를 기준으로 그룹을 분리한 후,
각 그룹에 있는 CustomerCount에 대해서
사분위수를 이용한 이상치 처리.
"""

dftest = pd.DataFrame({ \
    'key': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'data': [0, 5, 10, 5, 10, 15, 10, 15, 20],
    'test': [1, 1, 1, 1, 1, 1, 1, 1, 1]})

print(dftest)

print(dftest.groupby('key').sum())

print(dftest.groupby('key').data.apply( \
    lambda x: x.sum()))

print(dftest.groupby('key').data.transform( \
    lambda x: x.sum()))

print(df.head())

print(df.reset_index().head())

Daily = df.reset_index().groupby([ \
    'StatusDate', 'State']).sum()
print(Daily.head(10))

del Daily['Status']

print(Daily.head(10))

StateYear = Daily.groupby([ \
    Daily.index.get_level_values(0).year,
    Daily.index.get_level_values(1)])

print(Daily.head(10))

Daily['Lower'] = StateYear['CustomerCount'].transform( \
    lambda x: x.quantile(.25) - 1.5 * ( \
                x.quantile(.75) - x.quantile(.25)))

Daily['Upper'] = StateYear['CustomerCount'].transform( \
    lambda x: x.quantile(.75) + 1.5 * ( \
                x.quantile(.75) - x.quantile(.25)))
Daily['Outlier'] = ((Daily['CustomerCount'] < Daily.Lower) | (Daily.CustomerCount > Daily.Upper))

print(Daily.head(10))

#이상치 제거
Daily = Daily[Daily.Outlier == False]
print(Daily.head(10))

###############################################################################################
import pandas as pd

d = [0,1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d)
print(df)

df.columns = ['Rev']
print(df)

df['NewCol'] = 5
print(df)
