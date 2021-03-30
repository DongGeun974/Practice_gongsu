# one line

"""
여려줄 주석

변수명 규칙

자료형
-숫자형
--정수형 int
--부동소수점 float
---정수/정수 = float 중요
---정수//정수 = 정수부분만
---정수%정수 = 나머지
---(-7/2) = -3.5, // = -4, % = 1
---제곱 2**3 = 2^3
---루트 2**0.5 = 루트2
---정수와 부동소수점이랑 강제형변환 가능 : int(3.5) , float(8)   저장은 안됨 사용할려면 변수에 저장하여 사용
연산 결과값을 변수 대입 '='
연산순위 = P E D M A S 괄호 지수 곱셈 나눗셈 덧셈 뺄셈
-부울형 bool형
--True, False, 첫 문자는 대문자
--not, and, or 부울 연산자, 뒤에 있는 걸 확인 할 필요가 없으면 확인 안함
--'!=' 다른지 확인, '==' 같은 지 확인

"""

#두 숫자의 평균값을 구하는 함수
def average(a, b) :
    """
    :param a: 숫자
    :param b: 숫자
    :return: a+b average
    """
    return  (a+b)/2
print(average(3,4))

#두 숫자의 기하평균을 리턴하는 함수
def geometric_mean(a, b) :
    return (a*b)**0.5
print((geometric_mean(2, 8)))

#두 숫자 a와 b 사이의 거리를 리턴하는 함수, abs절대값
def distance(a, b):
    return abs(a-b)
print(distance(5, 2))

#바닥 면적이 A이고, 높이가 h인 피라미드의 부피를 리턴하는 함수
def pyramid_volume(A,h) :
    return A*h/3
print(pyramid_volume(10, 3))

#초(second)단위의 숫자를 받아 일(day) 단위의 값을 리턴하는 함숫
def second2day(sec) :
    return (sec/86400)
print(second2day(3600))