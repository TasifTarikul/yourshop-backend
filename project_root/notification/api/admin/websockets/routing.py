from django.urls import path, re_path


from .consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/admin/(?P<room_name>\w+)/$', NotificationConsumer.as_asgi()), 
]