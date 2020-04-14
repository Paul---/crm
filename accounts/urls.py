from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('customer/', views.customer_page),
    path('products/', views.products_page),
]
