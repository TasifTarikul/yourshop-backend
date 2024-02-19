import base64
from io import BytesIO

from rest_framework import serializers
import boto3
from botocore.exceptions import ClientError

from project_root.product.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    image=serializers.FileField()
    class Meta:
        model = ProductImage
        fields = ('id','image', 'display_picture', 'product')
    
    def create(self, validated_data):
        image_file = validated_data['image'].read()
        s3=boto3.client('s3')
        try:
            response = s3.upload_fileobj(BytesIO(image_file), 'yourshopdev-test-bucket', 'pp.jpg', ExtraArgs={'ContentType': 'image/jpeg'})
        except ClientError as e:
            print(e)
        return validated_data