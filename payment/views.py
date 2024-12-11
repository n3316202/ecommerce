from django.urls import path
from . import views

#dev_41 url 추가
# Create your views here.
urlpatterns = [
    path("payment_success/", views.payment_success, name="payment_success"),
]