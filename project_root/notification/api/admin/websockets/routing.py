from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import NotificationConsumer

urlpatterns = [
    path('ws/<room_name>/', NotificationConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(urlpatterns),
})

