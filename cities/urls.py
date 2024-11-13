from django.urls import path
from cities.views import CitiesView

urlpatterns = [
    path('', CitiesView.as_view({'get': 'index'}), name='cities'),
]
