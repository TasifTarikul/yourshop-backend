from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AddresViewset

router = DefaultRouter(trailing_slash=False)
router.register('admin-address', AddresViewset)

urlpatterns=[
    path('', include(router.urls))
]