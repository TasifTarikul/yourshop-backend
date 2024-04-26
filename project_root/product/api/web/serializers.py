from rest_framework import serializers
from project_root.product.models import Product
from project_root.product.api.admin.category.serializers import CategroySerializer
from project_root.product.api.admin.category_attribute.serializers import CategoryAttributeSerializer
from project_root.product.api.admin.category_attribute_value.serializers import CategoryAttributeValueSerializer

class ListCategorySerializer(CategroySerializer):
    
    def get_fields(self):
        fields = super(ListCategorySerializer, self).get_fields()
        fields['parent'] = ListCategorySerializer()
        fields['children'] = ListCategorySerializer(required=False, many=True)
        return fields

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image')

