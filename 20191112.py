import numpy as np
import matplotlib.pyplot as plt

"""
# y = 3x
xs = np.linspace(0, 3, 30)
ys = xs*3
plt.plot(xs, ys, 'o')
plt.show()

# y = x^2
xs = np.linspace(-1,1,20)
ys = xs**2
plt.plot(xs, ys, 'red')
plt.show()
"""

#########################################################################################################
"""
data = np.loadtxt('populations.txt')
#print(data)

year, hares, lynxes, carrots = data.T #전치행렬 .T
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)

plt.legend(('Hare', 'Lynx', 'Carrot'), loc = (1.05, 0.5))
plt.show()
"""
###################################################################################################

import matplotlib.pyplot as plt
import pandas as pd

# 1 데이터 만들기
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))
print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])          #DataFrame
print(df)

df.to_csv('births1880.csv', index=False, header=False)

# 2 데이터 가져오기
Location = 'births1880.csv'
df = pd.read_csv(Location, names=['Names', 'Births'])
print(df)

# 데이터 삭제
import os
os.remove(Location)

# 데이터 타입 확인
print(df.dtypes)
print(df.Births.dtypes)
print(df['Births'].dtypes)

# 데이터 분석
sorted = df.sort_values(['Births'], ascending=False)
print(sorted)
print(sorted.head(1))

print(df.Births.max())

# 데이터 표현
df.Births.plot()

MaxValue = df.Births.max()
MaxName = df.Names[df.Births == df.Births.max()].values
Text = str(MaxValue) + " - " + MaxName
print(Text)

plt.annotate(Text, xy=(1, MaxValue), xytext = (8,0), xycoords=('axes fraction', 'data'),
             textcoords='offset points')
plt.show()