from django.contrib import admin

from .models import Product, ProductVariant, ProductImage,Category, Attribute , CategoryAttribute, CategoryAttributeValue

# Register your models here.
admin.site.register([
                        Product, 
                        ProductVariant, 
                        ProductImage, 
                        Category, 
                        Attribute,
                        CategoryAttribute,
                        CategoryAttributeValue
                    ])