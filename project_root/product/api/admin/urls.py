from django.urls import path
from .views import AddProductView

urlpatterns = [
    path('add-product', AddProductView.as_view())
]