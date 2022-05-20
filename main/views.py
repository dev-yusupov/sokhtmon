from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import CurrencyForm, ProductForm
from .models import Currency
from home.models import Product

# Create your views here.
def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		context['url'] = fs.url(name)
	return render(request, 'upload.html', context)

def admin(request):
	products = Product.objects.all()
	currency = Currency.objects.get(id=1)
	return render(request, 'admin.html', {
		"products": products,
		"currency": currency,
		})

def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {
		'products': products
		})

def add_product(request):
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("admin")
	
	else:
		form = ProductForm()
	return render(request, 'add_product.html', {
		'form': form
		})

def delete_product(request, pk):
	if request.method == "POST":
		product = Product.objects.get(pk=pk)
		product.delete()
	return redirect('admin')


def currency(request):
	currency = Currency.objects.get(id=1)
	form = CurrencyForm(request.POST, instance=currency)
	if form.is_valid():
		form.save()
		return redirect("admin")

	return render(request, "change-currency.html", {
		"form": form
		})


def delete_product(request, pk):
	if request.method == "POST":
		product = Product.objects.get(pk=pk)
		product.delete()
	return redirect('admin')