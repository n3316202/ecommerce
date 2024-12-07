from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='accounts:login')
def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid(): # 폼이 유효하다면
            post = form.save(commit=False) # 임시 저장하여 post 객체를 리턴받는다.
            post.user = request.user  # author 속성에 로그인 계정 저장
            post.save()# 데이터를 실제로 저장한다.
            return redirect('boards:index')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'boards/post_form.html', context)

@login_required(login_url='accounts:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.user != post.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('boards:detail', post_id=post.id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) 
        if form.is_valid():
            post = form.save(commit=False)
            #post.modify_date = timezone.now()  # 수정일시 저장
            post.save()
            return redirect('boards:detail', post_id=post.id)
    else:
        form = PostForm(instance=post) #GET 요청인 경우 질문수정 화면에 조회된 질문의 제목과 내용이 반영될 수 있도록 다음과 같이 폼을 생성해야 한다.
    
    context = {'form': form}
    return render(request, 'boards/post_form.html', context)

@login_required(login_url='accounts:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('boards:detail', post_id=post.id)
    post.delete()
    return redirect('boards:index')

@login_required(login_url='accounts:login')
def post_vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.user:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
    return redirect('boards:detail', post_id=post.id)