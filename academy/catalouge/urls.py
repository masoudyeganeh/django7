from django.urls import path
from . import views

urlpatterns = [
    path('product/list/', views.product_list, name="product_list"),
    path('product/detail/<int:pk>/', views.product_detail, name="product_detail")
]