from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CategorySerializer, ProductSerializer
from store.models import Category, Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
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
    
#dev_51
class APICategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class APICategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, category_id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#dev_52
class MixinsCategories(ListModelMixin,CreateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request)
        
    def post(self, request, *args, **kwargs):
        return self.create(request)

class MixinsCategory(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#dev_53
class APICategories(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class APICategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#dev_54
# List Route
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# REST API 규격에 맞춘 URL 매핑

# List Route
# category_list = CategoryViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# # Detail Route
# category_detail = CategoryViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })