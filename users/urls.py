from django.urls import path
from . import views

urlpatterns = [
    path('get', views.getUserByTUID, name='get_user_t'),
]