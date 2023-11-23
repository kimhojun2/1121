from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:username>/', views.profile),
    path('accounts/profile_edit/<str:username>/', views.profile_edit),
    path('user/<str:username>/', views.current_user),
    path('recommend/<str:username>/', views.recommend),
]
