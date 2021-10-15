# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# 사용자 정의 User Model 정의
# 1) AbstractUser를 상속받아서 구현: 기존 AbstractUser Model(username/pasword) + 추가 필드 정의
# 2) settings.py에 이 클래스를 AUTH_USER_MODEL 변수에 등록
# 3) admin.py에 등록해서 관리자 화면 설정
# 기존 db.sqlite3 파일 삭제
# 4) python manage.py makemigrations, migrate

# username, password(상위클래스 기본제공) + name(이름), email, gender(성별)
class CustomUser(AbstractUser):
    # 추가할 model field들을 정의
    GENDER_CHOICE = [
        ['F', '여성'],   # <option value='F'>여성</option> --- [전송할값, 보여질값]
        ['M', '남성']
    ]
    name = models.CharField(max_length=100, verbose_name='이름')
    email = models.EmailField(max_length=100, verbose_name='이메일')
    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDER_CHOICE)

    def __str__(self):
        return f"{self.pk}. {self.name}"