from django.db import models

from project_root.coreapp.models import BaseModel
# Create your models here.

class Attribute(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class AttributeValue(BaseModel):
    title = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute,on_delete=models.CASCADE, related_name='attribute_values')

    def __str__(self):
        return self.title

class Category(BaseModel):
    title = models.CharField(max_length=200)
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class Product(BaseModel):
    title = models.CharField(max_length=500)
    price = models.FloatField()
    qty = models.BigIntegerField()
    sku = models.CharField(max_length=100)
    detail= models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title