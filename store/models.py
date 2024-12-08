from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    #price = models.DecimalField(default=0,decimal_places=2,max_digits=6) #9999.99
    price = models.IntegerField(default=0) #9999.99
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=250,default='',blank=True, null=True)
    image = models.ImageField(upload_to='upload/product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #판매 가능 여부(Add Sale stuff)
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

#User orders
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20,default='',blank=True)
    status = models.BooleanField(default = False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product