# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:25:00 2019

@author: USER
"""
import pandas as pd

States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', \
         'GA', 'GA', 'FL', 'FL']
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods = 10, \
                    freq = 'MS')
df1 = pd.DataFrame(data, index = idx, \
                   columns = ['Revenue'])
df1['State'] = States
print(df1)

data2 = [10.0, 10, 9, 9, 8, 8, 7, 7, 6, 6] 
idx2 = pd.date_range('1/1/2013', periods = 10, \
                    freq = 'MS')
df2 = pd.DataFrame(data2, index = idx2, \
                   columns = ['Revenue'])
df2['State'] = States
print(df2)

df = pd.concat([df1, df2])
print(df)

newdf = df.copy()
newdf['x-Mean'] = abs(newdf['Revenue'] - \
                       newdf['Revenue'].mean())
newdf['1.96*Std'] = 1.96*newdf['Revenue'].std()
newdf['Outlier'] = newdf['x-Mean'] > newdf['1.96*Std']
print(newdf)

newdf = df.copy()
#State별 Revenue 값에 대한 이상치처리 - 정규분포
State = newdf.groupby('State')

newdf['x - Mean'] = State.transform(\
                       lambda x : abs(x - x.mean())) 
newdf['1.96*Std'] = State.transform(\
                       lambda x : 1.96*x.std())
newdf['Outlier'] = newdf['x - Mean'] > newdf['1.96*Std']
print(newdf)


newdf = df.copy()
State = newdf.groupby('State')
newdf['Lower'] = State.Revenue.transform(\
                lambda x : x.quantile(.25) - \
               1.5*(x.quantile(.75) - x.quantile(.25)))
newdf['Upper'] = State.Revenue.transform(\
                lambda x : x.quantile(.75) + \
               1.5*(x.quantile(.75) - x.quantile(.25)))
newdf['Outlier'] = (newdf['Revenue'] < newdf['Lower']) | \
                   (newdf['Revenue'] > newdf['Upper'])
                   
print(newdf)                  







