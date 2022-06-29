from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from valley import consumer

websocket_urlPattern = [
    path('ws/pollData', consumer.DashConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern ))
})