from django.urls import path, include

urlpatterns = [
    path('', include('project_root.product.api.admin.product.urls',)),
    path('', include('project_root.product.api.admin.product_variant.urls',)),
    path('', include('project_root.product.api.admin.product_image.urls',)),
    path('', include('project_root.product.api.admin.attribute.urls',))
]

