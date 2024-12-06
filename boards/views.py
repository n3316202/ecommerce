from django.http import HttpResponseNotAllowed
from django.utils import timezone   
from django.shortcuts import get_object_or_404, redirect, render

from boards.forms import CommentForm, PostForm
from boards.models import Comment, Post
from django.core.paginator import Paginator  
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

def post_create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid(): # 폼이 유효하다면
            post = form.save(commit=False) # 임시 저장하여 post 객체를 리턴받는다.
            #post.created_at = timezone.now()# 실제 저장을 위해 작성일시를 설정한다.
            post.save()# 데이터를 실제로 저장한다.
            return redirect('boards:index')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'boards/post_form.html', context)

def comment_create(request,post_id):
    """
    댓글 등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid(): # 폼이 유효하다면
            comment = form.save(commit=False) # 임시 저장하여 post 객체를 리턴받는다.
            #post.created_at = timezone.now()# 실제 저장을 위해 작성일시를 설정한다.
            comment.post = post
            comment.save()# 데이터를 실제로 저장한다.
            return redirect('boards:index')
    else:
        return HttpResponseNotAllowed('Only POST is possible.')

    context = {'post':post,'form': form}
    return render(request, 'boards/post_form.html', context)
