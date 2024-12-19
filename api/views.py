from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from api.serializers import ProductSerializer
from store.models import Product

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


#def_49
@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)
