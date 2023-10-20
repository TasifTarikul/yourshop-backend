from rest_framework.generics import ListAPIView
from project_root.product.models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer
from project_root.product.helpers import category_restructure

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        parent_categories = queryset.filter(parent=None)
        restructured_category = category_restructure(parent_categories, queryset)
        
        page = self.paginate_queryset(restructured_category)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(restructured_category, many=True)
        return Response(serializer.data)
