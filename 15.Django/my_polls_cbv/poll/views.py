from django.shortcuts import redirect, render
from django.urls import reverse   # urls.py에 등록된 path이름을 이용해 url생성하는 함수
# 모델 클래스 import
from .models import Question, Choice
'''
View: 특정 사용자 요청을 처리하는 모듈(work flow). 기능별로 작성.
view 함수
    1. 사용자가 전송한 파라미터(요청(request)/path 파라미터) 조회
    2. 사용자가 전송한 파라미터 검증(validation)
        - 필수 파라미터의 전송 여부 확인
        - 값 확인(데이터 타입, 범위, 글자수, etc.)
        - 검증 실패할 경우 Error처리 페이지로 이동
    3. Business 로직 처리 -> 사용자가 요청한 작업 처리
        - DB 작업은 Model 호출
    4. 처리 결과를 응답
        - template 호출(render()), 또는 다른 view를 호출(redirect())
'''

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

    try:
        question = Question.objects.get(pk=question_id)   # get(): 1개 조회. 조회결과가 없거나 2개 이상인 경우 exception 발생
        return render(request, 'poll/vote_form.html', {'question':question})
    except:
        # 없는 question id로 조회한 경우
        return render(request, 'poll/error_page.html', {'error_message':'없는 설문 번호를 요청했습니다.'})

# 투표 처리 View함수
# 요청 파라미터 조회 - post/get에 따라 달라짐 (기본적으로 dict 형태로 옴)
# post방식 요청 처리: request.POST['name'], request.POST.get('name')  (name=요청파라미터의 name)
# get방식 요청 처리: request.GET['name'], request.GET.get('name')
# [] 조회: 없는 name으로 조회할 경우 exception 발생
# .get() 조회: 없는 name으로 조회할 경우 default(None)값 반환
def vote(request):
    # 요청 파라미터 조회: choice의 id(choice라는 이름으로 넘어옴), question_id
    # choice_id = request.POST['choice']
    choice_id = request.POST.get('choice')
    question_id = request.POST['question_id']

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

# 개별 설문의 결과를 보여주는 view
def vote_result(request, question_id):
    # Question을 select - 요청 파라미터로 넘어온 question_id 이용(hidden input) -- select * from question where id=질문id
    question = Question.objects.get(pk=question_id)
    # 응답 처리
    return render(request, 'poll/vote_result.html', {'question':question})