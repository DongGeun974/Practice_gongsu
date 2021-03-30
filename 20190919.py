"""
    9 , 15
1.  15, 9
2.  15/9 몫 = 1 나머지 = 6
3.  9/6 몫 = 1 나머지 = 3
4.  6/3 몫 =2 나머지 = 0
따라서 최대공약수 3
"""

#최대공약수
def gcd(a, b) :
    if a < b :
        a, b = b, a

    while b != 0 :
        a, b = b, a % b

    return a

#최소공배수
def lcm(a, b):
    return a*b/gcd(a,b)

print(lcm(9, 15))

"""
range(시작, 끝, 계단) 3개의 인자
1개의 인자 = 끝, 시작 = 0, 계단 = 1
"""
for i in range(6) :
    print(i)

for i in range(2, 7, 2) :
    print(i, " 제곱 ", i**2)

a_word = "hamster"

for i in range(7) :
    print(a_word[i])

for i in a_word :
    print(i)

#word에 dog가 있으면 true, 없으면 false
def find_dog(word) :
    for i in range(0, (len(word) - 2), 1) :
        if word[i:i+3] == "dog" :
            return True

    return False

print(find_dog("dog, cat"))
"""
def find_dog (word) :
    if "dog" in word :
        :return True
    else :
        :return False
"""
#자연수 n이 주어졌을 때, 1부터 n까지의 자연수 중에서 3의 배수이거나 숫자 3을 포함하는 숫자들을 합하는 함수
def sum_of_3s(n) :
    sum = 0
    for i in range(1, n+1):
        if (i%3 == 0) :
            sum += i
        elif "3" in str(i) :
            sum += i

    return sum

print(sum_of_3s(14))

#a를 A로 변경
aword = "aardvarks"
def aUpper(word) :
    return word.replace("a", "A")

print(aUpper(aword))
"""
aword = "aardvarks"
new_word = ""

for char in aword:
    if char == "a":
        new_word += "A"
    else:
        new_word += char
print(new_word)
"""
# n o r t h w e s t e r n -> northwestern
b_word = "n o r t h w e s t e r n"

def noBlank(word) :
    new_word = ""
    for char in word:
        if char != " ":
            new_word += char
    return (new_word)

print(noBlank(b_word))
print(noBlank(b_word).title())

# a의 갯수, aeiou제거한 문자열 출력

words = "When you are smiling, \
the whole world smiles with you"

def cnt_a(word) :
    cnt = 0
    for i in range(len(word)):
        if word[i] == "w":
            cnt += 1
    return cnt
print(cnt_a(words))
print(words.lower().count("w"))
#대소문자 구분, 순서중요

def deleteAeiou(word) :
    new_word = ""
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' :
            new_word += char
    return new_word
print(deleteAeiou(words))

new_words = ""
for word in words:
    if word not in "aeiou": #아에이오우가 없다면?
        new_words += word
print(new_words)