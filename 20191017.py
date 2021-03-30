""""""""""""""
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


import string #whitespace : 공백
def record_getter(filename):
    """
    지정된 학생의 신상정보를 리스트에 담아 리턴해주는 함수
    각 항목은 항목명과 내용의 튜플로 구성됨
    :param filename:
    :return:
    """
    std_data = {}
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

            std_data[item] = value

    return std_data

print(record_getter("Students_Records/Byun_Sato.txt"))
print(record_getter("Students_Records/Pi_Matgol.txt"))
print(record_getter("Students_Records/Byun_Sato.txt")['Department'])

#파일 리스트로 가져오기
import glob #주소?

def std_record_list(dir):
    file = glob.glob(dir + "/*.txt")
    return sorted(file)

filenames = std_record_list('Students_Records')

all_records = []

for file in filenames:
    data = record_getter(file)
    all_records.append(data)

print(all_records)
print(all_records[2]['Department'])
print(all_records[0]['Name'])

"""
문제 첫번째 학생의 신상 전보를 아래의 형식으로 출력하는 코드를 작성
제 이름은 ... 이고, 나이는 ...살 입니다.

전공이 컴퓨터인 학생 이름의 리스트를 구현

전공을 인자로 입력하면 해당 전공 학생들 이름으로 구성된 리스트
"""

print("제 이름은",all_records[0]['Name'], "이고, 나이는", str(2019 - all_records[0]['Date of Birth'][0] + 1), "입니다")

computer_name = []
for data in all_records:
    if 'Computer' in data['Department']:
        computer_name.append(data['Name'])
print(computer_name)

def department(depa):
    depa_name = []
    for data in all_records:
        if data['Department'] == depa:
            depa_name.append(data['Name'])
    return depa_name
print(department('Computer'))
print(department('Environment'))