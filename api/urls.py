from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from api.views import  MixinsCategories, MixinsCategory, api_product, api_products, hello_world, hello_world_drf

#dev_48 app/urls.py 추가
app_name = 'api'

urlpatterns = [
    path("hello_world/", hello_world),
    path("hello_world_drf/", hello_world_drf),
    path("products/", api_products),#dev_49
    path("products/<int:pk>/", api_product),#dev_49
    path("products/", api_products),
    path("products/<int:pk>/", api_product),
    path("categories/", MixinsCategories.as_view()),#dev_52
    path("categories/<int:pk>/", MixinsCategory.as_view()),#dev_52
]
