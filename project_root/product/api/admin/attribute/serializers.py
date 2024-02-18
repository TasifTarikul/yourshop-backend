from rest_framework import serializers

from project_root.product.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id','title', 'value', 'image')