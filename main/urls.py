from django.urls import path
from .views import admin, product_list, add_product, delete_product, currency

urlpatterns = [
	path('', admin, name="admin"),
	path('add_product/', add_product, name='add_product'),
	path('product_list/', product_list, name='product_list'),
	path('product_list/<int:pk>', delete_product, name="delete_product"),
	path('currency/', currency, name="currency"),
]