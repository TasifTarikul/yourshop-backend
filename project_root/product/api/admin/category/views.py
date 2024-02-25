from rest_framework import viewsets

from project_root.product.models import Category
from .serializers import CategroySerializer

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategroySerializer
