"""
#2차 과제
#학번 : 2016250056
#이름 : 황동근
#작성일 : 20191126
"""

import pandas as pd
users = pd.read_table('user.txt', sep = '|', index_col = 'user_id')

df = pd.DataFrame(users)

"""
1. 데이터의 개수를 확인하세요.
"""
print(df)
print(df.info()) #1. 943개

"""
2. 데이터프레임의 앞의 5개와 뒤의 5개의 행을 확인하세요.
"""
print("\n\n")
print(df.head(5)) #2. 앞의 5개의 행
print(df.tail(5)) #2. 뒤의 5개의 행

"""
3. users라는 데이터프레임의 occupation과 age 열만을 포함하는 데이터프레임을 만들고,
    이를 users_age에 할당하세요.
"""
print("\n\n")
users_age = df[['occupation', 'age']]
users_age = pd.DataFrame(users_age) #3. occupation과 age 열만을 포함하는 데이터프레임 만듦, user_age에 할당
print(users_age)

"""
4. users_age의 앞의 5개의 행을 확인하세요.
"""
print("\n\n")
print(users_age.head()) #4. users_age의 앞의 5개의 행

"""
5. 직업(occupation) 별 나이에 대한 사분위수를 이용한 이상치처리를 하세요.
    이때, users_age에는 Lower, Upper, Outlier 열이 추가되어야 합니다.
"""
print("\n\n")
_group = users_age.groupby(['occupation'])

#5. Lower열 추가
users_age['Lower'] = _group['age'].transform( \
    lambda x: x.quantile(.25) - 1.5 * ( \
                x.quantile(.75) - x.quantile(.25)))
#5. Upper열 추가
users_age['Upper'] = _group['age'].transform( \
    lambda x: x.quantile(.75) + 1.5 * ( \
                x.quantile(.75) - x.quantile(.25)))
#5. Outlier열 추가
users_age['Outlier'] = ((users_age['age'] < users_age.Lower) | (users_age.age > users_age.Upper))

print(users_age.head()) #5. 이상치처리

"""
6. 이상치가 몇 개 있는지 확인하세요.
"""
print("\n\n")
users_age_outlier = users_age[users_age.Outlier == True]
print(users_age_outlier.info()) #6. 14개

"""
7. 이상치의 값들을 각 직업별 중앙값(median)으로 변경하세요.
"""
print("\n\n")
#이상치 처리 전
mask = users_age['Outlier'] == True
print(users_age[mask])

#median열 추가
users_age['median'] = _group['age'].transform(lambda x: x.quantile(.5))

#이상치의 값들을 median으로 변경 
users_age['age'][mask] = users_age['median']

#이상치 처리
users_age['Outlier'] = False

#이상치 처리 후
users_age_outlier = users_age[users_age.Outlier == True]
print(users_age[mask])
