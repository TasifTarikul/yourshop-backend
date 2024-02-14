from django.db.models import ProtectedError
from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from project_root.product.models import Product

from .serializers import ProductSerializer, UpdateProductSerializer
from .filters import ProductFilter

class ProductView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_success_headers(self, data):
        # You can add custom headers here
        headers = super().get_success_headers(data)
        headers['Custom-Header'] = 'some value addeds'
        return headers

    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateProductSerializer
        return ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # notify admin
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     "notification_notification_admin",
        #     {
        #         'type': 'notify',
        #         "message": "product added"
        #     },
        # )
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except ProtectedError as exception:
            error = 'Cannot delete this product because it has variants associated with it - '
            error += '<br>'.join('Product Variant sku - ' + obj.sku 
                                 for obj in exception.protected_objects
                                 )
            
            data = {
                'code': 405,
                'message': _('Internal server error'),
                'error': error
            }
            return Response(data=data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        return Response(status=status.HTTP_204_NO_CONTENT)