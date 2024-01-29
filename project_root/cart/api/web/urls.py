from django.urls import path
from .views import AddCartView

urlpatterns = [
    path('add-cart/', AddCartView.as_view()),
]