from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("ok/", views.ok), #home/ok/ 끝에 슬러시 주의 할것
]
