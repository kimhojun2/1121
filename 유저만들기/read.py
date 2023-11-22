import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

# 기존 데이터가 JSON 파일에 저장되어 있다고 가정
with open('user_data3.json', 'r', encoding='utf-8') as file:
    existing_data = json.load(file)

# 새로운 형태로 데이터 구성
new_data = [{'username': entry['fields']['username'],
             'financial_products': entry['fields']['financial_products'],
             'money': entry['fields']['money'],
             'salary': entry['fields']['salary'],
             'travel': entry['fields']['travel'],
             'married': entry['fields']['married']} for entry in existing_data]

# 기존 데이터를 DataFrame으로 변환
df_existing = pd.DataFrame(new_data)

# 'money', 'salary', 'travel' 열을 이용하여 간단한 사용자 프로필 벡터 생성
user_features_existing = df_existing[['money', 'salary', 'travel']]

# 사용자 프로필 벡터 간의 코사인 유사도 계산
similarities = cosine_similarity(user_features_existing)

# 결과 출력
# print("코사인 유사도 행렬:")
# print(pd.DataFrame(similarities, index=df_existing['username'], columns=df_existing['username']))

# 새로운 사용자 데이터
new_user_data = {'username': '새로운사용자',
                 'financial_products': '10-047-1387-0001,10141109800021,010300100335,10-01-30-031-0018-0000',
                 'money': 80000000,
                 'salary': 150000000,
                 'travel': 2,
                 'married': False}

# 새로운 사용자를 DataFrame에 추가
df_new_user = pd.DataFrame([new_user_data])

# 'money', 'salary', 'travel' 열을 이용하여 새로운 사용자의 프로필 벡터 생성
user_features_new_user = df_new_user[['money', 'salary', 'travel']]

# 기존 사용자의 프로필 벡터와 새로운 사용자의 프로필 벡터를 합쳐 전체 사용자의 프로필 벡터 생성
user_features_combined = pd.concat([user_features_existing, user_features_new_user], ignore_index=True)

# 전체 사용자의 프로필 벡터 간의 코사인 유사도 계산
similarities_combined = cosine_similarity(user_features_combined)

# 새로운 사용자와 유사한 나이의 사용자들을 출력
similar_users_combined = similarities_combined[-1, :-1]  # 마지막 행(새로운 사용자)과 다른 행들 간의 유사도
similar_users_indices = similar_users_combined.argsort()[:-6:-1]  # 상위 5개 유저의 인덱스

# 결과 출력
print("새로운 사용자와 유사한 나이의 사용자들:")
print(df_existing.iloc[similar_users_indices])

# 새로운 사용자와 유사한 나이의 사용자들이 가입한 상품 출력
similar_users_products = df_existing.iloc[similar_users_indices]['financial_products']

# 상품을 하나의 리스트로 합침
all_products = [products.split(',') for products in similar_users_products]
all_products = [product for sublist in all_products for product in sublist]

# 중복 제거
unique_products = list(set(all_products))

# 결과 출력
print("새로운 사용자와 유사한 나이의 사용자들이 가입한 상품:")
print(unique_products)


