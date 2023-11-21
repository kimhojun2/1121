from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:username>/', views.profile),
]
