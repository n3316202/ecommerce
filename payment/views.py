from django.shortcuts import render
from django.urls import path
from . import views

#dev_41 url 추가
# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html",{})