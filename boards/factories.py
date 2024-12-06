import factory
from faker import Faker
from boards.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = Faker('ko-KR').name()
    content = Faker('ko-KR').catch_phrase() #fake.text() 

    #email = factory.lazy_attribute(lambda u: f"{u.name.split()[0]}@example.com")
    #phone = "01012345678"
    #password = make_password("qwer1234")