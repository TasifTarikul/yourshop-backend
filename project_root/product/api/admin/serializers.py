from collections import Counter

from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from project_root.product.models import Product, ProductVariant, ProductImage, Attribute

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id','title', 'value', 'image')
        read_only_fields = ('id', )

class ProductVariantSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)
    class Meta:
        model = ProductVariant
        fields = ('id','price', 'qty', 'sku', 'description', 'attributes')
        read_only_fields = ('id', )

    def find_duplicate_strings(self, lst):
        lowercase_strings = [s.lower() for s in lst]
        # Use Counter to count occurrences of each string
        string_counts = Counter(lowercase_strings)
        # Find strings with counts greater than 1 (indicating duplicates)
        duplicates = [string for string, count in string_counts.items() if count > 1]
        return duplicates
    
    def validate_attributes(self, attributes):
        attrs_title_values = []
        for attr_set in attributes:
            attrs_title_values.append(attr_set['title'])
        duplicates = self.find_duplicate_strings(attrs_title_values)
        if duplicates:
            if len(duplicates) > 1:
                raise ValidationError(f"Attributes cannot have duplicate titles - {', '.join(duplicates)}")
            else:
                raise ValidationError(f"Attributes cannot have duplicate title - {duplicates[0]}")
        return attributes

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','image', 'display_picture')
        read_only_fields = ('id', )

class ProductSerializer(serializers.ModelSerializer):
    product_variants = ProductVariantSerializer(many=True)
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','category','product_variants','product_images')
        read_only_fields = ('id', )

    # takes the list of attributes of a product variant and create product variant object
    def create_attribute_obj(self,product_variant_obj, attribute_list):
        for product_variant_attr in attribute_list:
            attr_obj = Attribute()
            attr_obj.title = product_variant_attr['title']
            attr_obj.value = product_variant_attr['value']
            if 'image' in product_variant_attr.keys():
                attr_obj.image = product_variant_attr['image']
            attr_obj.product_variant = product_variant_obj
            attr_obj.save()
        return

    # takes the list of product variants of a product and create product variant object
    def create_product_variant_obj(self, product_obj, product_variant_list):
        for product_variant in product_variant_list:
            product_variant_obj = ProductVariant()
            product_variant_obj.price = product_variant['price']
            product_variant_obj.qty = product_variant['qty']
            product_variant_obj.sku = product_variant['sku']
            product_variant_obj.description = product_variant['description']
            product_variant_obj.product = product_obj
            product_variant_obj.save()
            self.create_attribute_obj(product_variant_obj, product_variant['attributes'])
        return
    # takes the list of product images of a product and create product image object
    def create_product_image_obj(self, product_obj, product_image_list):
        for product_image in product_image_list:
            product_image_obj = ProductImage()
            product_image_obj.image = product_image['image']
            if 'display_picture' in product_image.keys():
                product_image_obj.display_picture = product_image['display_picture']
            product_image_obj.product = product_obj
            product_image_obj.save()
        return
            
    # Creates a product object
    def create_product_obj(self, title, category, prodcut_variant_list, product_image_list):
        product_obj = Product()
        product_obj.title = title
        product_obj.category = category
        product_obj.save()
        self.create_product_variant_obj(product_obj, prodcut_variant_list)
        self.create_product_image_obj(product_obj, product_image_list)
        return product_obj

    # override create method to save objects of multiple Models
    @transaction.atomic
    def create(self, validated_data):
        product_obj = self.create_product_obj(validated_data['title'], 
                                              validated_data['category'], 
                                              validated_data['product_variants'],
                                              validated_data['product_images'])
        return product_obj

class UpdateAttributeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)
    class Meta:
        model = Attribute
        fields = ('id','title', 'value', 'image')
    
class UpdateProductVariantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)
    attributes = UpdateAttributeSerializer(many=True)

    class Meta:
        model = ProductVariant
        fields = ('id','price', 'qty', 'sku', 'description', 'attributes')
        

    def find_duplicate_strings(self, lst):
        lowercase_strings = [s.lower() for s in lst]
        # Use Counter to count occurrences of each string
        string_counts = Counter(lowercase_strings)
        # Find strings with counts greater than 1 (indicating duplicates)
        duplicates = [string for string, count in string_counts.items() if count > 1]
        return duplicates
    
    def validate_attributes(self, attributes):
        attrs_title_values = []
        for attr_set in attributes:
            attrs_title_values.append(attr_set['title'])
        duplicates = self.find_duplicate_strings(attrs_title_values)
        if duplicates:
            if len(duplicates) > 1:
                raise ValidationError(f"Attributes cannot have duplicate titles - {', '.join(duplicates)}")
            else:
                raise ValidationError(f"Attributes cannot have duplicate title - {duplicates[0]}")
        return attributes
    
class UpdateProductImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = ProductImage
        fields = ('id','image', 'display_picture')
    
class UpdateProductSerializer(serializers.ModelSerializer):
    product_variants = UpdateProductVariantSerializer(many=True)
    product_images = UpdateProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title','category','product_variants','product_images')

    # takes the list of attributes of a product variant and update product variant object
    def update_attribute_obj(self,product_variant_obj, attribute_list):
        for product_variant_attr in attribute_list:
            attr_obj = Attribute.objects.get(id=product_variant_attr['id'])
            attr_obj.title = product_variant_attr['title']
            attr_obj.value = product_variant_attr['value']
            if 'image' in product_variant_attr.keys():
                attr_obj.image = product_variant_attr['image']
            attr_obj.product_variant = product_variant_obj
            attr_obj.save()
        return

    # takes the list of product variants of a product and update product variant object
    def update_product_variant_obj(self, product_obj, product_variant_list):
        for product_variant in product_variant_list:
            print(product_variant)
            product_variant_obj = ProductVariant.objects.get(id=product_variant['id'])
            product_variant_obj.price = product_variant['price']
            product_variant_obj.qty = product_variant['qty']
            product_variant_obj.sku = product_variant['sku']
            product_variant_obj.description = product_variant['description']
            product_variant_obj.product = product_obj
            product_variant_obj.save()
            self.update_attribute_obj(product_variant_obj, product_variant['attributes'])
        return
    # takes the list of product images of a product and update product image object
    def update_product_image_obj(self, product_obj, product_image_list):
        for product_image in product_image_list:
            product_image_obj = ProductImage.objects.get(id=product_image['id'])
            product_image_obj.image = product_image['image']
            if 'display_picture' in product_image.keys():
                product_image_obj.display_picture = product_image['display_picture']
            product_image_obj.product = product_obj
            product_image_obj.save()
        return
            
    # updates a product object
    def update_product_obj(self, product_obj, title, category, prodcut_variant_list, product_image_list):
        product_obj.title = title
        product_obj.category = category
        product_obj.save()
        self.update_product_variant_obj(product_obj, prodcut_variant_list)
        self.update_product_image_obj(product_obj, product_image_list)
        return product_obj
    
    @transaction.atomic
    def update(self,instance, validated_data):
        print(validated_data)
        print(self)
        product_obj = self.update_product_obj(
                                                instance,
                                                validated_data['title'], 
                                                validated_data['category'], 
                                                validated_data['product_variants'],
                                                validated_data['product_images']
                                            )
        return product_obj