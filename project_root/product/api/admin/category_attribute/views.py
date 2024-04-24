from rest_framework import viewsets

from project_root.product.models import CategoryAttribute
from .serializers import CategoryAttributeSerializer

class CategoryAttributeViewSet(viewsets.ModelViewSet):
    queryset = CategoryAttribute.objects.all()
    serializer_class = CategoryAttributeSerializer