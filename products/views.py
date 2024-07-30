from django.shortcuts import render
from .models import Product


def all_products(request): 
    return render(request, 'products/products.html', context)
