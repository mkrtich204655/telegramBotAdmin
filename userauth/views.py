import json
import random

from asgiref.sync import async_to_sync
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
from users.views import getUserById
from telegram_bot.main import send_message


# Create your views here.
def index(request):
    return render(request, 'userauth/login.html')


def send_code(request):
    if request.method == 'POST':
        if request.POST['user_id'] is None or request.POST['user_id'] == '':
            return render(request, 'userauth/login.html', {'error': 'User Id is required'}, status=400)

        user = getUserById(request.POST['user_id'])
        if user is None:
            return render(request, 'userauth/login.html', {'error': 'User By ID Not Found'}, status=404)

        code = random.randint(100000, 999999)
        async_to_sync(send_message)(user.tuid, "Hi @" + user.username + ". Your One Time Password is: " + str(code))

        user.set_password(str(code))
        user.save()

        data = {
            'code_send': True,
            'user_id': request.POST['user_id']
        }
        return render(request, 'userauth/login.html', data)

    else:
        return render(request, 'userauth/login.html')


def user_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('OTP')

        if not user_id or not password:
            return render(request, 'userauth/login.html', {'error': 'User ID and password are required'}, status=400)

        try:
            user = CustomUser.objects.get(uuid=user_id)
        except CustomUser.DoesNotExist:
            return render(request, 'userauth/login.html', {'error': 'Invalid User ID'}, status=404)

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'userauth/login.html', {'error': 'Invalid credentials'}, status=400)
    else:
        return render(request, 'userauth/login.html')


def custom_logout(request):
    logout(request)
    return render(request, 'userauth/login.html')
