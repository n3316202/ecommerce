from django.shortcuts import render

from boards.models import Post

# Create your views here.
# -기호가 붙으면 역방향 정렬을, 없으면 순방향 정렬을 의미한다. 게시물은 보통 최신순으로 보므로 작성일시를 역순으로 정렬했다.
def index(request):
    post_list = Post.objects.order_by('-created_at') 
    context = {'post_list': post_list}
    return render(request, 'boards/post_list.html', context)

def for_loop(request):
    post_list = Post.objects.all
    #context = {'post_list': post_list}
    #추가
    name = {'name':'jaewon', 'age':99, 'location':'seoul', 'isman':True}
    price = [100,200,300]

    return render(request, 'boards/for_loop.html', {'post_list': post_list,'name' : name, 'price':price})