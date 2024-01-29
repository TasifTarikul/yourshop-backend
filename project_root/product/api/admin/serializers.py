from rest_framework import serializers

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
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title','category','product_variants','product_image')


    def create(self, validated_data):
        
        ModelClass = self.Meta.model

        info = model_meta.get_field_info(ModelClass)

        print(info)