from django.shortcuts import render

from users.serializers_folder.user_serializer import UserSerializer
from users.services.user_service import UserService


class BaseView:

    def __init__(self, request):
        self.request = request
        self.userService = UserService()
        self.userSerialize = UserSerializer
        self.view = 'dashboard/index.html'

    def index(self, request):
        return render(
            request,
            self.view,
            UserSerializer(self.userService.get_user_with_relation(request.user.id)).data)
