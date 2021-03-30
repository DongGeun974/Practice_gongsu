import math

#문제6. 변의 길이가 각각 a,b,c인 직각육면체의 표면적을 계산해 주는 함수
def box_surface(a, b, c) :
    return 2*(a*b + b*c + a*c)

#문제7. 주어진 자연수 n이 짝수면 True, 홀수면 False를 리턴해주는 하수
def even_test(n) :
    if (n%2 == 0) :
        return True
    else :
        return False

#문제8. 반지름 r인 원의 넓이를 구하는 함수
def circle_area(r) :
    return r**2 * math.pi

#문제9. 변의 길이가 각 a, b, c인 삼각형의 면적 A를 계산하는 함수
def triangle_area(a, b, c) :
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

#문제 10, 정삼각형의 넓이를 구하는 함수
def eq_triangle_area(a) :
    return (math.sqrt(3))/4*a**2

###############################################################################
"""
print(box_surface(1, 1, 1))

print(even_test(3))

print(circle_area(2))

print(triangle_area(1, 1, 1))

print(eq_triangle_area(1))
"""
###################################################################################
"""
hello = "hello"
print(hello)
hi = "hi"
print(hi)
print(type(hi))

afa = "kebap"
print(afa)
print("kebap" + " and " + afa)
print(" kebap" * 3)
"""
##############################
import urllib.request

page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf-8")

print(text)
"""
#슬라이싱 
 문자열[시작인덱스 : 끝인덱스 : 계단(step)]
 끝인덱스의 전까지만 나타낸다
 시작값이 더 작아야한다
"""

a_food = "kebap"
print(a_food[0])
print(a_food[3])
print(a_food[-1])
print(a_food[1:3])
print(a_food[0:3:2])
print(a_food[-1::-1]) #reverse


#find metod 인덱스를 알려줌, 여러번 등장하면 제일 앞에 것
print(text.find(">$"))
print(text[232])
print(text[234:238])

price_index = text.find(">$") + 2
bean_price_str = text[price_index : price_index+4]
print(bean_price_str)

###############################################################
#6달라 이상시 인상 프린트
import urllib.request
import time

price = 5.0

while price < 6.0 :
    time.sleep(1)
    page = urllib.request.urlopen("https://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf-8")
    where = text.find(">$") + 2
    price_str = text[where:where+4]
    price = float(price_str)

print("커피의 가격은" + price_str + " 아메리카노 가격인상")