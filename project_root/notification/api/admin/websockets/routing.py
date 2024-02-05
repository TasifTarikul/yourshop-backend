from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path('ws/admin/notification/', NotificationConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})

