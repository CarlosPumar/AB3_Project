from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from django.db import close_old_connections
from jwt import decode as jwt_decode
from django.conf import settings
from rest_framework.authtoken.models import Token


@database_sync_to_async
def get_user(user_id):
    try:
        user = get_user_model().objects.get(id=user_id)
        return user
    except:
        return AnonymousUser()


class JwtAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
       # Close old database connections to prevent usage of timed out connections

        close_old_connections()

        try:
            token_key = scope['query_string'].decode().split('=')[-1]
            UntypedToken(token_key)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            print(e)
            scope['user'] = AnonymousUser()
        else:
            decoded_data = jwt_decode(
                token_key, settings.SECRET_KEY, algorithms=["HS256"])

            scope['user'] = await get_user(decoded_data['user_id'])

        return await super().__call__(scope, receive, send)


def JwtAuthMiddlewareStack(inner):
    return JwtAuthMiddleware(AuthMiddlewareStack(inner))
