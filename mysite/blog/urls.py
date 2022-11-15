from django.urls import path, include
from . import views # views.py import 

urlpatterns = [ 
    path('test1/', views.test1),
    path('test2/<int:no>/', views.test2),
    path('', views.list),
    path('<int:id>/', views.detail)
]