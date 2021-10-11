from django.urls import path

# view 모듈 import
from . import views

# 요청 url과 함수 매핑 => urlpatterns 변수의 리스트에 등록
app_name = 'poll'   # name space/prefix
# urlpatterns = [
#     path('list', views.QuestionListView.as_view(), name='list'),   # poll/list 요청 시 views.QuestionListView 호출
#     path('vote/<int:question_id>', views.VoteView.as_view(), name='vote'),   # poll/vote_form 요청 시 views.VoteView 호출
#     path('vote_result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result'),
# ]




# View클래스.as_view():
#   1. view클래스의 객체를 생성해서 등록(장고 실행환경)
#      - class 변수를 이용해 설정들만 할 경우에 그 설정을 as_view()메소드에 지정할 수 있다.
#   2. list url 요청이 들어오면 1에서 생성된 객체의 dispatch()메소드를 호출
#      - dispatch() - GET 요청일 경우 get()메소드, POST 요청일 경우 post()메소드 호출

from .models import Question
from django.views.generic import ListView, DetailView
urlpatterns = [
    path('list', ListView.as_view(model=Question, template_name='poll/list.html'), name='list'),
    path('vote/<int:question_id>', views.VoteView.as_view(), name='vote'),
    path('vote_result/<int:pk>', DetailView.as_view(model=Question, template_name='poll/vote_result.html'), name='vote_result'),
]


# 사용자 요청 url = http://ip:port/resource_path
# urls.py에 등록하는 부분 = resource_path
# resource_path = app_root/나머지path
# config.urls에는 app_root(poll/)만 지정, poll/urls.py에서 나머지path 지정 
# poll/urls.py에서 view함수와 url 매핑 작업