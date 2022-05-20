from django import forms
from .models import Currency, Post
from home.models import Product

class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('current_currency', )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'cover', 'cover_first', 'cover_second', 'size', 'price', 'somoni', 'ruble', "discription")
