from django.shortcuts import render

from users.models import CustomUser

# Create your views here.

def getUserById(uuid):
    user = CustomUser.objects.get(uuid=uuid) or None
    return user
