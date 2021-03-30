import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np

#state/status/data/date
np.seed(500)

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

df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'CustomerCount', 'StatusData'])


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


print(df.head())
print(df.reset_index().head())#새로운인덱스 생성, 기존 인덱스 밀려남

Daily = df.reset_index().groupby(['State', 'StatusData']).sum()
print(Daily)