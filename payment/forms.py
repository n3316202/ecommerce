from django import forms
from django.contrib.auth.models import User
from payment.models import ShippingAddress


#dev_42 배송폼 작성
class ShippingForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        exclude = ['user']
