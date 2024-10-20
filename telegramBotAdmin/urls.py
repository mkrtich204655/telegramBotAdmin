from django.contrib import admin
from django.urls import path, include
from userauth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include(urls)),
]
