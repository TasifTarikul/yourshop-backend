from django.db import models
from django.conf import settings

from project_root.coreapp.models import BaseModel
from .constants import ORDER_STATUS, O_PENDING

# Create your models here.

class Order(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=200)
    total_price = models.FloatField()
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=O_PENDING)

