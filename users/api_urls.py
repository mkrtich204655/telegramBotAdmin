from django.urls import path
from .views_folder.user_views import UserView
from .views_folder.cars_views import CarView

urlpatterns = [
    path('get', UserView.as_view({'post': 'get_user_by_TUID'}), name='get_user_by_tuid'),
    path('cars/create', CarView.as_view({'post': 'create_car'}), name='create_car'),
    path('cars', CarView.as_view({'post': 'get_cars'}), name='get_car'),
]