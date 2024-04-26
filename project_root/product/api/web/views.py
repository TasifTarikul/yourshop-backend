from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from project_root.product.models import Category, CategoryAttribute
from .serializers import ListCategorySerializer
from project_root.product.helpers import category_restructure_in_parent_child_format

class CategoryListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        parent_categories = queryset.filter(parent=None)
        restructured_category = category_restructure_in_parent_child_format(parent_categories, queryset)
        
        page = self.paginate_queryset(restructured_category)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(restructured_category, many=True)
        return Response(serializer.data)
    

