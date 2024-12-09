from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def cart_summary(reqeust):

    return render(reqeust, "cart/cart_summary.html",{})

def cart_add(reqeust):
    pass

def cart_delete(reqeust):
    pass

def cart_update(reqeust):
    pass

