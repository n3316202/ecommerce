from django.contrib import admin

from django.contrib import admin
from .models import Comment, Post

# Register your models here.

#admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ('id', 'user','title', 'created_at','updated_at')

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','created_at','updated_at')

#admin.site.register(Comment)