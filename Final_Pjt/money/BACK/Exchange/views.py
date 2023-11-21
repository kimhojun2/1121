from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
import requests
import json
# Create your views here.

@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        api = 'r2L3MOeBhzmCs0W9Ismk0LcWtpageXlH'
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        params = {
            'authkey' : api,
            'data' : 'AP01',
            'searchdate' : '20231117'
        }
        response = requests.get(url, params=params)
        json_data = response.json()
        return Response(json_data)