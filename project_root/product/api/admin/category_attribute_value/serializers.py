from rest_framework import serializers

from project_root.product.models import CategoryAttributeValue

class CategoryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttributeValue
        fields = ('category', 'title')