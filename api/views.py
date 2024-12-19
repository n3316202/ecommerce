from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer
from store.models import Product
from rest_framework import status

# Create your views here.

#dev_48
#기존방식
def hello_world(request):
    return HttpResponse('Hello World!')

#https://www.django-rest-framework.org/api-guide/views/#api_view
#DRF 방식
@api_view(['GET'])
def hello_world_drf(request):
    return Response({"message":'Hello World!'})


#def_50 추가 되도록
@api_view(['GET','POST'])
def api_products(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#def_50 수정 삭제 조회가 되도록 추가
@api_view(['GET', 'PUT', 'DELETE'])
def api_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)