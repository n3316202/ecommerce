from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from api.views import   CategoryViewSet, api_product, api_products, hello_world, hello_world_drf
from rest_framework.routers import DefaultRouter

#dev_48 app/urls.py 추가
app_name = 'api'

#dev_54
router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
# /post/ 주소에 대해 URL Reverse 이름은 post-list이 등록
# /post/10/ 류의 주소에 대해 URL Reverse 이름은 post-detail이 등록


urlpatterns = [
    path("hello_world/", hello_world),
    path("hello_world_drf/", hello_world_drf),
    path("products/", api_products),#dev_49
    path("products/<int:pk>/", api_product),#dev_49
    path("products/", api_products),
    path("products/<int:pk>/", api_product),
    #path("categories/", MixinsCategories.as_view()),#dev_52
    #path("categories/<int:pk>/", MixinsCategory.as_view()),#dev_52
    #path("categories/", APICategories.as_view()),#dev_53
    #path("categories/<int:pk>/", APICategory.as_view()),#dev_53
    #path("categories/", category_list),#dev_54
    #path("categories/<int:pk>/", category_detail),#dev_54
    path("", include(router.urls)),#dev_54
]
