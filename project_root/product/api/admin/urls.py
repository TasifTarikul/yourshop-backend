from django.urls import path, include

urlpatterns = [
    path('product/', include('project_root.product.api.admin.product.urls',)),
    path('product-variant/', include('project_root.product.api.admin.product_variant.urls',)),
    path('product-image/', include('project_root.product.api.admin.product_image.urls',)),
    path('attribute/', include('project_root.product.api.admin.attribute.urls',))
]

