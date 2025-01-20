from django.contrib import admin
from django.urls import path, include
from userauth import urls as auth_urls
from users import api_urls as users_api_urls
from .views import BaseView
from cities import urls as cities_urls
from ride import api_urls as rides_urls

urlpatterns = [
    path('', BaseView.as_view({'get': 'index'}), name='index'),
    path('cars/', BaseView.as_view({'get': 'cars'}), name='cars'),
    path('rides/', BaseView.as_view({'get': 'rides'}), name='rides'),
    path('bookings/', BaseView.as_view({'get': 'bookings'}), name='bookings'),
    path('admin/', admin.site.urls),
    path('login/', include(auth_urls)),
    path('tuser/', include(users_api_urls)),
    path('tcities/', include(cities_urls)),
    path('tride/', include(rides_urls)),
]
