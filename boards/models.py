from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128, verbose_name='제목')
    hit = models.PositiveIntegerField(verbose_name='조회수', default=0)
    image_url   = models.URLField(max_length=500,blank=True,null=True)
    content     = models.TextField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.title}"

# 댓글 관련 테이블
class Comment(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    post       = models.ForeignKey(Post, on_delete=models.CASCADE)
    content    = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

