from django.urls import path, include


urlpatterns = [
    path('product/web/', include('project_root.product.api.web.urls')),
]

