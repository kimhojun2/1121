from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import CustomRegisterSerializer, ItemSerializer
import requests


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

           
        