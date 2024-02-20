import base64
from io import BytesIO

from django.core.files.storage import get_storage_class

from rest_framework import serializers
import boto3
import botocore
from botocore.exceptions import ClientError

from project_root.product.models import ProductImage
from config.settings import local


class ProductImageSerializer(serializers.ModelSerializer):
    image=serializers.FileField()
    class Meta:
        model = ProductImage
        fields = ('id','image', 'display_picture', 'product')

    def create(self, validated_data):
        image_file = validated_data['image'].file
        s3=boto3.client('s3')
        try:
            s3.upload_fileobj(
                                BytesIO(image_file.read()),
                                'yourshopdev-test-bucket',
                                local.PUBLIC_MEDIA_LOCATION+'/profile/pp.jpg',
                                ExtraArgs={'ContentType': 'image/jpeg'}
                            )
        except ClientError as e:
            print(e)

        return validated_data