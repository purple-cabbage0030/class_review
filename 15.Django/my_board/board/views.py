# board/views.py
from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy   # urls.py에 등록된 path의 이름으로 url을 만들어서 반환하는 함수

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

# 글 수정 view -> UpdateView를 상속해서 정의
# 1) 수정 폼 제공 2) 수정 처리
class PostUpdateView(UpdateView):
    template_name = 'board/post_update.html'   # 수정 폼 template 경로 - Get방식 요청 시 이동
    form_class = PostForm   # 사용할 Form 클래스 설정
    model = Post   # updateview에서는 form class, model 둘 다 설정해야 함 - get 요청 시 수정할 데이터를 조회해서 넘겨주기 위해 model 설정

    def get_success_url(self):   # 수정 처리 후 redirect 방식으로 이동할 url을 반환
        return reverse_lazy('board:detail', args=[self.object.pk])
        # self.object: update된 model 객체

# 글 삭제 view -> 함수형으로
# CBV일 경우 DeleteView 상속받아서 - template_name='삭제확인페이지' (get방식 요청 시 처리), success_url='삭제 후 이동할 view url' (post방식)
def delete_post(request, post_id):
    """
    path 파라미터로 삭제할 게시물의 id를 받아서 삭제 처리
    """
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/')   # 삭제 후 home으로 이동

# 글 목록 보기 -> ListView 상속
# Post.objects.all() 조회한 후 template_name의 페이지로 이동하면서 데이터를 context_data(name: object_list, post_list)로 전달
class PostListView(ListView):
    template_name = 'board/post_list.html'   # 목록 페이지 (응답 페이지)
    model = Post   # 데이터를 조회할 Model클래스 지정
    paginate_by = 10   # 한번에 10개씩만 조회하도록 설정 - http://127.0.0.1:8000/board/list?page=번호

# def list(request):
    # p_list = Post.objects.all()
    # return render(request, 'template', {'object_list':p_list})