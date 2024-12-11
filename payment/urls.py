from django.urls import path
from . import views

#dev_42
app_name = 'payment'

#dev_41 url 추가
# Create your views here.
urlpatterns = [
    path("payment_update_info/", views.payment_update_info, name="payment_update_info"), #dev_42 추가
    path("payment_success/", views.payment_success, name="payment_success"),
]