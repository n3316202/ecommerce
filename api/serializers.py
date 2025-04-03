from rest_framework import serializers
from store.models import Product


#dev_49 serializers.py 생성
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  #fields = [ "id", "name", "price", "category", "is_sale","sale_price"]
        depth = 1 #카테고리도 나오도록 함

    


