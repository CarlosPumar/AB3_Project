"""
ASGI config for ab3_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from .utils.threading import thread_is_active
import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from .twitter.routing import ws_urlpatterns
from .twitter.stream import Stream_Twitter
from .utils.data import *
from .channelsmiddleware import JwtAuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ab3_project.settings')

"""
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
"""

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            JwtAuthMiddlewareStack(
                URLRouter(ws_urlpatterns)
            ),
        ),
    }
)


if not thread_is_active('Tweepy Stream'):

    stream = Stream_Twitter(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                            access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    stream.filter(follow=[ID_ACCOUNT], threaded=True)
