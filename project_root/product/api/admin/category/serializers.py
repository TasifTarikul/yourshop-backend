from rest_framework import serializers

from project_root.product.models import Category


class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title', 'parent')