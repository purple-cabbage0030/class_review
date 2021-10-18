# board/forms.py - board에서 사용할 Form/Model을 구현할 모듈
from django import forms
from .models import Post

#  Form Field: 사용자로부터 입력받는 부분
#   - label, widget(입력양식), error message로 구성
# class PostForm(forms.Form):
#     title = forms.CharField()   # 텍스트를 입력 받는 input (input type='text')
#     content = forms.CharField(widget=forms.Textarea)   # textarea

# Form Field들을 모델을 이용해서 구현하는 form
#   + save(): insert/update 기능 사용 가능
class PostForm(forms.ModelForm):

    class Meta:
        model = Post   # form field를 만들 때 참조/save() 시 데이터를 저장할 model 클래스 지정
        # fields = '__all__'   # 모델의 field 중 form field로 사용할 field 목록 지정
        # fields = ['필드명',...]    # 몇 개만 선택할 경우
        exclude = ['writer']   # 몇 개만 뺄 경우 - Post의 field 중 writer를 제외한 나머지를 Form에서 사용