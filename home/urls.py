from django.urls import path
from .views import homepage, product_view

urlpatterns = [
	path('', homepage, name="index"),
	path('product/<int:pk>', product_view, name='product_info')
]