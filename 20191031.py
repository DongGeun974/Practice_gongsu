
about_python = """
Python is a general-purpose programming Language. It is becoming more and more
popular for doing data science.
"""

#단어길이
words = about_python.split()
print(words)

print([(x.strip(".").upper(), len(x.strip("."))) for x in words][:5])
print([(words[n].strip(".").upper(), len(words[n].strip("."))) \
        for n in range(len(words)) if n <5])



#####################################자료#######################################
"""
자료 - 수치자료(양적자료), 범주형자료(질적자료)
1. 양적자료 또는 수치자료
 1.1 연속형 자료 예) 키, 몸무게 등
 1.2 이산형 자료 예) 자동차의 수
2. 질적자료 또는 범주형자료
 2.1 순위형 자료 예) 선호도조사, 평점
 2.2 명목형 자료 예) 성별, 혈액형
 
데이터 시각화
1 선그래프 - 추세, 변화 확인, 양적자료에 많이 쓰임
2 막대그래프 - 비교할때, 범주형자료에 많이 쓰임
3 히스토그램 - 비교할때, 붙어있음, 막대그래프와 차이?? 
4 원그래프 - 파이차트, 비율확인
5 산점도 - 점, 두개의 관계가 있는지 없는지 확인
"""


import matplotlib.pyplot as plt

data_f = open("Seoul_pop1.csv")

#선그래프 - 추세확인
years = []
populations = []
for line in data_f:
    year, population = line.split(",")
    years.append(int(year))
    populations.append(int(population))

data_f.close()
print(years)
print(populations)

fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)

plt.plot(years, populations, color = "green", marker = "o", linestyle = "solid")
plt.title("Seoul Population Change")
plt.ylabel("10Million")
plt.show()

#막대그래프 - 범주형자료 크기 비교
sport = ['Archery', 'Badminton','Boxing', 'Teakwondo', 'Wrestling']
medals = [39, 19, 20, 43, 19]

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)

plt.bar(sport, medals)
plt.ylabel("Medal")
plt.title("Olympic Medals")
plt.show()


#막대그래프 수치 확인

fig3 = plt.figure()
ax3 = fig3.add_subplot(1,1,1)

memtions = [500, 505]
years = [2013, 2014]

plt.bar(years, memtions)
plt.xticks(years) #x축 끊음
plt.axis([2012.5, 2014.5, 499, 506])#차이가 크게 하기위해서 씀
plt.show()


#원그래프 - 비율
fig4 = plt.figure()
ax4 = fig4.add_subplot(1,1,1)

label = ['Blue', 'Green', 'Red', 'Yellow']
x = [30, 50, 20, 40]

explode = [0,0,0,0.3] #빼내다

plt.pie(x, autopct="%1.1f%%", shadow=True, colors= label,\
        labels=label, explode=explode) #autopct자동으로 퍼센트를 만들어줌
plt.show()


#히스토그램 - 연속된막대그래프
import numpy as np

fig5 = plt.figure()
ax5 = fig5.add_subplot(1,1,1)

gaussian_numbers = np.random.randn(1000) #정규분포
plt.hist(gaussian_numbers, bins= 10)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


#산점도 - 두개의 관계를 확인, 전처리할때 쓰임
fig6 = plt.figure()
ax6 = fig6.add_subplot(1,1,1)

#핸드폰에 저장된 친구의 수와 핸드폰 사용시간
num_friends = [41, 26, 90, 50, 18, 124, 88, 72, 51, 3]
phone_time = [4.1, 3.3, 5.7, 4.2, 3.2, 6.4, 6.0, 5.1, 6.2, 3.7]

plt.scatter(num_friends, phone_time)
plt.show()


"""
상관관계와 인과관계(원인,결과)
산점도를 통해 인과관계를 알 수는 없다.
"""