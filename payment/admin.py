from django.contrib import admin
from payment.models import Order, OrderItem, Payment, ShippingAddress

#dev_41 admin 추가
# Register your models here.
admin.site.register(ShippingAddress)

#dev_43
admin.site.register(Order)
admin.site.register(OrderItem)

#dev_47
admin.site.register(Payment)
