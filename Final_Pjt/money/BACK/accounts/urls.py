from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:username>/', views.profile),
    path('accounts/profile_edit/<str:username>/', views.profile_edit),
    path('user/<int:user_pk>/', views.article_user)
]
