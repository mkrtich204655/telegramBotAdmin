from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('send_code/', views.send_code, name='send_code'),
    path('sign_in/', views.user_login, name='sign_in'),
    path('logout/', views.custom_logout, name='logout')
]