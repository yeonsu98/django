from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def test1(request):
    # request : 클라이언트에게 urls.py에서 온 요청정보
    # 응답정보 내보내기
    return HttpResponse("hello!")

def test2(request, no):
    print(type(no))
    return HttpResponse(f'no : {no}')

def list(request):
    post_list = Post.objects.all()
    titles = ""
    for post in post_list:
        titles += post.title
    return HttpResponse(titles)

def detail(request, id):
    """
    try:
         post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Data doesn't exist")
    """
    post = get_object_or_404(Post, id=id)
    return HttpResponse(post.title)