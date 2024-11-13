from django.shortcuts import redirect
from django.urls import reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        first_path_segment = request.path.strip('/').split('/')[0]
        if first_path_segment not in ['login', 'tuser', 'tcities', 'tride']:
            if not request.user.is_authenticated:
                return redirect('login')
        response = self.get_response(request)
        return response
