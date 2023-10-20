from rest_framework import serializers
from project_root.product.models import Category

class CategorySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    # parent = serializers.IntegerField(read_only=True)
    # children = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # class Meta:
    #     model = Category
    #     fields = [
    #         'id', 'title', 'created_at', 'updated_at', 'parent'
    #     ]
    
    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['parent'] = CategorySerializer()
        fields['children'] = CategorySerializer(required=False, many=True)
        return fields