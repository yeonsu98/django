from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import render
from .forms import *
from django.utils import timezone


def test1(request):
    return HttpResponse("blog/test1 응답!")

def test2(request, no):
    print('no 타입:', type(no))
    return HttpResponse(f'no:{no}')

def test3(request, year, month, day):
    return HttpResponse(f'년:{year}, 월:{month}, 일:{day}')

def test4(request):
    return render(request, 'blog/test4.html', {'score':70})

def test5(request):
    var ='''
    Miracles happen to only those who believe in them.
    Think like a man of action and act like man of thought.
    Courage is very important. Like a muscle, it is strengthened by use.
    Life is the art of drawing sufficient conclusions from insufficient premises.
    By doubting we come at the truth.
    A man that has no virtue in himself, ever envies virtue in others.
    When money speaks, the truth keeps silent.
    Better the last smile than the first laughter.
    '''
    return render(request, 'blog/test5.html', {'var':var})

def test6(request):
    d1 = timezone.now()
    d2 = timezone.datetime(2001,3,19)
    d3 = timezone.datetime(2030,3,19)
    return render(request, 'blog/test6.html', {'date1':d1, 'date2':d2, 'date3':d3})


def test7(request):
    print('요청방식 : ', request.method)
    print('GET방식으로 전달된 질의 문자열 :', request.GET)
    print('Post방식으로 전달된 질의 문자열 :', request.POST)
    print('업로드 파일 : ', request.FILES)
    return render(request, 'blog/form_test.html')


def list(request):
    search_key = request.GET.get('keyword', '')
    post_list = Post.objects.all()
    if search_key :
        post_list = post_list.filter(title__icontains=search_key) # icontains : 대소문자 구분 안하고 contains 된 거 찾기
    return render(request, 'blog/list.html', {'post_all':post_list})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_list = post.comment_set.all() # join, 1에 해당하는 comment만 가져오기
    return render(request, 'blog/detail.html',{'post':post, 'comment_all':comment_list})

def post_create(request): # 새로운 게시글 등록, 요청방식으로 구분
    # get : PostForm 형식을 화면에 보여주기, 템플릿 페이지 보여주기
    # post : post 테이블에 insert
    if request.method=='POST':
        form = PostModelForm(request.POST)
        if form.is_valid(): # 데이터 유효성 검사
            print(form.cleaned_data) # is_valid 하면 만들어지는 메소드 cleaned_data
            # post = Post.objects.create(**form.cleaned_data) # 아래와 같은 결과
            post = form.save() # (form 사용으로 간단하게) 위와 같은 결과 : 모델 인스턴스 생성 및 데이터 바인딩 -> 모델 인스턴스.save() -> 모델 인스턴스 리턴
            return redirect(post) # insert 후의 insert한 데이터 페이지로 이동
    else: # GET 방식
        form = PostModelForm() # form 만들어주기
        return render(request, 'blog/post_form.html', {'form':form})

def post_update(request, id):
    post = Post.objects.get(id=id)
    if request.method=='POST':
        form = PostModelForm(request.POST, instance=post) # 가져온 다음에 저장 => 수정
        if form.is_valid(): # 데이터 유효성 검사
            print(form.cleaned_data) 
            post = form.save() # (form 사용으로 간단하게) 위와 같은 결과 : 모델 인스턴스 생성 및 데이터 바인딩 -> 모델 인스턴스.save() -> 모델 인스턴스 리턴
            return redirect(post) # insert 후의 insert한 데이터 페이지로 이동
    else: # GET 방식
        form = PostModelForm(instance=post) # form 양식 만들고 이 안에 필드에 맞게끔 값을 넣기
        return render(request, 'blog/post_update.html', {'form':form})    
    

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete() # 인스턴스 1개 삭제 : 모델의 인스턴스.delete() 
                      # 전체 삭제 : Queryset.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post':post})