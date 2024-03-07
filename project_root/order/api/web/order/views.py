from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from project_root.order.models import Order
from .serializers import CreateOrderSerializer

class CreateOrder(CreateAPIView):
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
