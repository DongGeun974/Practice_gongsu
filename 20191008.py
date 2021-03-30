
result_f = open("scores_list.txt", "r")
for line in result_f:
    """
    
    print(line.strip().split(" ")[1])
    """
    record = line.split()
    print(record[1])

result_f.close()

################################################################################

try:
    result_f = open("no_file.txt")
except:
    print("해당하는 파일이 없습니다")

#############################################################################################
result_f = open("scores_list.txt", "r")

highest_score = 0
second_highest_score = 0
third_highest_score = 0

for line in result_f:
    record = line.split()
    try:
        score = float(record[1])
    except:
        continue
    if highest_score < score:
        third_highest_score = second_highest_score
        second_highest_score = highest_score
        highest_score = score
    elif second_highest_score < score:
        third_highest_score = second_highest_score
        second_highest_score = score
    elif third_highest_score < score:
        third_highest_score = score
result_f.close()
print("1등의 점수",highest_score)
print("2등의 점수",second_highest_score)
print("3등의 점수",third_highest_score)

##########################################################################################

result_f = open("scores_list.txt", "r")
score_list = []
for line in result_f:
    name , score = line.split()
    try:
        score_list.append(float(score))
    except:
        continue
result_f.close()
score_list.sort()
score_list.reverse()
print(score_list)
print("1등", score_list[0])
print("3등", score_list[2])

def ranking(rank):
    result_f = open("scores_list.txt", "r")
    score_list = []
    for line in result_f:
        name, score = line.split()
        try:
            score_list.append(float(score))
        except:
            continue
    result_f.close()
    score_list.sort(reverse=True)
    return score_list[rank - 1]

print(ranking(1))
print(ranking(2))
##############################################################################

print([1, 2, 3] + [4, 5])
print([1, 2, 3] * 3)

#빈 리스트
empty_list = []

#리스트 길이
print(len(empty_list))

a_singleton =[[]]
print(len(a_singleton))

a_list = [1, 2, [3, 4], [[5, 6, 7], 8]]
# 2
print(a_list[1])
#[3, 4]
print(a_list[2])
#3
print(a_list[2][0])
#7
print(a_list[3][0][2])

animals = ['dog', 'cat', 'pig']
print(animals)
animals.append('coq')
print(animals)
animals.append(['eagle', 'bear'])
print(animals)
animals.remove(['eagle', 'bear'])
print(animals)
animals.extend(['eagle', 'bear'])
print(animals)
print("\n")
animals[1] = 'cow'
print(animals)
print(animals[1:4])
animals[1:2] =['tiger', 'lion', 'rabbit']
print(animals)
animals[1:2] = []
print(animals)

print(animals.index('pig'))
animals.pop(3)
print(animals)
animals.pop()
print(animals)

del animals[-1]
print(animals)

animals.insert(1, 'leopard')
print(animals)
print(animals.count('leopard'))










