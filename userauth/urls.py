from django.urls import path
from .views import AuthView

urlpatterns = [
    path('', AuthView.as_view({'get': 'index'}), name='login'),
    path('send_code', AuthView.as_view({'post': 'send_code'}), name='send_code'),
    path('sign_in', AuthView.as_view({'post': 'user_login'}), name='sign_in'),
    path('logout', AuthView.as_view({'get': 'custom_logout'}), name='logout'),
]