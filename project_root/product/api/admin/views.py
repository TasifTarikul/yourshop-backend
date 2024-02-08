from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .serializers import AddProductSerializer

class AddProductView(CreateAPIView):
    serializer_class = AddProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # notify admin
        print('notify')
        channel_layer = get_channel_layer()
        print(f"channel_layer in view {channel_layer}")
        async_to_sync(channel_layer.group_send)(
            "notification_notification_admin",
            {
                'type': 'notify',
                "message": "product added"
            },
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
