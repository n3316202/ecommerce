from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# -기호가 붙으면 역방향 정렬을, 없으면 순방향 정렬을 의미한다. 게시물은 보통 최신순으로 보므로 작성일시를 역순으로 정렬했다.
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    
    post_list = Post.objects.order_by('-created_at')
    
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj} 
    #context = {'post_list': post_list}

    return render(request, 'boards/post_list.html', context)

def for_loop(request):
    post_list = Post.objects.all
    #context = {'post_list': post_list}
    #추가
    name = {'name':'jaewon', 'age':99, 'location':'seoul', 'isman':True}
    price = [100,200,300]

    return render(request, 'boards/for_loop.html', {'post_list': post_list,'name' : name, 'price':price})

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'boards/post_detail.html', context)

def reply_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.comment_set.create(content=request.POST.get('content'))
    return redirect('boards:detail', post_id=post.id)

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
