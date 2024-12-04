from django.contrib import admin
from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
   path("", views.index,name='index'), #boards/ 끝에 슬러시 주의 할것
   path("for_loop/", views.for_loop), #boards/for_loop/ 끝에 슬러시 주의 할것
   path('<int:post_id>/', views.detail, name='detail'),
]
