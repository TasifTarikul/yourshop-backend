from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AdminProductView

router = DefaultRouter(trailing_slash=False)
router.register('admin-product', AdminProductView)

urlpatterns = [
    path('', include(router.urls))
]