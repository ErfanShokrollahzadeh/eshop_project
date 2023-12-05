from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    path('', views.ProductListView.as_view(), name='product_list'),
    # path('<slug:slug>', views.product_detail, name='product_detail')
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]