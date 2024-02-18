from rest_framework import viewsets

from project_root.product.models import ProductVariant
from .serializers import ProductVariantSerializer

class ProductVariantViewSet(viewsets.ModelViewSet):

    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer