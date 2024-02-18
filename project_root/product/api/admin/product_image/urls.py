from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductImageViewSet

router = DefaultRouter(trailing_slash=False)
router.register('admin-product-image', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]