from django.shortcuts import render
from main.models import Post, Contact, Currency
from .models import Product

# Create your views here.
def homepage(request):
	products = Product.objects.all()
	currency = Currency.objects.get(id=1)
	posts = Post.objects.get(id=1)
	contact = Contact.objects.get(id=1)
	return render(request, 'index.html', {
		"products": products,
		"posts": posts,
		"contact": contact,
		"currency": currency
		})


def product_view(request, pk):
	product = Product.objects.get(pk=pk)
	contact = Contact.objects.get(id=1)
	currency = Currency.objects.get(id=1)
	return render(request, 'product.html', {
		"product": product,
		"contact": contact,
		"currency": currency
		})