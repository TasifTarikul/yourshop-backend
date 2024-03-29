from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductVariantViewSet

router = DefaultRouter(trailing_slash=False)
router.register('admin-product-variant', ProductVariantViewSet)

urlpatterns = [
    path('', include(router.urls))
]