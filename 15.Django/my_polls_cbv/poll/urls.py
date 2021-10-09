from django.urls import path

# view 모듈 import
from . import views

# 요청 url과 함수 매핑 => urlpatterns 변수의 리스트에 등록
app_name = 'poll'   # name space/prefix
urlpatterns = [
    path('list', views.QuestionListView.as_view(), name='list'),   # poll/list 요청 시 views.QuestionListView 호출
    path('vote/<int:question_id>', views.VoteView.as_view(), name='vote'),   # poll/vote_form 요청 시 views.VoteView 호출
    path('vote_result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result'),
]


# 사용자 요청 url = http://ip:port/resource_path
# urls.py에 등록하는 부분 = resource_path
# resource_path = app_root/나머지path
# config.urls에는 app_root(poll/)만 지정, poll/urls.py에서 나머지path 지정 
# poll/urls.py에서 view함수와 url 매핑 작업