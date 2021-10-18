# board/views.py
from django.core import paginator
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy   # urls.py에 등록된 path의 이름으로 url을 만들어서 반환하는 함수

# 함수형 view에 설정할 decorator: 로그인 여부를 체크해서 로그인 안 된 상태에서 요청 시에 settings.py의 LOGIN_URL에 등록된 url로 이동.
from django.contrib.auth.decorators import login_required
# 클래스의 메소드에 decorator를 선언할 수 있도록 돕는 class decorator
from django.utils.decorators import method_decorator

from django.contrib.auth import get_user
# 요청을 보낸 (로그인한) 사용자의 User 모델 객체를 반환
# view에서 로그인한 사용자의 정보를 조회할 때 이 함수를 이용하면 간단하게 적용할 수 있다

from .models import Post
from .forms import PostForm

# 1개 게시물을 조회하는 view
# urls.py에 직접 등록 가능
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'board/post_detail.html'

# 글 inser하는 view -> CreateView를 상속해서 정의
# 1) 등록폼 제공 2) 등록 처리
# CreateView()가 post방식으로 들어온 요청 파라미터의 값을 검증하고, DB에 insert한다. 그 후 redirect까지 처리.

# dispatch: 클래스 기반 뷰는 사용자 요청이 들어오면 장고 실행환경이 dispatch()메소드를 호출함
# dispatch는 get요청일 경우 get(), post 요청일 경우 post() 메소드를 호출함 --> dispatch()메소드는 view의 시작 단계
@method_decorator(login_required, name="dispatch")   # dispatch()라는 메소드에 login_required 데코레이터를 적용
class PostCreateView(CreateView):
    template_name = 'board/post_create.html'   # 입력 폼 - GET방식 요청일 경우 이동(render)할 template
    form_class = PostForm   # 등록 시 사용할 Form 클래스 설정
    # success_url = reverse_lazy("board:detail")   # 등록 처리 후 이동할(redirect) url 등록 - 새로고침 방지
    # 그냥 변수로 주면 아직 등록이 안 된 model 객체의 pk값을 가져올 수 없어서 get_success_url 메소드를 사용한다
    # 패스 파라미터가 없으면 그냥 변수로 url값 줘도 됨

    # redirect()할 url을 만들 때 단순히 urls.py의 path이름만 사용할 경우: success_url에 등록
    # insert/update한 model객체의 속성값을 path파라미터로 전송해야 하는 경우: get_success_url()을 overriding
    # url 생성 시에는 reverse_laze() 사용. reverse()는 함수형 view에서만 사용한다.
    def get_success_url(self):
        return reverse_lazy('board:detail', args=[self.object.pk])
        # self.object: insert된 model 객체

    def form_valid(self, form):
        """
        form_valid(): CreateView, UpdateView에 정의된 메소드 (form을 사용하는 경우 다 이 메소드 가지고 있다)
        POST방식으로 요청이 들어왔을 때 요청파라미터를 검증(is_valid())한 뒤에 호출되는 메소드
        요청파라미터로 전달된 값들을 DB에 insert/update 처리 로직이 구현되어 있음
        - 요청파라미터들을 저장하기 전이나 후에 추가적으로 처리해야할 것이 있으면 overriding한다.
        - 글 등록 시 사용자가 입력한 글 제목, 내용, 카테고리에 글을 작성한 (로그인한) 사용자의 CustomUser모델을 writer에 넣는 작업 추가

        [매개변수]
            form: 요청파라미터 검증을 통과한 값들을 가진 ModelForm

        ModelForm객체의 모델 field 조회
            - ModelForm객체.cleaned_data 속성: 사용자가 입력한 값을 딕셔너리로 반환 (ModelForm.title 이런 직접 조회 불가)
        
        ModelForm객체의 모델 field 값 변경
            - ModelForm을 Model로 변경 후 처리
            - ModelForm객체.save([commit=False]): ModelForm의 요청파라미터를 연결된 Model을 이용해서 insert/update한 후의 Model객체를 반환. commit=False 지정 시 실제 DB에는 저장되지 않음(임시 저장, 모델을 가져오는 역할만)
        """
        # form: title, content, category (사용자가 입력한 값) <= writer를 추가
        post_model = form.save(commit=False)   # Model 객체 가져오기
        post_model.writer = get_user(self.request)   # 로그인한 사용자를 조회해서 모델의 writer에 추가
        # GenericView의 메소드에서 HttpRequest 객체 사용 시 항상 self.request로 호출
        return super().form_valid(form)   # db에 저장하는 작업(update & commit처리 = post_model.save()) 알아서 수행

# 글 수정 view -> UpdateView를 상속해서 정의
# 1) 수정 폼 제공 2) 수정 처리
@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    template_name = 'board/post_update.html'   # 수정 폼 template 경로 - Get방식 요청 시 이동
    form_class = PostForm   # 사용할 Form 클래스 설정
    model = Post   # updateview에서는 form class, model 둘 다 설정해야 함 - get 요청 시 수정할 데이터를 조회해서 넘겨주기 위해 model 설정

    def get_success_url(self):   # 수정 처리 후 redirect 방식으로 이동할 url을 반환
        return reverse_lazy('board:detail', args=[self.object.pk])
        # self.object: update된 model 객체

# 글 삭제 view -> 함수형으로
# CBV일 경우 DeleteView 상속받아서 - template_name='삭제확인페이지' (get방식 요청 시 처리), success_url='삭제 후 이동할 view url' (post방식)
@login_required   # 함수형 view는 login_required 데코레이터를 직접 적용한다
def delete_post(request, post_id):
    """
    path 파라미터로 삭제할 게시물의 id를 받아서 삭제 처리
    """
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/board/list')   # 삭제 후 home으로 이동

# 글 목록 보기 -> ListView 상속
# Post.objects.all() 조회한 후 template_name의 페이지로 이동하면서 데이터를 context_data(name: object_list, post_list)로 전달
# pagenate_by - 페이징 처리 => Paginator 객체를 생성해서 context data로 저장
# 페이지번호 링크 처리를 위한 값들을 context data의 Paginator 객체로 추출한 뒤 template에 전달
class PostListView(ListView):
    template_name = 'board/post_list.html'   # 목록 페이지 (응답 페이지)
    model = Post   # 데이터를 조회할 Model클래스 지정
    paginate_by = 10   # 한번에 10개씩만 조회하도록 설정 - http://127.0.0.1:8000/board/list?page=번호

# def list(request):
    # p_list = Post.objects.all()
    # return render(request, 'template', {'object_list':p_list})

    # context data: view가 template에 전달하는 값들을 모아 둔 dictionary
    # get_context_data() 메소드: 모든 generic view에 정의된 메소드. View class들이 생성해서 전달하는 context data 이회에 추가적으로 전달할 값이 있을 경우 overriding
    def get_context_data(self, **kwargs):
        # 부모클래스에 정의된 get_context_data() 호출 - 반환값: context data dictionary
        # ListView: pagenate_by 설정 시 'paginator':Paginator객체 생성해서 context data에 제공
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_group_count = 10   # 한 페이지 그룹 당 페이지 수
        # HttpRequest 객체 조회: self.request
        current_page = int(self.request.GET.get('page', 1))   # 사용자가 요청한 페이지 번호(현재 페이지 그룹: ?page=번호 - 이 값을 조회), default=1

        # 현재 페이지가 속한 페이지 그룹의 페이지 범위(index: pn.page_range)
        start_idx = int((current_page-1)/page_group_count)*page_group_count
        end_idx = start_idx+page_group_count
        page_range = paginator.page_range[start_idx:end_idx]

        # 이전/다음 페이지 그룹이 있는지 여부 + 이전/다음 페이지 번호
        # 현재 페이지가 속한 page group이 이전 페이지(그룹)이 있는지 / 다음 페이지(그룹)이 있는지 => page group의 시작페이지/마지막 페이지 기준으로 찾는다 + 페이지 번호
        start_page = paginator.page(page_range[0])   # 시작 페이지의 page 객체
        end_page = paginator.page(page_range[-1])   # 마지막 페이지의 page 객체

        has_previous = start_page.has_previous()   # 시작 페이지의 이전 페이지 존재 여부 (True/False)
        has_next = end_page.has_next()   # 마지막 페이지의 다음 페이지 존재 여부

        # 조회 결과를 context data에 추가 => super().get_context_data(**kwargs)에서 리턴받은 context data 딕셔너리에 추가
        context['page_range'] = page_range
        if has_previous:
            context['has_previous'] = has_previous
            context['previous_page_no'] = start_page.previous_page_number()   # 시작 페이지의 이전 페이지 번호
        
        if has_next:
            context['has_next'] = has_next
            context['next_page_no'] = end_page.next_page_number()   # 마지막 페이지의 다음 페이지 번호

        return context   # overriding한 메소드에서 리턴한 context data dictionary가 template에 전달


