from rest_framework import serializers
from project_root.cart.models import CartItem
from project_root.product.api.admin.product_variant.serializers import ProductVariantSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_variant = ProductVariantSerializer()
    class Meta:
        model=CartItem
        fields = '__all__'

