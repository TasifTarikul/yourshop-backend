from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from project_root.product.models import CategoryAttribute
from .serializers import CategoryAttributeSerializer, ListCategoryAttributeSerializer

class CategoryAttributeViewSet(viewsets.ModelViewSet):
    queryset = CategoryAttribute.objects.all()
    serializer_class = CategoryAttributeSerializer

class CategoryAttributeListView(ListAPIView):
    queryset = CategoryAttribute.objects.all()
    serializer_class = ListCategoryAttributeSerializer
    filterset_fields = ['category']