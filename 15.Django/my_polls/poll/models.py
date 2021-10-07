from django.db import models

# Question(질문) 테이블과 연결된 모델 클래스
# question_text: 질문 내용 - varchar
# pub_date: 등록 일시 - datetime
# id(PK-자동생성): 1씩 자동 증가하는 값

# 모델 클래스
# models.Model을 상속
# 컬럼 관련 변수들을 class 변수로 정의 => Field
# class명: table명으로 지정/ Pascal 표기법 사용.
class Question(models.Model):
    # Field 클래스 변수: 변수명=컬럼명, 값=Field객체(데이터타입, 추가 설정)
    # Primary Key 생략 시 자동으로 id라는 이름의 정수형 컬럼 생성됨
    question_text = models.CharField(max_length=200)   # CharField: 문자열(varchar)
    pub_date = models.DateTimeField(auto_now_add=True)   # DateTimeField: 일시타입(Date) - auto_now_add: insert될 때의 일시를 자동으로 등록

    # initializer가 자동으로 만들어짐
    # def __init__(self, question_text="", pub_date=None):
    #     self.question_text = question_text
    #     self.pub_date = pub_date

    # 매직메소드
    def __str__(self):
        return self.question_text

# Choice - 보기
# choice_text: 보기 내용 - varchar
# vote: 몇 번 선택됐는지 - int
# question: 어떤 질문에 대한 보기인지 - Question의 Foreign Key
# id(PK-자동생성)
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.PositiveIntegerField(default=0)   # PositiveIntegerField: 정수 가운데 양수만
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)   # ForeignKey: ForeignKey필드 선언. to: 부모테이블, on_delete: 참조 데이터 삭제 시 어떻게 할지(cascade- 같이 지워라)


    # 매직메소드
    def __str__(self):
        return self.choice_text

# 모델 클래스 작성/변경 시 makemigrations - DB에 테이블을 어떻게 만들지 정의
# python manage.py migrate - DB에 테이블 생성, 변경