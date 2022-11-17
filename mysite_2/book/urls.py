from django.urls import path, reverse_lazy
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book 

app_name = 'book'
urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'), # ListView.as_view : 모델과 키워드 인자값만 입력해주면 자동으로 데이터 가져와서 응답해주는 모듈
                                                         # as_view : Main entry point for a request-response process.
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'), # pk로 인자를 넘겨줘야 함
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'), # fields='__all__' : Book 모델에 있는 속성값 모두 사용
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
    path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse_lazy('book:list')), name='delete'), # 필수 옵션 : success_url=reverse_lazy('book:list'))
                                                                                                                 # success_url에 지정한 해당 url로 이동
                                                                # reverse_lazy는 클라이언트로부터 요청이 들어오고 실제 reverse가 실행시점에 실행됨
]
