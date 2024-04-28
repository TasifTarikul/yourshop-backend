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

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name='order_items')
    qty = models.IntegerField()
    price = models.FloatField()
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=O_PENDING)

class OrderReturn(BaseModel):
    order_item = models.OneToOneField(OrderItem, on_delete=models.PROTECT)
    reason = models.CharField(max_length=2000)

class Review(BaseModel):
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE, related_name='reviews')
    show_username = models.BooleanField(default=True)
    description = models.CharField(max_length=700)

class ProductRating(BaseModel):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='product_rating')
    rate = models.IntegerField(max_value=5)
    rate_name = models.SlugField()
    user_message = models.CharField(max_length=200)

class DeliveryRating(BaseModel):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='delivery_rating')
    rate = models.IntegerField(max_value=5)
    rate_name = models.SlugField()
    user_message = models.CharField(max_length=200)

class ReviewImage(BaseModel):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_images')
    image_or_video = models.FileField()