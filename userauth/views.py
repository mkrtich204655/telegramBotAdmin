import json
import random

from asgiref.sync import async_to_sync
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from userauth.serializers_folder.auth_serializer import AuthSerializerSendCode, AuthSerializerAuth
from users.models import CustomUser
from telegram_bot.main import send_message
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'userauth/login.html')


def send_code(request):
    if request.method == 'POST':
        serializer = AuthSerializerSendCode(data=request.POST)
        if serializer.is_valid():
            validate_data = serializer.validated_data

            try:
                user = CustomUser.objects.get(uuid=validate_data['user_id'])
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid User ID')
                return redirect(reverse('login'))

            code = random.randint(100000, 999999)
            try:
                async_to_sync(send_message)(user.tuid, "Hi @" + user.username + ". Your One Time Password is: " + str(code), None)
            except Exception:
                messages.error(request, 'Something went wrong, please try later')
                return redirect(reverse('login'))

            user.set_password(str(code))
            user.save()

            result = AuthSerializerAuth(user).data
            result['code_send'] = True

            return render(request, 'userauth/login.html', result)
        for field, error in serializer.errors.items():
            messages.error(request, f"{''.join(error)}")
        return redirect(reverse('login'))
    else:
        return redirect(reverse('login'))


def user_login(request):
    if request.method == 'POST':
        serializer = AuthSerializerAuth(data=request.POST)
        if serializer.is_valid():
            data = serializer.validated_data
            user_id = data['user_id']
            password = data['OTP']

            try:
                user = CustomUser.objects.get(uuid=user_id)
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid User ID')
                return redirect(reverse('login'))

            authenticate_user = authenticate(request, username=user.username, password=password)

            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect(reverse('login'))
        for field, error in serializer.errors.items():
            messages.error(request, f"{''.join(error)}")
        return redirect(reverse('login'))
    else:
        return redirect(reverse('login'))


def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))
