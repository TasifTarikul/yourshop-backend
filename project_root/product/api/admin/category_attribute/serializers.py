from rest_framework import serializers

from project_root.product.models import CategoryAttribute

class CategoryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = ('category', 'title')