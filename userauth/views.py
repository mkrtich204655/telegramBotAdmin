import json
import random

from asgiref.sync import async_to_sync
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from users.views import getUserById
from telegram_bot.main import send_message
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'userauth/login.html')


def send_code(request):
    if request.method == 'POST':
        if request.POST['user_id'] is None or request.POST['user_id'] == '':
            messages.error(request, 'User Id is required')
            return redirect(reverse('login'))

        user = getUserById(request.POST['user_id'])
        if user is None:
            messages.error(request, 'User By ID Not Found')
            return redirect(reverse('login'))

        code = random.randint(100000, 999999)
        async_to_sync(send_message)(user.tuid, "Hi @" + user.username + ". Your One Time Password is: " + str(code), None)

        user.set_password(str(code))
        user.save()

        data = {
            'code_send': True,
            'user_id': request.POST['user_id']
        }
        return render(request, 'userauth/login.html', data)

    else:
        return redirect(reverse('login'))


def user_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('OTP')

        if not user_id or not password:
            messages.error(request, 'User ID and password are required')
            return redirect(reverse('login'))

        try:
            user = CustomUser.objects.get(uuid=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid User ID')
            return redirect(reverse('login'))

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(reverse('login'))
    else:
        return redirect(reverse('login'))


def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))
