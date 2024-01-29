from django.db import models
from django.conf import settings

from project_root.coreapp.models import BaseModel
from project_root.product.models import ProductVariant

# Create your models here.
class CartItem(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='cart_items')
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='cart_items')
    qty = models.BigIntegerField()
    price = models.FloatField()

class WishlistItem(BaseModel):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='wishlist_item')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
