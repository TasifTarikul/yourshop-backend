from rest_framework import serializers

from project_root.product.models import CategoryAttributeValue

class CategoryAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttributeValue
        fields = ('id', 'category_attribute', 'title')