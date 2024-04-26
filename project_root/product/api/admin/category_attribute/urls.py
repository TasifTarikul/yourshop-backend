from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryAttributeViewSet, CategoryAttributeListView

router = DefaultRouter(trailing_slash=False)
router.register('admin-category-attribute', CategoryAttributeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-category-attributes-with-values', CategoryAttributeListView.as_view())
]

