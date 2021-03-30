#2개의 숫자 a, b를 받아서 a/b를 계산해주는 코드

def calAB() :
    while True :
        num = input("Input 2 Number : ").split(', ')
        try :
            A = int(num[0])
            B = int(num[1])
            print("result : ", A/B)
            break
        except ZeroDivisionError :
            print("cannot divide by zero")
        except ValueError :
            print("Input Z")


"""
while True:
    try:
        print("숫자 두개를 입력하세요")
        a, b = input().split(', ')
        a, b = int(a), int(b)
        a, b = map(int, input().split(", "))             편리한 기능
        print("계산의 결과는 ", a/b)
        break
    except ZeroDivisionError:
        print("0이 아닌 수를 입력하세요")
    except ValueError:
        print("정수를 입력하세요")

"""

"""
BMI 지수를 계산하는 코드
BMI = 체중(kg) / (키(m))**2
18.5 보다 작으면 저체중
18.5~23 정상
23~25 과체중
25~비만
"""
def BMI() :
    while True :
        try :
            weight , height = map(float, input("몸무게, 키 : ").split(", "))
            if (weight/(height)**2) < 18.5 :
                print("저체중")
            elif (weight/(height)**2) >= 18.5 and (weight/(height)**2) <= 23 :
                print("정상")
            elif (weight/(height)**2) >23 and (weight/(height)**2) <=25 :
                print("과체중")
            else:
                print("비만")
            break

        except ZeroDivisionError :
            print("cannot divide by zero")
        except ValueError :
            print("Input number")

#############################################함수#################################################모듈
"""
def 함수명(인자) :
    함수 본체


문서화 docstirng """"""
def mysum(a, b) :
    '''
    두 숫자를 인자로 받아 합을 리턴하는 함수
    '''
    return a + b
print(help(mysum))
print(help(abs))

print(print('a'))
출력값 : a \n None


A = print('A')
print(type(A))

def print42():
    print(42)
def return42():
    return 42

print(print42())
print(return42())
"""

"""
모듈 : py파일로 저장, 다른 사람이 저장
math, time

모듈 import 하는 방법
1. import math
    print(math.sin(math.pi))
2. import math as m                        as = nickname
    print(m.cos(0))
3. from math import cos, sin, tan, pi
    print(pi)
4. from math import *
    print(pi)
    print(exp(0))    = 1.0

    
"""


def shopping(file):
    file = open(file, "r")  # 파일열기
    buy_list = file.read()
    file.close()
    return buy_list

#print(shopping("shopping_list.txt"))
#print(type(shopping("shopping_list.txt")))
print(type(shopping("shopping_list.txt")))
buy_list = shopping("shopping_list.txt").split("\n")
print(buy_list)
"""
for item in buy_list:
    name, num, price = item.split(" " or "  ")
    print(name, num,"개", price, "원")

for item in buy_list:
    each_item = item.split(" ")
    print(each_item[0], "의 수량은 ", each_item[1], " 가격은", each_item[2])
"""
"""
for i in range(len(buy_list)):
    print("============================")
    print(buy_list[i])
"""
