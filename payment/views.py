from django.shortcuts import redirect, render
from django.urls import path

from payment.forms import ShippingForm
from payment.models import ShippingAddress
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

