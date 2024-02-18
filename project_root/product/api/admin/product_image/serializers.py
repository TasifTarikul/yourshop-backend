from rest_framework import serializers

from project_root.product.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','image', 'display_picture')