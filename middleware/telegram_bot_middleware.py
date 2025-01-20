import os
import json
from django.http import JsonResponse
from telegram_bot.encode import encrypt_json
from telegram_bot.decode import decrypt_json


class TBTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        first_path_segment = request.path.strip('/').split('/')[0]
        if first_path_segment in ['tuser', 'tcities', 'tride']:
            token = request.META.get('TBTOKEN')
            if token is None or token != os.getenv('TBTOKEN'):
                return JsonResponse(encrypt_json({'data': 'Permission denied'}), status=501)

            try:
                if request.body:
                    dec_body = decrypt_json(json.loads(request.body))
                    request.dec_body = dec_body
            except (json.JSONDecodeError, TypeError) as e:
                return JsonResponse(encrypt_json({'data': 'Invalid request format'}), status=400)

        response = self.get_response(request)
        return response
