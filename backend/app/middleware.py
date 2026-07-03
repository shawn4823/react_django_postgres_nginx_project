from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from .authentication import JWTAuthentication

User = get_user_model()

class SimpleJWTMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = AnonymousUser()

        auth = JWTAuthentication()
        result = auth.authenticate(request)

        if result:
            request.user, _ = result

        return self.get_response(request)