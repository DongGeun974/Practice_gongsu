"""
import pandas as pd
import numpy.random as np
import matplotlib.pyplot as plt

names = ["Bob", 'Jessica', 'Mary', 'John', 'Mel']

np.seed(500)
random_name = [names[np.randint(low = 0, high = len(names))] for i in range(1000)]
print(random_name[:20])

births = [np.randint(low=0, high=1000) for i in range(1000)]
print(births[:20])

BabyDataSet = list(zip(random_name, births))
print(BabyDataSet[:10])

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

#####################################################################################
# 1 데이터 저장하기
df.to_csv('births1880.csv', index=False, header=False)

# 2 데이터 가져오기
Location = 'births1880.csv'
df = pd.read_csv(Location, names=['Names', 'Births'], header=None)
####################################################################################
print(df.head(10)) #앞에 디폴트 5 또는 n개 확인
print(df.tail())
print(df.info()) #dataframe정보

df = pd.read_csv(Location, names = ['Names', 'Births'])
print(df.head())

print(df.Names.unique())
for x in df.Names.unique():
    print(x)

print(df.Births.describe())

name = df.groupby('Names') #데이터 합치기, 그룹핑
df = name.sum()
print(df)

#막대그래프 bar
df.Births.plot.bar()
plt.show()

df = df.sort_values(by='Births', ascending=False)
print(df)
"""

#######################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#state/status/data/date
np.seed(111)

def CreateDataSet(Number):
    Output = []

    for i in range(Number):
        #date
        rng = pd.date_range(start='01/01/2009', end='12/31/2012', freq='W-Mon')

        #data
        data = np.randint(low=25, high=1000, size=len(rng))

        #status
        status = [1,2,3]
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]

        #state
        state = ["GA", "Fl", "fl", "NY", "NJ", "Tx"]
        random_state = [state[np.randint(low=0,high=len(state))] for i in range(len(rng))]

    Output.extend(zip(random_state, random_status, data, rng))

    return Output

dataset = CreateDataSet(4)
print(dataset)