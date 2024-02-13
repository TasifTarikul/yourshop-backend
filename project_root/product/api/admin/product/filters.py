from django_filters import rest_framework as filters

from project_root.product.models import Product

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['created_at', 'category']