from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AttributeViewSet

router = DefaultRouter(trailing_slash=False)
router.register('admin-attribute', AttributeViewSet)

urlpatterns = [
    path('', include(router.urls))
]