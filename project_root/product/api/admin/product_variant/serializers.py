from rest_framework import serializers

from project_root.product.models import ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('id','price', 'qty', 'sku', 'description', 'color', 'category_attribute_value')