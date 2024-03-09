from django.db import transaction

from project_root.order.api.admin.order.serializers import OrderSerializer
from project_root.order.api.admin.order_item.serializers import OrderItemSerializer
from project_root.order.helpers import generate_order_id

from project_root.order.models import Order, OrderItem
from project_root.coreapp.models import User

class CustomOrderItemSerializer(OrderItemSerializer):
    class Meta:
        model=OrderItemSerializer.Meta.model
        fields = ('product_variant', 'qty', 'price')

class CreateOrderSerializer(OrderSerializer):
    order_items = CustomOrderItemSerializer(many=True)
    
    class Meta:
        model = OrderSerializer.Meta.model
        fields = ('total_price', 'address', 'order_items')

    def create_order_item(sef, order_object, order_item_list):
        for order_item in order_item_list:
            order_item_object = OrderItem()
            order_item_object.order = order_object
            order_item_object.product_variant = order_item['product_variant']
            order_item_object.qty = order_item['qty']
            order_item_object.price = order_item['price']
            order_item_object.save()
        return

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request', None)
        order_object = Order()
        order_object.user = request.user.id
        order_object.order_number = generate_order_id()
        order_object.total_price = validated_data['total_price']
        order_object.address = validated_data['address']
        order_object.save()
        self.create_order_item(order_object, validated_data['order_items'])
        return order_object

