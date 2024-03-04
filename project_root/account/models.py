from django.db import models
from django.conf import settings

from project_root.coreapp.models import BaseModel
# Create your models here.

class Address(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name='address')
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=50)
    division = models.CharField(max_length=50,choices=())
    city = models.CharField(max_length=50, choices=())
    area = models.CharField(max_length=50, choices=())
    default_billing = models.BooleanField(default=False)
    default_shipping = models.BooleanField(default=False)



