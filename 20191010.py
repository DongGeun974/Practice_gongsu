#key랑 value
city_temperature = {'Peongteak' : 22, 'Suwon' : 18, 'Jeju' : 25, 'Anseong' : 21, 'Yongin': 23}
print(city_temperature.keys())
print(city_temperature.values())
print(city_temperature.items())

for key in city_temperature.keys():
    print(key, "의 온도는 ", city_temperature[key])

for key in city_temperature:
    print(key, "의 온도는 ", city_temperature[key])

city_temperature.pop('Suwon')
print(city_temperature.keys())

###############################################################################
listFile = open("scores_list.txt", "r")
score_dict = {}
for line in listFile:
    name, score = line.split()
    try:
        score_dict[float(score)] = name
    except:
        continue
listFile.close()
print(score_dict)
ordered_list = sorted(score_dict.keys(), reverse=True)
print(ordered_list)
i = 1
for score in ordered_list:
    print(i, "등", score_dict[score], "의 점수는", score)
    i += 1
    if i == 4:
        break

print("")
for i in range(1,len(ordered_list)+1):
    print(i, "등", score_dict[ordered_list[i-1]], "의 점수는", ordered_list[i-1])

"""
for key in sorted(score_dict.keys(), reverse=True):
    print(score_dict[key], ":", key)
"""
"""
등수까지 출력
3등까지 출력
일정 이상 점수의 점수와 선수만 출력
"""
print("")
for key in ordered_list:
    if float(key) > 21.8:
        print(score_dict[key], ":", key)

#max와 min함수 사용할 것
print("1등과 꼴등의 점수차", ordered_list[0],ordered_list[len(ordered_list) - 1],ordered_list[0]-ordered_list[len(ordered_list) - 1])