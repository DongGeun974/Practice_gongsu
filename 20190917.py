week_days = " Mon, The, Wed, Thu, Fri, Sat, Sun "

#strip() : 끝에 공간이 사라짐
print(week_days.strip())

#쪼갠다 > 리스트가 됨
print(week_days.split())

print(week_days.strip().split())

#repalce("A", "B") A을 B로 바꾸다
print(week_days.replace("M", "m"))

#upper() : 전부 대문자로
print(week_days.upper())

#lower()
print(week_days.lower())

#앞만 대문자
print(week_days.strip().capitalize())

#title()
print(week_days.strip().title())

#startwith() T or F
print(week_days.startswith(" M"))
print(week_days.startswith("K"))

#endwith()
print(week_days.endswith("n "))
print(week_days.endswith("e"))

print(week_days)
#불변자료형


#두개의 자연수 k, m이 주어졌을 때, 만약 m이 3의 배수이거나 3으로 끝나는 숫자일 경우에만 k와 m을 더하고, 아닌 경우에는 k를 리턴하는 함수
def sum_if_3(k , m) :
    if(m % 3 == 0) or (str(m).endswith("3")) :
        return k+m
    else :
        return k

print(sum_if_3(4, 3))
print(sum_if_3(5, 13))

#두개의 자연수 k, m이 주어졌을 때, 만약 m이 3의 배수이거나 3을 포함하는 경우에만 k와 m을 더하고, 아닌 경우에는 k를 리턴하는 함수
def sum_if_3s(k, m) :
    if(m % 3 == 0) or ("3" in str(m)) :
        return k+m
    else:
        return k

print(sum_if_3s(3, 13))
print(sum_if_3s(4, 42))

"""
if 조건문 :
    실행코드
else:
    실행코드
    
    
else if
"""

num1 = 5
num2 = 10

if num1 < num2 :
    print("num1이 num2보다 작다")
else :
    if num1 == num2 :
        print("num1과 num2가 같다")
    else:
        print("num1이 num2보다 크다")

if num1 < num2:
    print("num1이 num2보다 작다")
elif num1 == num2:
    print("num1과 num2가 같다")
else:
    print("num1이 num2보다 크다")

#====================================
"""
while 조건 :
    실행코드
"""
num = 43
div = 7
count = 0
while num > div :
    num -= div
    count += 1
print(count)

"""
두 정수의 최대 공약수를 구하는 함수
유클리드 호제법
1 작은 수로 큰수를 나눈다
    만약 나누어 떨어진다면 gcd는 작은수
    아니면 작은수를 나머지로 나눈다
    
    15, 9
    
    15/9 = 몫 1 나머지 6
    
    9 != gcd
    
    9/6 = 몫 1 나머지 3
    
    6 != gcd
    
    6/3 = 몫 2
    
    3 == gcd
    
def gcd(a,b):
    if a < b:
        a, b = b, a
    while b != a:
        a, b = b, a%b
    return a
"""
def gcd(a, b) :
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)

print(gcd(52, 26))




"""
자연수 n이 주어졌을 때, 1부터 n까지의 자연수 중 3의 배수이거나
숫자 3을 포함하는 숫자들의 합을 구하는 함수 sum_of_3()만들기
"""