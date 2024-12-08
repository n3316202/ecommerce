from calendar import c
from itertools import product
from django.shortcuts import redirect, render

from store.models import Category, Product
from django.contrib import messages

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,'store/home.html',{'products':products,'categories':categories})

def about(request):
    return render(request,'store/about.html',{})

def product(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/product.html', {'product':product})

def category(request, foo):
    #Replace Hyphens with Spaces

    foo = foo.replace('-',' ')
    print(foo)

    # Grab the category from the url
    try:
        #Look up the category
        category = Category.objects.get(name=foo)
        print(category)
        
        products = Product.objects.filter(category=category)
        print(products)
        
        return render(request, 'store/category.html',{'products':products,'category':category})
    
    except:
        messages.success(request, ("카테고리가 존재하지 않습니다."))        
        return redirect('store:home')