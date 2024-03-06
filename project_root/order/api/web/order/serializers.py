from project_root.order.api.admin.order.serializers import OrderSerializer
from project_root.order.api.admin.order_item.serializers import OrderItemSerializer


class CustomOrderItemSerializer(OrderItemSerializer):
    class Meta:
        model=OrderItemSerializer.Meta.model
        fields = ('product_variant', 'qty', 'price')

class CreateOrderSerializer(OrderSerializer):
    order_items = CustomOrderItemSerializer(many=True)
    
    class Meta:
        model = OrderSerializer.Meta.model
        fields = ('total_price', 'address', 'order_items')