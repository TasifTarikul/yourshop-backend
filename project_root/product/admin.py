from django.contrib import admin

from .models import Product, ProductVariant, ProductImage,Category, Attribute 

# Register your models here.
admin.site.register([
                        Product, 
                        ProductVariant, 
                        ProductImage, 
                        Category, 
                        Attribute
                    ])