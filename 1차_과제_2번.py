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


print(shopping_total_sum("shopping_list.txt"))
