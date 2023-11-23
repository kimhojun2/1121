from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# 전체 데이터
data = {
    'money': [70000000, 86800000, 99200000, 66600000, 92600000, 41500000, 12333123, 124213214, 12312323, 123213132],
    'salary': [195000000, 116000000, 278000000, 504000000, 1342000000, 1036000000, 123213213123, 123132, 41221124, 14155555],
    'travel': [3.0, 3.0, 2.0, 1.0, 3.0, 0.0, 3.0, 0.0, 4.0, 0.0],
    'married': [True, True, False, False, False, False, True, True, True, True]
}

df = pd.DataFrame(data)

# 하나의 데이터
new_user_data = {
    'money': 124213214,
    'salary': 123132,
    'travel': 0.0,
    'married': True
}

df_new_user = pd.DataFrame([new_user_data])

# 두 벡터 간의 코사인 유사도 계산
user_features_combined = pd.concat([df, df_new_user], ignore_index=True)
similarities_combined = cosine_similarity(user_features_combined)
similarities_new_user = similarities_combined[-1, :-1]

# 특정 조건을 만족하는 상위 5명의 데이터 인덱스 찾기
target_users_selected = similarities_new_user.argsort()[-5:][::-1]

# 특정 조건을 만족하는 상위 5명의 데이터 출력
top_5_similar_users = df.iloc[target_users_selected]

print(top_5_similar_users)


# 특정 조건을 만족하는 상위 5명의 데이터 인덱스 찾기
target_users_selected = [index for index, similarity in sorted(enumerate(similarities_new_user), key=lambda x: x[1], reverse=True) if
                          df.loc[index, 'married'] == new_user_data['married'] and
                          df.loc[index, 'travel'] == new_user_data['travel']][:5]

# 특정 조건을 만족하는 상위 5명의 데이터 출력
top_5_similar_users = df.iloc[target_users_selected]

print(top_5_similar_users)

