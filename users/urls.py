from django.urls import path
from .views_folder import cars_views

urlpatterns = [
    path('cars', cars_views.index, name='get_cars'),
    path('cars/edit', cars_views.editCars, name='edit_car'),
]