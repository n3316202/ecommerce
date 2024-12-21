from rest_framework import serializers
from payment.models import Order
from store.models import Category, Product


#dev_49 serializers.py 생성
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  #fields = [ "id", "name", "price", "category", "is_sale","sale_price"]

    
#dev_51
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

#dev_58
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = "__all__"
