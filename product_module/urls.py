from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:save>', views.product_detail, name='product_detail')
]