def shopping(file):
    file = open(file, "r")  # 파일열기
    buy_list = file.read()
    file.close()
    return buy_list

buy_list = shopping("shopping_list.txt").split("\n")
print(buy_list)
############################################################################################################3
# 파일을 인자로 받아서 총 비용을 리턴해주는 함수
def shopping_amount(shopping_file):
    _list = shopping(shopping_file).split("\n")
    sum = 0
    for item in _list:
        sum += int(item.split()[2])  # 공백을 기준으로 분리
    return sum


print(shopping_amount("shopping_list.txt"))

"""

    sum = 0
    arr[] = shopping_file.split(" ")
    for i in  :
        sum += i
    return i 
    """

##################################################################################################################
# 구매할 수량이 달라졌을 때, 그 총 가격을 리턴해주는
def shopping_amount_n(shopping_file):
    """sum = 0
    a = []
    _list = shopping(shopping_file).split("\n")

    for item in _list:
        sum += int(input(item.split()[0] + " input : ")) * int(item.split()[2])

    return sum"""

    buy_list = shopping(shopping_file).split("\n")
    print("bread, tomato, cola 구매 수량을 순서대로 입력하세요")

    while True:
        try:
            number = list(map(int, input().split(", ")))
            break
        except ValueError:
            print("정수를 입력하세여")

    sum = 0

    for i in range(len(buy_list)):
        sum += int(buy_list[i].split()[2]) * number[i]

    return sum
print(shopping_amount_n("shopping_list.txt"))

################################################################################################################
#쇼핑파일을 인자로 받아서 구매할 물건을 묻고 그것의 가격을 리턴해주는
def shopping_item(shopping_file) :
    buy_list = shopping(shopping_file).split("\n")
    item = input("Bread, Tomato, Cola 중에서 살 품목을 적어주세요 : ")
    sum = 0
    if 'bread' in item.lower():
        sum += int(buy_list[0].split()[2])
    if 'tomato' in item.lower():
        sum += int(buy_list[1].split()[2])
    if 'cola' in item.lower():
        sum += int(buy_list[2].split()[2])

    return sum

print(shopping_item("shopping_list.txt"))