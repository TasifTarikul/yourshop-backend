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


    def create_attribute_obj(self,product_variant_obj, attribute_list):
        for pv_attrs in attribute_list:
            attr_obj = Attribute()
            attr_obj.title = pv_attrs['title']
            attr_obj.value = pv_attrs['value']
            if 'image' in pv_attrs.keys():
                attr_obj.image = pv_attrs['image']
            attr_obj.product_variant = product_variant_obj
            attr_obj.save()
        return

    def create_product_variant_obj(self, product_obj, product_variant_list):
        for pv in product_variant_list:
            pv_obj = ProductVariant()
            pv_obj.price = pv['price']
            pv_obj.qty = pv['qty']
            pv_obj.sku = pv['sku']
            pv_obj.description = pv['description']
            pv_obj.product = product_obj
            pv_obj.save()
            self.create_attribute_obj(pv_obj, pv['attributes'])
        return

    def create_product_image_obj(self, product_obj, p_image_list):
        for p_image in p_image_list:
            p_image_obj = ProductImage()
            p_image_obj.image = p_image['image']
            if 'display_picture' in p_image.keys():
                p_image_obj.display_picture = p_image['display_picture']
            p_image_obj.product = product_obj
            p_image_obj.save()
        return
            
    def create_product_obj(self, title, category, pv_list, p_image_list):
        product_obj = Product()
        product_obj.title = title
        product_obj.category = category
        product_obj.save()
        self.create_product_variant_obj(product_obj, pv_list)
        self.create_product_image_obj(product_obj, p_image_list)
        return product_obj
    

    def create(self, validated_data):
        product_obj = self.create_product_obj(validated_data['title'], 
                                              validated_data['category'], 
                                              validated_data['product_variants'],
                                              validated_data['product_images'])
        return product_obj

