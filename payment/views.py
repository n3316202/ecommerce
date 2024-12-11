from statistics import quantiles
from django.shortcuts import redirect, render
from django.urls import path

from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import Order, ShippingAddress
from . import views
from django.contrib import messages

#dev_41 url 추가
# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html",{})

#dev_42
def payment_update_info(request):

    if request.user.is_authenticated:
        
        #Get Current uer's shipping Info
        shipping_user = ShippingAddress.objects.get(id=request.user.id)

        #Get User's Shipping Form
        form = ShippingForm(request.POST or None, instance=shipping_user)
            
        if form.is_valid():
            form.save()
            #Save shipping form
            form.save()

            messages.success(request, "결재정보가 업데이트 되었습니다!!")
            return redirect('/')
                
        return render(request, "payment/payment_update_info.html",{'form':form})
    else:
         messages.success(request, "You Must be logged In To Access That Page!!")
         return redirect('/login')

#dev_43
def payment_process_order(request):
    
    if request.POST:

        cart = Cart(request)
        cart_products = cart.get_prods
        quantiles = cart.get_quants
        totals = cart.cart_total()
        print(totals)
        
        #Gether Order Info
        if request.user.is_authenticated:
            #logged in
            user = request.user
            #Create Order
            create_order = Order(user=user)
            create_order.amount_paid = totals
            create_order.save()

            messages.success(request, "주문이 완료 되었습니다.")
            return redirect('/')
        else:
            messages.success(request, "You Must be logged In To order the products")
            return redirect('/login')


    else:
        messages.success(request, "Access denied")
        return redirect('/')
            

