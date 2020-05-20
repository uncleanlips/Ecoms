from django.shortcuts import render

from .models import Customer
from .models import Product
from .models import Order
from .models import OrderItem
from .models import ShippingAddress


def store(request):
    products = Product.objects.all()
    context = {
        'product': products
    }
    
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
