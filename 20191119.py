import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#state/status/data/date
np.seed(111)

def CreateDataSet(Number): #Number에 따라 데이터 생성
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

    random_states = [state[np.randint( \
        low=0, high=len(state))] \
                     for i in range(len(rng))]

    Output.extend(zip(random_state, random_status, data, rng))

    return Output

dataset = CreateDataSet(4)
#print(dataset)

"""
데이터 프레임 만들기 
컬럼 1 스테이트 2 스테이터스 3 커스터머카운드 4 스테이터스데이터
"""

df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'CustomerCount', 'StatusData'])
#print(df)

"""
데이터 프레임 정보 확인
"""

#print(df.dtypes)#변수타입
#print(df.info())#데이터 정보 확인

"""
데이터 프레임 앞에 5개 행 확인
"""

print(df.head())

#파일 저장#######################################################################################
"""
df.to_excel("Lesson3.xlsx", index=False)

Location = "Lesson3.xlsx"
#cvs가져올때
df = pd.read_excel(Location, 0, index_col="StatusData")

print(df.head())
"""
#################################################################################################


"""
데이터의 State의 열에 이쓴 유일한 값들을 확인
"""
print(df.State.unique())
print(df["State"].unique())

#lambda argument : expression 익명함수
x = lambda a : a +10
print(x(5))
y = lambda a, b : a*b
print(y(3,7))

df['State'] = df.State.apply(lambda x : x.upper())
print(df.State.unique())

print(df.head(10))

"""
Status의 값이 1인 자료들만 선택해서 데이터프레임만들기
"""
mask = df.Status == 1
print(mask)

df = df[mask]
print(df.head())

"""
NJ을 NY으로 변경
"""
mask = df.State == "NJ"
df["State"][mask] = "NY"
print(df.State.unique())

"""
이상치 제거
"""
#4분위수, state와 statusDate의 년도을 기준으로 그룹을 구분한 후 각 그룹에 있는
#CustomerCount에 대해서 사분위수를 이용한 이상치 처리
#groupby 데이터 나누기, apply, transform
"""
dftest = pd.DataFrame({'_key' : ['A','B','C','A','B','C','A','B','C'],
                        'data' : [0, 5, 10, 5, 10, 15, 10, 15, 20],
                       'test' : [1,1,1,1,1,1,1,1,1]})#사전형 자료형
print(dftest)

print(dftest.groupby('_key').sum())
print('apply 병합')
print(dftest.groupby('_key').data.apply(lambda x:x.sum()))
print('transform 원래데이터크기 그대로')
print(dftest.groupby('_key').data.transform(lambda x:x.sum()))
"""
print(df.head())
print(df.reset_index().head())#새로운인덱스 생성, 기존 인덱스 밀려남

Daily = df.reset_index().groupby(['State', 'StatusData']).sum()
print(Daily)