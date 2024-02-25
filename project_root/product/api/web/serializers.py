from rest_framework import serializers
from project_root.product.models import Category
from project_root.product.api.admin.category.serializers import CategroySerializer

class ListCategorySerializer(CategroySerializer):
    
    def get_fields(self):
        fields = super(ListCategorySerializer, self).get_fields()
        fields['parent'] = ListCategorySerializer()
        fields['children'] = ListCategorySerializer(required=False, many=True)
        return fields