from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from project_root.product.helpers import find_duplicate_strings
from project_root.product.models import Product, ProductVariant, ProductImage, Attribute
from project_root.product.api.admin.product_variant.serializers import ProductVariantSerializer
from project_root.product.api.admin.attribute.serializers import AttributeSerializer
from project_root.product.api.admin.product_image.serializers import ProductImageSerializer

class CustomAttributeSerializer(AttributeSerializer):
    class Meta:
        model = Attribute
        fields = ('id','title', 'value', 'image')

class CustomProductVariantSerializer(ProductVariantSerializer):
    attributes = CustomAttributeSerializer(many=True)

    class Meta:
        model = ProductVariantSerializer.Meta.model
        fields = ProductVariantSerializer.Meta.fields + ('attributes',)
    
    def validate_attributes(self, attributes):
        attrs_title_values = []
        for attr_set in attributes:
            attrs_title_values.append(attr_set['title'])
        duplicates = find_duplicate_strings(attrs_title_values)
        if duplicates:
            if len(duplicates) > 1:
                raise ValidationError(f"Attributes cannot have duplicate titles - {', '.join(duplicates)}")
            else:
                raise ValidationError(f"Attributes cannot have duplicate title - {duplicates[0]}")
        return attributes

class CustomProductImageSerializer(ProductImageSerializer):
    class Meta:
        model=ProductImageSerializer.Meta.model
        fields=('id', 'display_picture', 'image')

class ProductSerializer(serializers.ModelSerializer):
    product_variants = CustomProductVariantSerializer(many=True)
    product_images = CustomProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','category','product_variants', 'product_images')


    # takes the list of attributes of a product variant and create product variant object
    def attribute_obj(self,product_variant_obj, attribute_list):
        for product_variant_attr in attribute_list:
            attr_obj = None
            if 'id' in product_variant_attr:
                attr_obj = Attribute.objects.get(id=product_variant_attr['id'])
            else:
                attr_obj = Attribute()
            attr_obj.title = product_variant_attr['title']
            attr_obj.value = product_variant_attr['value']
            if 'image' in product_variant_attr.keys():
                attr_obj.image = product_variant_attr['image']
            attr_obj.product_variant = product_variant_obj
            attr_obj.save()
        return

    # takes the list of product variants of a product and create/update product variant object
    def product_variant_obj(self, product_obj, product_variant_list):
        for product_variant in product_variant_list:
            product_variant_obj = None
            if 'id' in product_variant:
                product_variant_obj = ProductVariant.objects.get(id=product_variant['id'])
            else:
                product_variant_obj = ProductVariant()
            product_variant_obj.price = product_variant['price']
            product_variant_obj.qty = product_variant['qty']
            product_variant_obj.sku = product_variant['sku']
            product_variant_obj.description = product_variant['description']
            product_variant_obj.category_attribute_value = product_variant['category_attribute_value']
            product_variant_obj.product = product_obj
            product_variant_obj.save()
            self.attribute_obj(product_variant_obj, product_variant['attributes'])
        return

    # takes the list of product images of a product and create/update product image object
    def product_image_obj(self, product_obj, product_image_list):
        for product_image in product_image_list:
            product_image_obj = None
            if 'id' in product_image:
                product_image_obj = ProductImage.objects.get(id=product_image['id'])
            else:
                product_image_obj = ProductImage()
            product_image_obj.image = product_image['image']
            if 'display_picture' in product_image.keys():
                product_image_obj.display_picture = product_image['display_picture']
            product_image_obj.product = product_obj
            product_image_obj.save()
        return
            
    # Creates/Updates a product object
    def product_obj(self, **kwargs):
        product_obj = None
        if 'product_obj' in kwargs:
            product_obj = kwargs['product_obj']
        else:
            product_obj = Product()
        product_obj.title = kwargs['title']
        product_obj.category = kwargs['category']
        product_obj.save()
        self.product_variant_obj(product_obj, kwargs['product_variants_list'])
        self.product_image_obj(product_obj, kwargs['product_images_list'])
        return product_obj

    # override create method to save objects of multiple Models
    @transaction.atomic
    def create(self, validated_data):
        product_obj = self.product_obj(
                                        title=validated_data['title'], 
                                        category=validated_data['category'], 
                                        product_variants_list=validated_data['product_variants'],
                                        product_images_list=validated_data['product_images']
                                    )
        return product_obj

class UpdateCustomAttributeSerializer(CustomAttributeSerializer):
    id = serializers.IntegerField(read_only=False)

class UpdateCustomProductVariantSerializer(CustomProductVariantSerializer):
    id = serializers.IntegerField(read_only=False)
    attributes = UpdateCustomAttributeSerializer(many=True)
    
class UpdateProductImageSerializer(CustomProductImageSerializer):
    id = serializers.IntegerField(read_only=False)
    
class UpdateProductSerializer(ProductSerializer):
    product_variants = UpdateCustomProductVariantSerializer(many=True)
    product_images = UpdateProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','category','product_variants','product_images')
    
    @transaction.atomic
    def update(self,instance, validated_data):
        product_obj = self.product_obj(
                                        product_obj=instance,
                                        title=validated_data['title'], 
                                        category=validated_data['category'], 
                                        product_variants_list=validated_data['product_variants'],
                                        product_images_list=validated_data['product_images']
                                    )
        return product_obj