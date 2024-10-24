from django.shortcuts import render
from users.views import getUserWithRelation


def index(request):
    data = getUserWithRelation(request.user.id)
    return render(request, 'dashboard/index.html', data)
