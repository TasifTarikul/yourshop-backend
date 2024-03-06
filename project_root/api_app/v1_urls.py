from django.urls import path, include


urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('auth/common/', include('project_root.coreapp.api.common.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('product/web/', include('project_root.product.api.web.urls')),
    path('product/admin/', include('project_root.product.api.admin.urls')),
    path('cart/web/', include('project_root.cart.api.web.urls')),
    path('account/admin/', include('project_root.account.api.admin.urls')),
    # path('order/web/', include('project_root.order.api.web.urls')),
    # path('order/admin/', include('project_root.order.api.admin.urls')),
]

