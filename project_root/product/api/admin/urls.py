from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductView

router = DefaultRouter(trailing_slash=False)
router.register('admin-product', ProductView)

urlpatterns = [
    path('', include(router.urls))
]

