from django.db import models

from project_root.coreapp.models import BaseModel
from django.db.models import UniqueConstraint
# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=200)
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class Product(BaseModel):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.title

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_variants')
    price = models.FloatField()
    qty = models.BigIntegerField()
    sku = models.CharField(max_length=100)
    description= models.TextField(max_length=5000)

    def __str__(self):
        return self.product.title
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.CharField(max_length=300)
    display_picture = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

class Attribute(BaseModel):
    title = models.CharField(max_length=100)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='attributes')
    value = models.CharField(max_length=100)
    image = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        # Define a unique constraint on ('title', 'product_variant') with case-insensitive comparison
        constraints = [
            UniqueConstraint(
                fields=['title', 'product_variant'],
                name='unique_title_per_variant',
                condition=models.Q(title__iexact=models.F('title'))
            )
        ]

    def __str__(self):
        return self.title
    