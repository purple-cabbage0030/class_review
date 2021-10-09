from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, View, DetailView

from .models import Question, Choice


# 설문 목록(list) 보기 처리 view class
# 목록(list)와 관련된 view는 ListView를 상속 받아서 구현
class QuestionListView(ListView):
    model = Question   # 전체 데이터를 조회할 모델 클래스를 설정
    template_name = 'poll/list.html'   # 응답할 template 파일 경로를 지정
    # 조회 결과를 template에 전달하는 데이터(dict) = context_data / context_object
    # 똑같은 데이터를 두 개의 이름으로 보내줌 - 1) object_list / 2) 모델클래스이름_list(클래스이름은 소문자로 변경)
    # 원하는 이름 지정: context_object_name = '원하는이름'

# 투표 작업 처리하는 view
# 동일한 url 요청
#   - get 방식: form을 전달
#   - post 방식: 투표 처리
class VoteView(View):
    # get 요청 처리 메소드
    def get(self, request, *args, **kwargs):
        # **kwargs: path parameter를 조회
        question_id = kwargs['question_id']
        try:
            question = Question.objects.get(pk=question_id)   # get(): 1개 조회. 조회결과가 없거나 2개 이상인 경우 exception 발생
            return render(request, 'poll/vote_form.html', {'question':question})
        except:
            # 없는 question id로 조회한 경우
            return render(request, 'poll/error_page.html', {'error_message':'없는 설문 번호를 요청했습니다.'})

    # post 요청 처리 메소드
    def post(self, request, *args, **kwargs):
        # 요청 파라미터 조회: choice의 id(choice라는 이름으로 넘어옴), question_id
        # choice_id = request.POST['choice']
        choice_id = request.POST.get('choice')
        question_id = request.POST['question_id']   # kwargs['question_id']로 받아도 됨

        # 요청 파라미터 검증(validation) - 필수 요청 파라미터가 잘 전송되었는지 체크
        if choice_id == None:   # 보기를 선택하지 않고 투표버튼 누른 경우 => vote_form.html 호출
            question = Question.objects.get(pk=question_id)
            return render(request, 'poll/vote_form.html', {'question':question, 'error_message':'보기를 선택하세요'})

        # print('vote(): ', choice_id, question_id)
        # Choice를 update - 요청 파라미터로 넘어온 선택된 choice의 id값을 이용 -- update choice set vote=vote+1 where id=선택된id
        # choice 조회 -> vote 값 변경 -> save()
        choice = Choice.objects.get(pk=choice_id)
        choice.vote += 1
        choice.save()

        # url = f"/poll/vote_result/{question_id}"
        url = reverse('poll:vote_result', args=[question_id])   # ('app_name:path_name', args=[path 파라미터에 전달할 값, ...])
        print('--------------------------redirect url:', url)
        return redirect(to=url)

# DetailView: 특정 모델의 primary key 값을 path parameter로 받아서 조회한 결과를 template에 전달하면서 호출
# pk를 받는 path parameter: urls.py에 등록 시 'url경로/<타입:pk>' 로 지정
# context data의 name
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'poll/vote_result.html'
    # 똑같은 데이터를 두 개의 이름으로 보내줌 - 1) object / 2) 모델클래스이름(클래스이름은 소문자로 변경)
    # 원하는 이름 지정: context_object_name = '원하는이름'