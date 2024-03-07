from django.urls import path

from .views import CreateOrder

urlpatterns = [
    path('create-order/', CreateOrder.as_view()),
]