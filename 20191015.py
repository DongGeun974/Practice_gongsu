"""
"""
"""
even_number = (2, 4, 6, 8)
print(even_number)
print(type(even_number))

week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
print(week)

#튜플 괄호 생략 가능
a = 10, 20, 30, 40, 50
print(a)
print(type(a))

print(a[1])
print(a[-1])
print(a[::2]) #######################################??

b, c = 1, 2
print(b)
print(c)
print(type(b))
b, c = c, b
print(b)
print(c)

#함수 리턴값 여러개
def f(x):
    return x**2, x**3

b, c = f(3)
print(b)
print(c)

#불변자료형 문자열 튜플
a = ("hello", "world")
print(a)
b = ("hi", a[1])
print(b)

c = ("hi",) + a[1]
print(c)

d = ([1,2,3], 'd')
#d[0] = [1,2,3,4]
d[0].append(4)
print(d)
"""

"""
#튜블 메소드
a = ('b','b','c','c','c')
print(a.count('c'))
print(a.index('c'))
"""

file_open = open("Students_Records/Byun_Sato.txt", "r")
for line in file_open.readlines():#전체 내용을 리스트로, readline은 첫줄만
    print(line)

def date_of_birth(date):
    """
    """
    """
    out = date.split(".")
    out_list = []
    out_list.append(int(out[0]) + 1900)
    out_list.append(int(out[1]))
    out_list.append(int(out[2]))
    return tuple(out_list)
    """

    year,  month, day = date.split(".")
    #year,  month, day = map(int,date.split("."))
    year = int(year) +1900
    month = int(month)
    day = int(day)
    return year, month, day

print(date_of_birth('95.4.28'))

#튜블만들기
import string #whitespace : 공백
def record_getter(filename):
    """
    지정된 학생의 신상정보를 리스트에 담아 리턴해주는 함수
    각 항목은 항목명과 내용의 튜플로 구성됨
    :param filename:
    :return:
    """
    std_data = []
    a_file = open(filename)
    for line in a_file.readlines():
        if line[0] == '#' or line in string.whitespace:
            continue
        else:
            item, value = line.split(":")
            item = item.strip()
            value = value.strip()
            if item == 'Date of Birth':
                value = date_of_birth(value)

            std_data.append((item, value))

    return std_data

print(record_getter("Students_Records/Byun_Sato.txt"))
print(record_getter("Students_Records/Pi_Matgol.txt"))

for item in record_getter("Students_Records/Byun_Sato.txt"):
    if "Department" in item[0]:
        print(item[1])
        break
