from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register('admin-category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]