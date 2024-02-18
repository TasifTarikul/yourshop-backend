from rest_framework import viewsets

from project_root.product.models import Attribute
from .serializers import AttributeSerializer

class AttributeViewSet(viewsets.ModelViewSet):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer