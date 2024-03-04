from django.db import models
from django.conf import settings

from project_root.coreapp.models import BaseModel
from project_root.product.models import ProductVariant
from project_root.account.models import Address
from .constants import ORDER_STATUS, O_PENDING

# Create your models here.

class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='orders')
    order_number = models.CharField(max_length=200)
    total_price = models.FloatField()
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=O_PENDING)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='orders')

class OrderItems(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name='order_items')
    qty = models.IntegerField()
    price = models.FloatField()

class OrderReturn(BaseModel):
    order_item = models.OneToOneField(OrderItems, on_delete=models.PROTECT)
    reason = models.CharField(max_length=2000)