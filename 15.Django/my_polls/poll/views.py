from django.shortcuts import redirect, render
# 모델 클래스 import
from .models import Question, Choice

# View: 특정 사용자 요청을 처리하는 모듈(work flow). 기능별로 작성.
# 질문 목록을 보여주는 View함수
# 1. DB에서 질문 목록 조회
# 2. 응답 화면을 생성해서 반환 -> template 사용

# view함수 : 이름 지정은 자유. 첫번째 매개변수는 무조건 HttpRequest를 받는 변수로 지정.
# view함수를 poll/urls.py에 등록 -> 사용자 요청 url과 view함수를 매핑
def list(request):
    q_list = Question.objects.all()   # db에서 전체 설문 데이터를 select

    # 응답 처리
    response = render(request, 
                    'poll/list.html',  # 응답 처리할 template 파일 -> poll/templates/poll/list.html
                    {'question_list':q_list})   # template에 전달할 값 (dict)

    return response

# vote_form 처리 View함수
# 매개변수: 1. HttpRequest, 2. question_id: Path parameter로 전달된 질문 id를 받을 변수
def vote_form(request, question_id):
    print('vote_form(): question_id', question_id)
    # question_id로 Question, Choice 조회해서 template으로 전달

    question = Question.objects.get(pk=question_id)

    return render(request, 'poll/vote_form.html', {'question':question})

# 투표 처리 View함수
# 요청 파라미터 조회 - post/get에 따라 달라짐 (기본적으로 dict 형태로 옴)
# post방식 요청 처리: request.POST['name'], request.POST.get('name')  (name=요청파라미터의 name)
# get방식 요청 처리: request.GET['name'], request.GET.get('name')
# [] 조회: 없는 name으로 조회할 경우 exception 발생
# .get() 조회: 없는 name으로 조회할 경우 default(None)값 반환
def vote(request):
    # 요청 파라미터 조회: choice의 id(choice라는 이름으로 넘어옴), question_id
    choice_id = request.POST['choice']
    question_id = request.POST['question_id']
    print('vote(): ', choice_id, question_id)
    # Choice를 update - 요청 파라미터로 넘어온 선택된 choice의 id값을 이용 -- update choice set vote=vote+1 where id=선택된id
    # choice 조회 -> vote 값 변경 -> save()
    choice = Choice.objects.get(pk=choice_id)
    choice.vote += 1
    choice.save()

    url = f"/poll/vote_result/{question_id}"
    print('redirect url:', url)
    return redirect(to=url)

# 개별 설문의 결과를 보여주는 view
def vote_result(request, question_id):
    # Question을 select - 요청 파라미터로 넘어온 question_id 이용(hidden input) -- select * from question where id=질문id
    question = Question.objects.get(pk=question_id)
    # 응답 처리
    return render(request, 'poll/vote_result.html', {'question':question})