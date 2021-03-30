"""
2016250056 황동근
"""
"""
1. 자연수 n을 입력받아 n 번째 피보나치 수를 리턴하는 함수 fibo(n)를 구현하라.
참고) fibo(1) = 1, fibo(2) = 1, fibo(n) = fibo(n-1) + fibo(n-2)이다.

test) fibo(5) = 5, fibo(10) = 55
"""
def fibo(n) :
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#test
print(fibo(5))
print(fibo(10))

"""
2. 쇼핑리스트(첨부파일)을 입력받아, 총 가격을 리턴하는 함수 shopping_total_sum(shopping_file)를 구현하라.
단, 이 함수는 아래의 조건을 만족시킨다.

(1) 함수가 실행된 후, 구매가능한 물품과 가격을 출력한다.
    이후 구매할 물품과 수량을 입력하면, 선택한 물품에 대한 총 가격을 리턴해준다. 
(2) 발생할 수 있는 오류에 대한 예외 처리를 한다. 

test) shopping_total_sum('shopping_list.txt') 을 실행 후,
       tomato : 1, cola : 2를 입력하면,  5000원을 리턴해준다.
"""
def shopping_total_sum(file):
    _file = open(file, "r")
    _list = _file.read()
    _file.close()

    buy_list = _list.split("\n")

    for item in buy_list:
        print(item.split(" ")[0] + "은 " + item.split(" ")[1] + "개는 " + item.split(" ")[2] + "원 입니다.")

    items = input("구매할 물품과 수량을 입력하세요.(예 tomato : 1, cola : 2) : ")

    lowItems = items.lower().split(", ")
    hap = 0
    try:
        for i in range(len(lowItems)):
            if 'bread' in lowItems[i] :
                num = int(lowItems[i].split(" ")[2])
                hap += num * 3000
            elif 'tomato' in lowItems[i] :
                num = int(lowItems[i].split(" ")[2])
                hap += num * 2000
            elif 'cola' in lowItems[i] :
                num = int(lowItems[i].split(" ")[2])
                hap += num * 1500
            else:
                raise Exception()

        return hap

    except IndexError:
        print("예시와 같이 입력하세요.")
    except ValueError:
        print("개수에 정수만 입력세하세요.")
    except Exception:
        print("물품을 입력하세요.")

#test(input "tomato : 1, cola : 2")
print(shopping_total_sum("shopping_list.txt"))

"""
3. 리스트를 받아 중복값을 제거한 리스트를 리턴해주는 remove_elt(list) 함수를 구현하라.

test) remove_elt(['a', 'a', 'b', 'c', 'd', 'b']) = ['a', 'b', 'c', 'd']
"""
def remove_elt(para):
    len_list = len(para)
    i = 0
    while True:
        len_list = len(para)
        if i > len_list-1:
            break
        else:
            if para.count(para[i]) > 1:
                li.pop(i)
                i -= 1
        i += 1

    para.sort()

    return para

#test
li = ['a', 'a', 'b', 'c', 'd', 'b']
print(remove_elt(li))