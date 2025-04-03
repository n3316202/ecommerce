from importlib.resources import read_binary
from itertools import product
from django.db import transaction
from rest_framework import serializers

from store.models import Product


#def_49 serializers.py 생성
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  #fields = [ "id", "name", "price", "category", "is_sale","sale_price"]

        # def validate_price(self, value):
        #     if value > 1000:
        #         raise serializers.ValidationError("Price must be a positive value.")
        #     return value

        # def validate_name(self, value):
        #     if len(value) > 3:
        #         raise serializers.ValidationError("Name must be at most 3 characters long.")
        #     return value

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.IntegerField()
#     category = serializers.IntegerField()
#     description = serializers.CharField(max_length=250, required=False, allow_blank=True, allow_null=True)
#     image = serializers.ImageField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()    


