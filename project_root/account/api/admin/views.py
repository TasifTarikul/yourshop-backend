from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from project_root.account.models import Address
from .serializers import AddressSerializer

class AddresViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_class = (IsAuthenticated)
