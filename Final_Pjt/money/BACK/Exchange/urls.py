from django.urls import path
from . import views

urlpatterns = [
    path('rate/', views.exchange_rate),
]
