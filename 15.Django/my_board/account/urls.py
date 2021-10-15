from django.urls import path

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm   # 로그인 form: username, password

from .forms import CustomUserCreationForm

# from . import views

app_name = 'account'
urlpatterns = [
    # path('join', views.UserCreateView.as_view(), name='join'),
    path('join', CreateView.as_view(template_name = 'account/join_form.html', form_class = CustomUserCreationForm,\
        success_url = reverse_lazy('home')), name='join'),
    # path('login', views.UserLoginView.as_view(), name='login'),
    path('login', LoginView.as_view(template_name = 'account/login_form.html', form_class = AuthenticationForm),\
         name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]