from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from accounts.forms import UserForm
from django.contrib import messages

from cart.cart import Cart
from cart.models import Cart as CartModel, CartItem
#dev_40
import json

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

#dev_40
def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user) 
            
            saved_cart_item = CartItem.objects.filter(cart__user__id=request.user.id)
            
            if saved_cart_item:
                
                #Get the cart
                cart = Cart(request)

                for item in saved_cart_item:
                    print("===========",item.product.id)
                    print("===========",item.quantity)                    
                    cart.add(product=item.product,quantity=item.quantity) 

            messages.success(request,"You Have been logged in")
            return redirect('/')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')
    else:    
        return render(request, 'accounts/login.html',{})