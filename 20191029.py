#리스트 조건 제시법

odd1_20 = [1,3,5,7,9,11,13,15,17,19]
print(odd1_20)

i = 0
odd2_20 = []
while i <= 20:
    if i % 2 == 1:
        odd2_20.append(i)
    i += 1
print(odd2_20)

odd3_20 = []
for i in range(21):
    if i % 2 == 1:
        odd3_20.append(i)
print(odd3_20)

def odd_number(num):
    _List = []
    for i in range(num+1):
        if i % 2 == 1:
            _List.append(i)
    return  _List
print(odd_number(20))

odd_100M = odd_number(100000)
print(odd_100M[:21])

"""
#속도측정
import time
start = time.clock()
odd_100M = odd_number(100000)
end = time.clock()
print(end - start)
"""

#####################################조건제시법으로 변경#########################################
"""
1.
{x | 0 <= x <= 100000, 단 x는 홀수}
2.
[x | 0 <= x <= 100000, 단 x는 홀수]
3. 컴프리헨션
[x for x in range(100001) if x % 2 == 1]
"""
odd1_100 = [x for x in range(100001) if x % 2 == 1]
print(odd1_100[:20])

#0~100000사이에 이쓴 값들을 제곱한 값을 담고 있는 리스트
li = [x for x in range(101) if x % 2 == 1]
print(li)
li_2 = [2*x+1 for x in range(50)]
print(li_2)

odd_100_square = [x**2 for x in range(1001) if x%2==1]
print(odd_100_square[:20])

##################################그래프그리기#######################################
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

xs = [x for x in range(-10, 11)]
ys = [x**2 for x in xs]

plt.plot(xs, ys)
plt.show()

#exp지수함수 math.exp [exp(1), exp(3) ,,, exp(9)]
from math import exp
exp_odd10 = [exp(x) for x in range(10) if x%2==1]
print(exp_odd10)
#[exp(3), exp(6), exp(9), exp(12), exp(15)]
exp_3 = [exp(x) for x in range(1,16) if x%3==0]
print(exp_3)

#절대값 그래프
import math
xs_1 = [x for x in range(-10, 11)]
ys_1 = [abs(x**2 - 50) for x in xs_1]

xs = [x for x in range(-10, 11)]
ys = [x**2 for x in xs]

plt.plot(xs_1, ys_1)
plt.show()

#relu
xs_2 = [x for x in range(-10, 11)]
ys_2 = [max(0, x) for x in xs_2]
ys_2 = [x if x > 0 else 0 for x in xs_2]
print(ys_2)
plt.plot(xs_2, ys_2)
plt.show()


