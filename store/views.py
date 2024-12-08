from itertools import product
from django.shortcuts import render

from store.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'store/home.html',{'products':products})

def about(request):
    return render(request,'store/about.html',{})

def product(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product.html', {'product':product})