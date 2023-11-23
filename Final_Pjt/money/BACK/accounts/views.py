from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import CustomRegisterSerializer, ItemSerializer, ProfileSerializer, ReadUserSerializer
import requests
from django.http import JsonResponse
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity



# Create your views here.
@api_view(['GET', 'PUT'])
def profile(request, username):
    if request.method == 'GET':
        oneprofile = User.objects.get(username=username)
        serializer = CustomRegisterSerializer(oneprofile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        user_profile = User.objects.get(username=username)
        new_financial_product = request.data.get('financial_products', None)
        if new_financial_product:
            if user_profile.financial_products:
                if new_financial_product not in user_profile.financial_products:
                    user_profile.financial_products += f',{new_financial_product}'
                    request.data['financial_products'] = user_profile.financial_products
                else:
                    before_products = user_profile.financial_products.split(',')
                    before_products.remove(new_financial_product)
                    after_products = ','.join(before_products)
                    
                    request.data['financial_products'] = after_products
            else:
                user_profile.financial_products = new_financial_product

            serializer = ItemSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            

@api_view(['PUT'])
def profile_edit(request, username):
    if request.method == 'PUT':
        oneprofile = User.objects.get(username=username)
        serializer = ProfileSerializer(oneprofile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def current_user(request, username):
    user = User.objects.get(username=username)
    serializer = ReadUserSerializer(user)
    return Response(serializer.data)



def recommend(request, username):
    print(request,1)
    existing_data = User.objects.values()
    # print(request,2)

    df_existing = pd.DataFrame(existing_data)
    # print(df_existing)
    
    user_features_existing = df_existing[['money', 'salary', 'travel']]
    # print(user_features_existing)
    new_user_ = User.objects.get(username=username)
    new_user_data = {
    'username': new_user_.username,
    'financial_products': new_user_.financial_products,
    'money': new_user_.money,
    'salary': new_user_.salary,
    'travel': new_user_.travel,
    'married': new_user_.married,
}
    # print(new_user_data)
    # new_user_data = ReadUserSerializer(new_user_)
    # print(new_user_data)
    df_new_user = pd.DataFrame([new_user_data])
    # print(df_new_user)

    user_features_new_user = df_new_user[['money', 'salary', 'travel']]
    
    # user_features_combined = pd.concat([user_features_existing, user_features_new_user], ignore_index=True)
    
    similarities_combined = cosine_similarity(user_features_existing)
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
    # json_response = json.dumps(response_data, ensure_ascii=False)
    # print(json_response)
    return JsonResponse(response_data, safe=False)