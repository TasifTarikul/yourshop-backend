from rest_framework import serializers
from project_root.cart.models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem

