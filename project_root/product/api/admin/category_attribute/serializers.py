from rest_framework import serializers

from project_root.product.models import CategoryAttribute
from project_root.product.api.admin.category_attribute_value.serializers import CategoryAttributeValueSerializer

class CategoryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = ('category', 'title')

# List Filter Option in the product list page
class ListCategoryAttributeSerializer(CategoryAttributeSerializer):
    category_attribute_values = CategoryAttributeValueSerializer(many=True)
    class Meta:
        model = CategoryAttributeSerializer.Meta.model
        fields = CategoryAttributeSerializer.Meta.fields + ('category_attribute_values',)