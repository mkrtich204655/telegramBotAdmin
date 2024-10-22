import os

from django.http import JsonResponse
from django.urls import reverse

class TBTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        first_path_segment = request.path.strip('/').split('/')[0]
        if first_path_segment in ['tuser']:
            token = request.META.get('TBTOKEN')
            if token is None or token != os.getenv('TBTOKEN'):
                return JsonResponse({'data': 'Permission denied'}, status=501)

        response = self.get_response(request)
        return response
