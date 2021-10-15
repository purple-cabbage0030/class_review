from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm   # 로그인 form: username, password

from .forms import CustomUserCreationForm

# 가입처리 view
# class UserCreateView(CreateView):
#     template_name = 'account/join_form.html'   # GET방식 요청 시 이동할 가입 폼 템플릿
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')   # POST방식 요청 시 가입 처리 성공 후 redirect방식으로 이동할 url

# 로그인 처리 view
# class UserLoginView(LoginView):
#     template_name = 'account/login_form.html'   # Get방식 요청 시 이동할 로그인 폼 템플릿
#     form_class = AuthenticationForm
    # POST방식 요청 시 로그인 처리, 성공 후 settings.py의 LOGIN_REDIRECT_URL에 설정된 url로 이동

# 로그아웃 처리 view - LogoutView 사용: 추가적으로 정의할 것 없음. urls.py에 직접 등록
# class UserLogoutView(LogoutView):
#     pass
