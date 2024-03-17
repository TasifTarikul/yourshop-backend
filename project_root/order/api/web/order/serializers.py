from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import serializers

from project_root.order.api.admin.order.serializers import OrderSerializer
from project_root.order.api.admin.order_item.serializers import OrderItemSerializer
from project_root.cart.api.web.serializers import CartItemSerializer
from project_root.order.helpers import generate_order_id
from project_root.order.models import Order, OrderItem
from project_root.account.models import Address
from project_root.product.models import ProductVariant
from project_root.coreapp.models import User

class  CustomCartItemSerializer(CartItemSerializer):
    class Meta:
        model=CartItemSerializer.Meta.model
        fields=('id',)

class CustomOrderItemSerializer(OrderItemSerializer):
    class Meta:
        model=OrderItemSerializer.Meta.model
        fields = ('product_variant', 'qty', 'price')

class CreateOrderSerializer(serializers.ModelSerializer):
    order_items = CustomOrderItemSerializer(many=True)
    cart_items = serializers.ListField(child=serializers.PrimaryKeyRelatedField(
        queryset=CartItemSerializer.Meta.model.objects.all()), write_only=True
        )

    class Meta:
        model = OrderSerializer.Meta.model
        fields = ('total_price', 'address', 'cart_items', 'order_items')
        
    
    def delete_cart_items(self, cart_item_list):
        for cart_item in cart_item_list:
            cart_item.delete()
        return

    def create_order_item(sef, order_object, order_item_list):
        for order_item in order_item_list:
            order_item_object = OrderItem()
            order_item_object.order = order_object
            order_item_object.product_variant = order_item['product_variant']
            order_item_object.qty = order_item['qty']

            # Reduce stock of Product Variant in the cart
            order_item['product_variant'].qty = order_item['product_variant'].qty - 2
            order_item['product_variant'].save()

            order_item_object.price = order_item['price']
            order_item_object.save()
        return

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request', None)
        # cart_items = validated_data.pop('cart_items', None)
        print(validated_data)
        order_object = Order()
        order_object.user = request.user.id
        order_object.order_number = generate_order_id()
        order_object.total_price = validated_data['total_price']
        order_object.address = validated_data['address']
        order_object.save()
        self.create_order_item(order_object, validated_data['order_items'])
        self.delete_cart_items(validated_data['cart_items'])
        return order_object

