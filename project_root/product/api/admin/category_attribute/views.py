from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from .filters import CategoryAttributeFilter

from project_root.product.models import CategoryAttribute
from .serializers import CategoryAttributeSerializer, ListCategoryAttributeSerializer

class CategoryAttributeViewSet(viewsets.ModelViewSet):
    queryset = CategoryAttribute.objects.all()
    serializer_class = CategoryAttributeSerializer

class CategoryAttributeListView(ListAPIView):
    queryset = CategoryAttribute.objects.all()
    serializer_class = ListCategoryAttributeSerializer
    filterset_class = CategoryAttributeFilter
    # filterset_fields = ['category']

    def list(self, queryset, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)