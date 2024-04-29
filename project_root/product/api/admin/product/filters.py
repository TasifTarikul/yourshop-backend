from django_filters import rest_framework as filters

from project_root.product.models import Product

class ProductFilter(filters.FilterSet):
    category_attribute_value = filters.NumberFilter(field_name='product_variants__category_attribute_value')
    price = filters.NumberFilter(field_name='product_variants__price', distinct=True)
    min = filters.NumberFilter(field_name='product_variants__price', lookup_expr='gte', distinct=True)
    max = filters.NumberFilter(field_name='product_variants__price', lookup_expr='lte', distinct=True)
    class Meta:
        model = Product
        fields = ['created_at', 'category', 'brand']