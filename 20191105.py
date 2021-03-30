#컬렉션자료형
"""
리스트-느리다, 딕셔너리, 튜블

넘파이 : 컬렉션자료형의 단점을 보안
"""
import numpy as np

a = np.array([0,1,2,3])
print(a)
print(type(a))

b = np.array((0,1,2,3))
print(b)
print(type(b))

#항목별로 비교연산
c = a == b
print(c.dtype)
print(b.dtype)

d = np.array([True, True, False], dtype=int)
print(d)

"""
#넘파이는 같은자료형?? 장점은 빠른 처리 속도
import time
start1 = time.process_time()
a_list = range(0,10000000,2)
a_list_square = [i**2 for i in a_list]
end1 = time.process_time()
print("시간1은 ", end1 - start1)

start2 = time.process_time()
an_array = np.arange(0,10000000,2)
square = an_array**2
end2 = time.process_time()
print("시간2는", end2 - start2)
"""

#array 생성방법
a_1dim = np.array([0,1,2,3])
print(a_1dim)
print("차원",a_1dim.ndim)#n차원확인
print("shape",a_1dim.shape)

a_2dim = np.array([[1,2],[3,4],[5,6]])
print(a_2dim)
print("차원",a_2dim.ndim)#n차원확인
print("shape",a_2dim.shape)

print(len(a_2dim))
print(len(a_2dim.shape))
print(np.shape(a_2dim))

print(np.shape(a_2dim)[0] == len(a_2dim))
print(len(np.shape(a_2dim)) == a_2dim.ndim)
