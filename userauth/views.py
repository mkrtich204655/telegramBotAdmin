import random
from django.contrib.auth.hashers import check_password
from asgiref.sync import async_to_sync
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from rest_framework.viewsets import ViewSet

from userauth.serializers_folder.auth_serializer import AuthSerializerSendCode, AuthSerializerAuth
from users.services.user_service import UserService
from telegram_bot.main import send_message
from django.urls import reverse
from django.contrib import messages


class AuthView(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService()

    def index(self, request):
        return render(request, 'userauth/login.html')

    def send_code(self, request):
        serializer = AuthSerializerSendCode(data=request.POST)
        print(request.POST)
        if serializer.is_valid():
            validate_data = serializer.validated_data
            user = self.service.get_user_by_uuid(validate_data['uuid'])
            if user is None:
                messages.error(request, 'Invalid User UUID')
                return redirect(reverse('login'))
            print(user)

            code = random.randint(100000, 999999)
            try:
                async_to_sync(send_message)(user.tuid, "Hi. Your One Time Password is: " + str(code), None)
            except Exception as e:
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

    def user_login(self, request):
        serializer = AuthSerializerAuth(data=request.POST)
        if serializer.is_valid():
            data = serializer.validated_data
            user_id = data['uuid']
            password = data['password']

            user = self.service.get_user_by_uuid(user_id)
            if user is None:
                messages.error(request, 'Invalid User ID')
                return redirect(reverse('login'))

            if check_password(password, user.password):
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect(reverse('login'))
        for field, error in serializer.errors.items():
            messages.error(request, f"{''.join(error)}")
        return redirect(reverse('login'))

    def custom_logout(self, request):
        logout(request)
        return redirect(reverse('login'))
