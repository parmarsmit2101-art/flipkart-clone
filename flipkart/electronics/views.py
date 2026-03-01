from django.shortcuts import render, redirect
from .models import Electronics
from django.http import HttpResponse
# Create your views here.

def electronics(request):
    return render(request, 'electronics.html')
def electronics_home(request):
    products = Electronics.objects.all()
    return render(request, 'electronics/electronics.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Electronics.objects.create(
            name=name,
            brand=brand,
            price=price,
            description=description
        )


def clothing(request):
    return HttpResponse("Welcome to the clothing section!")

