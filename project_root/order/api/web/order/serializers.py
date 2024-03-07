from django.db import transaction

from project_root.order.api.admin.order.serializers import OrderSerializer
from project_root.order.api.admin.order_item.serializers import OrderItemSerializer
from project_root.order.helpers import generate_order_id


class CustomOrderItemSerializer(OrderItemSerializer):
    class Meta:
        model=OrderItemSerializer.Meta.model
        fields = ('product_variant', 'qty', 'price')

class CreateOrderSerializer(OrderSerializer):
    order_items = CustomOrderItemSerializer(many=True)
    
    class Meta:
        model = OrderSerializer.Meta.model
        fields = ('total_price', 'address', 'order_items')

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request', None)
        order_object = OrderItemSerializer.Meta.model()
        order_object.user = request.user
        order_object.order_number = generate_order_id()
        order_object.total_price = validated_data['total_price']
        order_object.address = validated_data['address']

