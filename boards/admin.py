from django.contrib import admin

from django.contrib import admin
from .models import Comment, Post

# Register your models here.

#admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title','content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)