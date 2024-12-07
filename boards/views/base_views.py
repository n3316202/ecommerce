from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    
    post_list = Post.objects.order_by('-created_at')
    
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj} 
    #context = {'post_list': post_list}

    return render(request, 'boards/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'boards/post_detail.html', context)
