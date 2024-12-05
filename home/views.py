from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def index(request):
    return render(request,"home/hello_world.html")

def ok(request):
    return HttpResponse("홈 OK 입니다")
