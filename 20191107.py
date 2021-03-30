import numpy as np

a = np.arange(10)
print(a)

b = np.arange(1,9,2)
print(b)

c = np.linspace(0,1,6)
print(c)

d = np.linspace(0,1,6,endpoint=False)
print(d)

e = np.linspace(0,1,7)
print(e)

f = np.zeros((2,2))
print(f)

g = np.ones((2,2))
print(g)

i = np.eye(2)
print(i)

h = np.diag([1,2,3])
print(h)

h1 = np.diag((1,2,3))
print(h1)

h2 = np.diag(np.arange(1,7,2))
print(h2)

h3 = np.arange(0,9).reshape(3,3)
print(h3)

h4 = np.diag(h3)#2차원에서 대각선
print(h4)

h5 = np.diag(h3, k =1)#2차원에서, 대각선옮김, 양수는 위로, 음수는 아래로
print(h5)

print(np.diag(np.diag(h3, k =1), k = -1))#2 > 1 > 2차원 이동

###############################자료형확인##########################################

print(np.ones((2,3)).dtype)
print(np.zeros((2,2)).dtype)
print(np.eye(4).dtype)

print(np.array([1+3j, 2 +5j]).dtype)

#난수생성 : np.random.rand() - [0부터 1)사이에 임의의 값, np.random.randn() - 정규분포(normal dist)에서 난수를 생성

f = np.random.rand(4)
print(f)
f1 = np.random.rand(2, 3)
print(f1)

g = np.random.randn(4)
print(g)

g1 = np.random.randn(2,3)
print(g1)

np.random.seed(0)
print(np.random.rand(4))

np.random.seed(0)
print(np.random.rand(4))

np.random.seed(1234)
print(np.random.rand(4))

import matplotlib.pyplot as plt
rand_numbers = np.random.rand(1000)
plt.hist(rand_numbers, bins=10)
plt.show()

gaussian_numbers = np.random.randn(1000)
plt.hist(gaussian_numbers, bins=10)
plt.show()

#예제문제
"""
[[1,1,1,1]
[1,1,1,1]
[1,1,1,2]
[1,6,1,1]]
3줄이내
"""
ex1 = np.ones((4,4))
ex1[2,3] = 2
ex1[3,1] = 6
print(ex1)

"""
[[0,0,0,0,0,0]
[2,0,0,0,0,0]
[0,3,0,0,0,0]
[0,0,4,0,0,0]
[0,0,0,5,0,0]
[0,0,0,0,6,0]]
"""
ex2 = np.diag(np.arange(2,7), k=-1)
print(ex2)

"""
[[4,3,4,3,4,3]
[2,1,2,1,2,1]
[4,3,4,3,4,3]
[2,1,2,1,2,1]]
"""
ex3 = np.tile(np.arange(4,0,-1).reshape((2,2)),(2,3))
print(ex3)
