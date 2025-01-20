from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.template.loader import render_to_string
from users.serializers_folder.user_serializer import UserSerializer
from users.services.user_service import UserService
from django.http import JsonResponse


class BaseView(ViewSet):

    def __init__(self, ):
        super().__init__()
        self.userService = UserService()
        self.userSerialize = UserSerializer
        self.view = 'dashboard/index.html'

    def index(self, request):
        return render(
            request,
            self.view,
            UserSerializer(self.userService.get_user_with_relation(request.user.id)).data)

    def cars(self, request):
        cars = self.userService.get_user_with_relation(request.user.id).cars.all()
        component_html = render_to_string('dashboard/cars_component.html', {'items': cars})
        return JsonResponse({'html': component_html})

    def rides(self, request):
        rides = self.userService.get_user_with_relation(request.user.id).user.all()
        component_html = render_to_string('dashboard/rides_component.html', {'items': rides})
        return JsonResponse({'html': component_html})

    def bookings(self, request):
        bookings = self.userService.get_user_with_relation(request.user.id).passenger.all()
        component_html = render_to_string('dashboard/bookings_component.html', {'items': bookings})
        return JsonResponse({'html': component_html})
