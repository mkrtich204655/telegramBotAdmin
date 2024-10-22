from django.contrib import admin
from django.urls import path, include
from userauth import urls as auth_urls
from users import urls as users_urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', include(auth_urls)),
    path('tuser/', include(users_urls)),
]
