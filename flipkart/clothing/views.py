from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def home(request):
    prod = Product.objects.all()
    form = ProductForm()
    return render(request, 'clothing/home.html', {"prod":prod, "from":form})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'prod': products})


