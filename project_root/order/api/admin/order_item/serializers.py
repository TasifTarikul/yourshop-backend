from rest_framework import serializers

from project_root.order.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

