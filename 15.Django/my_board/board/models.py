# board/models.py
from django.db import models
from account.models import CustomUser

# 모델 클래스 정의 후 admin.py에 등록해야 관리자 앱에서 관리 가능
# python manage.py makemigrations
# python manage.py migrate

# category
# 게시글의 카테고리
# category_id: PK, 자동 증가 정수
# category_name: varchar, 카테고리 이름
class Category(models.Model):
    # Model Field(테이블 컬럼) 클래스 변수 선언
    category_id = models.AutoField(primary_key=True)   # AutoField: 1씩 자동 증가하는 정수형 컬럼
    category_name = models.CharField(max_length=200, verbose_name='카테고리명')   # verbose_name: 필드가 화면에 나올 때 사용할 label값(등록/수정/조회 시 보여질 label값)

    def __str__(self):
        # 출력되는 값 설정
        return self.category_name

    class Meta:
        ordering=['category_id']   # 기본 정렬방식 지정


# 게시글
# id(pk), title(글제목), content(글내용), category, create_at(처음등록일시), update_at(글수정일시) + writer(작성자-로그인한 사용자의 pk), up_file, up_image(업로드된 파일/이미지 정보)
class Post(models.Model):
    # 글 작성자: 글 쓴 사용자의 pk -> CustomUser를 Foreign key로 참조
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='작성자')


    title = models.CharField(max_length=255, verbose_name='글 제목')   # not null -> null/none/빈 문자열은 비허용
    content = models.TextField(verbose_name='글 내용')   # TextField: 대용량 text
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)   # nullable 컬럼, 빈 문자열 허용 컬럼으로 설정(blank는 form 검증과 관련)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일시')   # auto_now_add: insert할 때만 일시를 자동 입력
    update_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')   # auto_now=True: insert/update할 때 일시를 자동 입력


    def __str__(self):
        return f"{self.id}. [{self.category.category_name}] {self.title}"

    class Meta:
        ordering=['-id']   # id 내림차순 정렬