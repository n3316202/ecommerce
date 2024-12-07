from django.contrib import admin
from django.urls import path

from .views import base_views,comment_views,post_views
app_name = 'boards'

urlpatterns = [
   # base_views.py
   path("", base_views.index,name='index'), #boards/ 끝에 슬러시 주의 할것
   path('<int:post_id>/', base_views.detail, name='detail'),
   
   #comment_views.py
   path('comment/create/<int:post_id>/', comment_views.comment_create, name='reply_create'),
   path('comment/modify/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
   path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
   path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),

   #post_views
   path('post/create/', post_views.post_create, name='post_create'),
   path('post/modify/<int:post_id>/', post_views.post_modify, name='post_modify'),
   path('post/delete/<int:post_id>/', post_views.post_delete, name='post_delete'),
   path('post/vote/<int:post_id>/', post_views.post_vote, name='post_vote'),

]
