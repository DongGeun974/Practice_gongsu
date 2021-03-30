"""
import pandas as pd

d = [0,1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d)
print(df)

df.columns = ['Rev']
print(df)

df['NewCol'] = 5
print(df)

df['NewCol'] = df['NewCol'] + 1
print(df)

#열삭제
del df['NewCol']
print(df)

df['test'] = 3
df['col'] = df['Rev']
print(df)

#인덱스 이름 변경
print(df.index)
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
print(df)

#행 가져오기, 데이터의 일부를 선택
print(df.loc["a"])
#슬라이싱 인덱스, 끝 포함
print(df.loc['a':'d'])
#숫자 인덱스, 끝 포함하지 않음
print(df.iloc[0:3])

#열 가져오기
print(df['Rev'])
#두개 이상
print(df[['Rev', 'test']])

#임의의 행, 열 가져오기
print(df.loc[df.index[0:3], 'Rev'])
print(df.loc[df.index[5:], 'col'])
print(df.loc[df.index[0:3], ['Rev', 'test']])

print(df.head())
print(df.tail())

"""
"""
import  pandas as pd
d = {'one' : [1,1], 'two' : [2,2]}
i = ['a','b']

df = pd.DataFrame(data = d, index= i )
print(df)

print(df.index)

#인덱스에 하위로 컬럼이 들어감
stack = df.stack()
print(stack)
print(stack.index)

unstack = df.unstack()
print(unstack)
print(unstack.index)

transpose = df.T
print(transpose)

"""
import  pandas as pd
d = {'one' : [1,1,1,1,1], 'two' : [2,2,2,2,2], 'letter' : ['a','a','b','b','c']}
df = pd.DataFrame(data=d)
print(df)

one = df.groupby('letter')
print(one.sum())

letterone = df.groupby(['letter', 'one']).sum()
print(letterone)

#인덱스 지우기
letterone = df.groupby(['letter', 'one'], as_index=False).sum()
print(letterone)

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
print(chipo)

"""
1. 10개의 행 확인
2. 데이터셋에는 몇 개의 관측치 확인(행 갯수 확인)
3. 열의 이름을 확인
4. 인덱스를 확인
"""
print(chipo.head(10))

print(chipo.info())
print(chipo.shape) # 행과 열

print(chipo.columns)

print(chipo.index)
