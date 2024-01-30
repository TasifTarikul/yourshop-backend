from rest_framework import serializers
from rest_framework.utils import model_meta
from project_root.product.models import Product, ProductVariant, ProductImage, Attribute, Category

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('title', 'value', 'image')
        

class ProductVariantSerializer(serializers.ModelSerializer):
    attributes = AttributeSerializer(many=True)
    class Meta:
        model = ProductVariant
        fields = ('price', 'qty', 'sku', 'description', 'attributes')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', 'display_picture')

class AddProductSerializer(serializers.ModelSerializer):
    product_variants = ProductVariantSerializer(many=True)
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title','category','product_variants','product_images')

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
    def create_product_obj(self, title, category, pv_list, p_image_list):
        product_obj = Product()
        product_obj.title = title
        product_obj.category = category
        product_obj.save()
        self.create_product_variant_obj(product_obj, pv_list)
        self.create_product_image_obj(product_obj, p_image_list)
        return product_obj
    
    # override create method to save objects of multiple Models
    def create(self, validated_data):
        product_obj = self.create_product_obj(validated_data['title'], 
                                              validated_data['category'], 
                                              validated_data['product_variants'],
                                              validated_data['product_images'])
        return product_obj

