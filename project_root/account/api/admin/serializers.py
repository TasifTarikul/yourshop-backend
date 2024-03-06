from django.contrib.auth.models import AnonymousUser

from rest_framework import serializers

from project_root.account.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'

    
    def create(self, validated_data):
        request = self.context.get('request', None)
        print(request.user)
        address_object = Address()
        address_object.user = request.user
        address_object.full_name = validated_data['full_name']
        address_object.address = validated_data['address']
        address_object.mobile_number = validated_data['mobile_number']
        address_object.division = validated_data['division']
        address_object.city = validated_data['city']
        address_object.area = validated_data['area']
        address_object.save()
        return address_object
