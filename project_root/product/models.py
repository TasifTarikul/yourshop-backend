from django.db import models
from django.contrib.postgres.fields import CIText
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from project_root.coreapp.models import BaseModel
# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=200)
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class Product(BaseModel):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_variants')
    price = models.FloatField()
    qty = models.BigIntegerField()
    sku = models.CharField(max_length=100)
    description= models.TextField(max_length=5000)

    def __str__(self):
        return self.product.title + ', sku-' + self.sku
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.CharField(max_length=300)
    display_picture = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title

class CategoryAttribute(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_attributes')
    title = models.CharField(max_length=200)

class CategoryAttributeValue(BaseModel):
    category_attribute = models.ForeignKey(CategoryAttribute, on_delete=models.CASCADE, related_name='category_attribute_values')
    title = models.CharField(max_length=200)

class Attribute(BaseModel):
    title = models.CharField(max_length=200)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='attributes')
    value = models.CharField(max_length=100)
    image = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title
    