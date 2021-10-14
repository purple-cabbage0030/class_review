# board/urls.py
from django.urls import path
from django.views.generic import DetailView
from .models import Post
from . import views

app_name = 'board'
urlpatterns = [
    path('detail/<int:pk>', DetailView.as_view(model=Post, template_name='board/post_detail.html'), name='detail'),
    path('create', views.PostCreateView.as_view(), name='create'),   # 글 등록 url 매핑
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update'),   # 글 수정 url 매핑 - get방식일 때 수정할 글의 pk값을 path 파라미터로 전송
    path('delete/<int:post_id>', views.delete_post, name='delete'),
    path('list', views.PostListView.as_view(), name='list'),
]