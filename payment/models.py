from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#dev_41 model 생성
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True,blank=True)
    zipcode = models.CharField(max_length=255, null=True,blank=True)
    country = models.CharField(max_length=255)

    # Dont' plurallize address
    #어드민 패널을 만지다 보면 내가 등록한 모델 이름을 장고 어드민이 알아서 복수로 만들어 주는 것을 알 수 있다. 
    # 그럴때 가끔 -y 로 끝나는 단어의 끝에도 그냥 s를 붙이는 경우가 있는데, 
    # 이때 메타 클래스의 verbose_name을 이용해서 바꿔줄 수 있다.
    
    #verbose_name_plural 옵션
    #사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시되는 것은 동일하나 영어를 기준으로 복수형이다.
    #한국어에서는 굳이 단수와 복수를 구별해 사용하지 않으므로 verbose_name과 동일하게 쓸 수 있다.
    #verbose_name_plural 옵션을 지정하지 않으면 verbose_name에 s를 붙인다.

    class Meta:
        verbose_name_plural = "배송주소"
    
    def __str__(self):
        return f'배송주소 - {str(self.id)}'