from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='accounts:login')
def comment_create(request,post_id):
    """
    댓글 등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid(): # 폼이 유효하다면
            comment = form.save(commit=False) # 임시 저장하여 post 객체를 리턴받는다.
            comment.user = request.user
            comment.post = post
            comment.save()# 데이터를 실제로 저장한다.
            return redirect('boards:index')
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'post':post,'form': form}
    return render(request, 'boards/post_form.html', context)


@login_required(login_url='boards:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.user:
        messages.error(request, '수정권한이 없습니다')
        return redirect('boares:detail', comment_id=comment.post.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            #answer.modify_date = timezone.now()
            comment.save()
            return redirect('boards:detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'boards/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('boards:detail', post_id=comment.post.id)
    comment.delete()
    return redirect('boards:detail', post_id=comment.post.id)

@login_required(login_url='accounts:login')
def comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user == comment.user:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        comment.voter.add(request.user)
    
    return redirect('boards:detail', post_id=comment.post.id)