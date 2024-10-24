from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from users.serializers_folder.car_serializer import CarSerializer

from users.models import Cars


def index(request):
    cars = getCars(request.user.id)
    result = CarSerializer(cars, many=True).data
    return render(request, 'cars/index.html', {'cars': result})


def getCars(user_id):
    try:
        cars = Cars.objects.filter(user_id=user_id).all()
    except Cars.DoesNotExist:
        cars = None
    return cars


def editCars(request):
    try:
        car = Cars.objects.first(id=request.GET['car_id'], user_id=request.user.id)
    except Cars.DoesNotExist:
        messages.error(request, 'Cars does not exist')
        redirect(reverse('get_cars'))
    else:
        result = CarSerializer(car).data
        render(request, 'cars/manage.html', {'car': result})


def createCar(request):
    pass
