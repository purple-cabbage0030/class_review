# board/urls.py
from django.urls import path
from django.views.generic import DetailView
from .models import Post

app_name = 'board'
urlpatterns = [
    path('detail/<int:pk>', DetailView.as_view(model=Post, template_name='board/post_detail.html'), name='detail'),
]