
"""
예외처리
"""

"""
number_input = input("A number please: ")
print(type(number_input))


강제형변환 int()는 정수형만 변형 가능
int(3.0)
int('3')
중요) 에러
int(3.2)
int('3.2')

문법오류 따옴표 중요

들여쓰기 중요

문자열연산은 + 와 * 만 가능
문자열의 len함수는 존재x -> 그냥 함수 len()만 존재




$$$$$$$$예외처리$$$$$$$$$
try :
    code1
    오류가 발생하면 except문로 감
except :
    code2
    

"""
"""
n = True
while n :
    number_input = input("A number please : ")
    try :
        number = int(number_input)
        print("제곱의 결과는 ", number ** 2  , "입니다")
        n = False  #break
    except :
        print("정수를 입력하세요")






"""
"""
여러가지 오류 처리
number_input = input("A number please : ")
try :
    number = int(number_input)
    a = 5/(number - 4)
    print("결과는", a)
except ValueError : #주기 이름달기
    print("정수를 입력하세여")
except ZeroDivisionError :
    print("4가 아닌 수를 입력하세요")

"""
"""
#함수가 아직 완전히 정의되어 있지 않을때
def to_define(n) :
    
    raise NotImplementedError("아직 미정의")

print(to_define((3)))
"""

def my_square(n) :
    """
    :param n: 입력받는 수
    :return: n의 제곱 리턴
    """
    return n**2

#print(help(my_square))
#print(my_square(3))

"""
0이 아닌 숫자가 입력될 경우 100을 그 숫자로 나눔
0이 입력되면 0이 아닌 숫자를 입력하라는 문구 출력
숫자가 아닌 값이 입력되면 숫자를 입력하라는 문구 출력
"""
while True :
    num = input("Input number : ")
    try :
        int_num = int(num)
        print("Result : " , 100/int_num)
        break
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
"""
두 개의 숫자 a, b를 입력받아 a/b를 계산하는 코드
"""
while True :
    a, b = input("Input a :"), input("Input b :")
    try :
        int_a = int(a)
        int_b = int(b)
        print("Result : ", int_a/int_b)
        break
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")