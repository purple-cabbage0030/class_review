# board/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# 1개 게시물을 조회하는 view
# urls.py에 직접 등록 가능
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'board/post_detail.html'
