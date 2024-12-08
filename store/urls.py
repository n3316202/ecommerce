from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('product/<int:product_id>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'), #변수 foo 의 의미  참고:https://namu.wiki/w/foo
]
