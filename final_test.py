# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:24:48 2019

@author: USER
"""
"""
import pandas as pd
import numpy.random as np
import matplotlib.pyplot as plt

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']

np.seed(500)
# np.randint(low = 1, high = 100)
random_names = [ names[\
                np.randint(low = 0, \
                           high = len(names))] \
                for i in range(1000)] #1000개

print(random_names[0:10])

births = [ np.randint(low = 0, high = 1000) \
          for i in range(1000)]

print(births[0:10])

BabyDataSet = list(zip(random_names, births))
print(BabyDataSet[0:10])

df = pd.DataFrame(data = BabyDataSet, \
                  columns = ['Names', 'Births'])
print(df[0:10])

#csv 파일저장, csv 파일 가져오기
df.to_csv('births1880.csv', index = False, \
          header = False)

Location = 'births1880.csv'

df = pd.read_csv(Location, header = None)
print(df[:10])


df = pd.read_csv(Location, \
                 names = ['Names', 'Births'])
print(df[:10])

print(df.info())
print(df.head(10))
print(df.tail())

print(df.Names.unique())

for x in df.Names.unique():
    print(x)

print(df.Births.describe())

name = df.groupby('Names')
df = name.sum()
print(df)

df.Births.plot.bar()

df = df.sort_values(by = 'Births', \
                    ascending = False)
print(df)
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
print(dataset[:10])













