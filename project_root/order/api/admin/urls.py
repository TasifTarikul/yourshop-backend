from django.urls import path, include

urlpatterns = [
    path('order/', include('project_root.order.api.admin.order.urls')),
    path('order-item/', include('project_root.order.api.admin.order_item.urls')),
    path('order_return/', include('project_root.order.api.admin.order_return.urls'))
]