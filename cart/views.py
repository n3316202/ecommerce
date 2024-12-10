from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render

from cart.cart import Cart
from store.models import Product
from django.contrib import messages

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    
    # 추가
    totals = cart.cart_total()
    
    return render(request, "cart/cart_summary.html",{"cart_products": cart_products,"quantities": quantities,"totals": totals})


def cart_add(request):
    
    cart  = Cart(request)

    if request.POST.get('action') == 'post':
        
        #get stuff
        product_id = int(request.POST.get('product_id'))
        print('product_id', product_id)
        
        product_qty = int(request.POST.get('product_qty'))
        # lookup proudct in DB
        product = get_object_or_404(Product,id=product_id)

        print("프로덕트",product)

        #save to session
        cart.add(product=product, quantity = product_qty)

        #Get Cart Quantity
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        #추가 dev_38
        messages.success(request,"장바구니에 해당 상품이 추가되었습니다.")
        return response
    

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        print('=========')
        
        #get stuff
        product_id = int(request.POST.get('product_id'))
        print('product_id =============== ', product_id)

        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request,"장바구니에서 해당 상품이 삭제되었습니다.")
        return response

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        #추가 dev_38
        messages.success(request,"장바구니가 업데이트 되었습니다.")        
        return response

