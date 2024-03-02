from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CartViewset

router = DefaultRouter(trailing_slash=False)
router.register('web-cart', CartViewset)

urlpatterns = [
    path('', include(router.urls)),
]