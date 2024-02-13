from django.urls import path, include

urlpatterns = [
    path('product/', include('project_root.product.api.admin.product.urls'))
]

