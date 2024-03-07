from django.urls import path, include

urlpatterns = [
    path('order/', include('project_root.order.api.web.order.urls')),
    # path('order-item/', include('project_root.order.api.web.order_item.urls')),
    # path('order_return/', include('project_root.order.api.web.order_return.urls'))
]