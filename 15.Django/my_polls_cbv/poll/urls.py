from django.urls import path

# view 모듈 import
from . import views

# 요청 url과 함수 매핑 => urlpatterns 변수의 리스트에 등록
app_name = 'poll'   # name space/prefix
urlpatterns = [
    path('list', views.list, name='list'),   # poll/list 요청 시 views.list()함수 호출
    path('vote_form/<int:question_id>', views.vote_form, name='vote_form'),   # poll/vote_form 요청 시 views.vote_form()함수 호출
    path('vote', views.vote, name='vote'),
    path('vote_result/<int:question_id>', views.vote_result, name='vote_result'),
]


# 사용자 요청 url = http://ip:port/resource_path
# urls.py에 등록하는 부분 = resource_path
# resource_path = app_root/나머지path
# config.urls에는 app_root(poll/)만 지정, poll/urls.py에서 나머지path 지정 
# poll/urls.py에서 view함수와 url 매핑 작업