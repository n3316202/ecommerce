from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # 페이지 만약 넘어온값이 없으면 1페이지
    
    kw = request.GET.get('kw', '')  # 검색어 넘어온값이 없으면 ''(빈값으로)   
    post_list = Post.objects.order_by('-created_at')
    
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)|  # 내용 검색
            Q(comment__content__icontains=kw) |  # 답변 내용 검색
            Q(user__username__icontains=kw) |  # 게시글 글쓴이 검색
            Q(comment__user__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct() # 중복 제거

    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj,'page': page, 'kw': kw} 

    return render(request, 'boards/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'boards/post_detail.html', context)
