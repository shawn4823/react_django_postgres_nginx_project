import jwt
from datetime import datetime, timedelta
from django.conf import settings

SECRET = settings.SECRET_KEY


def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        print("TOKEN EXPIRED")
        return None
    except jwt.InvalidTokenError as e:
        print("INVALID TOKEN:", e)
        return None