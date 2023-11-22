import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json

with open('user_data3.json', 'r', encoding='utf-8') as file:
    existing_data = json.load(file)

new_data = [{'username': entry['fields']['username'],
             'financial_products': entry['fields']['financial_products'],
             'money': entry['fields']['money'],
             'salary': entry['fields']['salary'],
             'travel': entry['fields']['travel'],
             'married': entry['fields']['married']} for entry in existing_data]

df_existing = pd.DataFrame(new_data)

user_features_existing = df_existing[['money', 'salary', 'travel']]

similarities = cosine_similarity(user_features_existing)

new_user_data = {'username': '새로운사용자',
                 'financial_products': '10-047-1387-0001,10141109800021,010300100335,10-01-30-031-0018-0000',
                 'money': 80000000,
                 'salary': 150000000,
                 'travel': 2,
                 'married': False}

df_new_user = pd.DataFrame([new_user_data])

user_features_new_user = df_new_user[['money', 'salary', 'travel']]

user_features_combined = pd.concat([user_features_existing, user_features_new_user], ignore_index=True)

similarities_combined = cosine_similarity(user_features_combined)

similar_users_combined = similarities_combined[-1, :-1]  
similar_users_indices = similar_users_combined.argsort()[:-6:-1] 

# 결혼 여부와 돈이 같은 사용자들의 인덱스 찾기
target_user_married = new_user_data['married']
target_user_money = new_user_data['money']

similar_users_selected = [user for user in similar_users_indices if 
                          df_existing.loc[user, 'married'] == target_user_married and 
                          abs(df_existing.loc[user, 'money'] - target_user_money) <= 100000000000000]

# 새로운 사용자와 유사한 나이, 결혼 여부가 같고 돈이 비슷한 사용자들이 가입한 상품 출력
similar_users_products = df_existing.iloc[similar_users_selected]['financial_products']

# 상품을 하나의 리스트로 합침
all_products = [products.split(',') for products in similar_users_products]
all_products = [product for sublist in all_products for product in sublist]

# 중복 제거
unique_products = list(set(all_products))

# 결과 출력
# print("새로운 사용자와 유사한 나이, 결혼 여부가 같고 돈이 비슷한 사용자들이 가입한 상품:")
# print(unique_products)

response_data = {'recommended_products': unique_products}
json_response = json.dumps(response_data, ensure_ascii=False)
print(json_response)
