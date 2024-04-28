from django_filters import rest_framework as filters

from project_root.product.models import Product

class ProductFilter(filters.FilterSet):
    category_attribute_value = filters.NumberFilter(field_name='product_variants__category_attribute_value')
    class Meta:
        model = Product
        fields = ['created_at', 'category', 'category_attribute_value', 'brand']