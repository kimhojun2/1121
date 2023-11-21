from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DepositProducts, DepositOptions, GeneralDepositOptions, GeneralDepositProducts
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, NestedSerialzer, GeneralDepositOptionsSerializer, GeneralDepositProductsSerializer, GeneralNestedSerialzer
import requests
from django.db.models import Max

API_KEY = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def save(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    
    response = requests.get(url).json()
    result = response['result']['baseList']
    
    for prod in result:
        save_product = {
            'fin_prdt_cd' : prod["fin_prdt_cd"],
            'kor_co_nm' : prod["kor_co_nm"],
            'fin_prdt_nm' : prod["fin_prdt_nm"],
            'join_deny' : prod["join_deny"],
            'etc_note' : prod["etc_note"],
            'join_member' : prod["join_member"],
            'join_way' : prod["join_way"],
            'spcl_cnd' : prod["spcl_cnd"],
        }
        serializer = DepositProductsSerializer(data=save_product)
        if serializer.is_valid(): 
            serializer.save()

    optionlist = response['result']["optionList"]
    for opt in optionlist:
        
        # try:
        #     product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
        # except:
        #     product = None

        save_option = {
        'fin_prdt_cd' : opt["fin_prdt_cd"],
        'intr_rate_type_nm' : opt["intr_rate_type_nm"],
        'intr_rate' : opt["intr_rate"],
        'intr_rate2' : opt["intr_rate2"],
        'save_trm' : opt["save_trm"],
        }
        serializer = DepositOptionsSerializer(data=save_option)
        if serializer.is_valid(): 
            product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
            serializer.save(product=product)
    

    # 여기부터 예금 저장
    url2 = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    
    response2 = requests.get(url2).json()
    result2 = response2['result']['baseList']
    
    for prod in result2:
        save_product2 = {
            'fin_prdt_cd' : prod["fin_prdt_cd"],
            'kor_co_nm' : prod["kor_co_nm"],
            'fin_prdt_nm' : prod["fin_prdt_nm"],
            'join_deny' : prod["join_deny"],
            'etc_note' : prod["etc_note"],
            'join_member' : prod["join_member"],
            'join_way' : prod["join_way"],
            'spcl_cnd' : prod["spcl_cnd"],
        }
        serializer2 = GeneralDepositProductsSerializer(data=save_product2)
        if serializer2.is_valid(): 
            serializer2.save()
            

    optionlist2 = response2['result']["optionList"]
    for opt in optionlist2:
        
        # try:
        #     product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
        # except:
        #     product = None

        save_option2 = {
        'fin_prdt_cd' : opt["fin_prdt_cd"],
        'intr_rate_type_nm' : opt["intr_rate_type_nm"],
        'intr_rate' : opt["intr_rate"],
        'intr_rate2' : opt["intr_rate2"],
        'save_trm' : opt["save_trm"],
        }
        serializer2 = GeneralDepositOptionsSerializer(data=save_option2)
        if serializer2.is_valid(): 
            save_product = GeneralDepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
            serializer2.save(product=save_product)
    




    return Response({'message' : 'okay'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    # 전체 정기 예금 상품 목록 반환
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        # products = DepositProducts.objects.all()
        # serializer = De(products)
        # serializer 자체는 객체라서 .data로 해서 보내줘야댐
        return Response(serializer.data)
    
    # 상품 데이터 저장
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(): # 참고 :form 에서 쓴거랑 다른거임! 이름만 똑같은거임!
            serializer.save() # 얘도 이름만 똑같은거
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    if request.method == 'GET':
        optionlist = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(optionlist, many=True)
        return Response(serializer.data)


# 여기부터 예금

@api_view(['GET', 'POST'])
def Generaldeposit_products(request):
    # 전체 정기 예금 상품 목록 반환
    if request.method == 'GET':
        products = GeneralDepositProducts.objects.all()
        serializer = GeneralDepositProductsSerializer(products, many=True)
        # products = DepositProducts.objects.all()
        # serializer = De(products)
        # serializer 자체는 객체라서 .data로 해서 보내줘야댐
        return Response(serializer.data)
    
    # 상품 데이터 저장
    elif request.method == 'POST':
        serializer = GeneralDepositProductsSerializer(data=request.data)
        if serializer.is_valid(): # 참고 :form 에서 쓴거랑 다른거임! 이름만 똑같은거임!
            serializer.save() # 얘도 이름만 똑같은거
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    if request.method == 'GET':
        optionlist = GeneralDepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = GeneralDepositOptionsSerializer(optionlist, many=True)
        return Response(serializer.data)
    


@api_view(['GET'])
def deposit_detail(request, fin_prdt_nm):
    if request.method == 'GET':
        onedeposit = GeneralDepositProducts.objects.get(fin_prdt_nm=fin_prdt_nm)
        serializer = GeneralDepositProductsSerializer(onedeposit)
        return Response(serializer.data)
    

@api_view(['GET'])
def saving_detail(request, fin_prdt_nm):
    if request.method == 'GET':
        onesaving = DepositProducts.objects.get(fin_prdt_nm=fin_prdt_nm)
        serializer = DepositProductsSerializer(onesaving)
        return Response(serializer.data)