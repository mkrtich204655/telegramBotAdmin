from django.contrib import admin
from django.urls import path, include
from userauth import urls as auth_urls
from dashboard import urls as dashboard_urls
from users import urls as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(dashboard_urls)),
    path('login/', include(auth_urls)),
    path('tuser/', include(users_urls)),
]
