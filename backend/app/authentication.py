from rest_framework.authentication import BaseAuthentication
from app.models import Users
from app.jwt import decode_token


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]
        user_id = decode_token(token)

        if not user_id:
            return None

        try:
            user = Users.objects.get(pk=int(user_id))
            return (user, token)
        except Users.DoesNotExist:
            return None