# account/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# UserAdmin: 관리자 앱에서 사용자 관리를 위한 화면 구성
# 사용자 관리 화면 변경 시 UserAdmin을 상속받아서 구현(보통 user에만 사용)
class CustomUserAdmin(UserAdmin):
    # class 변수 변경
    # 사용자 수정화면의 '개인정보' 카테고리에 나올 Model Field 들을 선언
    UserAdmin.fieldsets[1][1]['fields'] = ('name', 'email', 'gender')

    # 사용자 목록 화면에 나올 field들을 정의
    list_display = ['username', 'name', 'email', 'date_joined', 'is_staff']



admin.site.register(CustomUser, CustomUserAdmin)
