from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# method_decorator 은 배열 내에 있는 모든 데코레이터를 확인
has_ownership = [account_ownership_required, login_required]


# Function Based View


@login_required  # 데코레이터: 로그인이 안 된 경우 로그인 창으로 돌아가도록
def hello_world(request):  # view 에서 만든 함수를 urls 에서 routing
    # return HttpResponse("hello world")
    # HttpResponse 는 직접 view 단을 만드는 것임

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')  # html 에서 name 이 hello_world_input

        new_hello_world = HelloWorld()  # 데이터베이스를 연결한 HelloWorld 라는 클래스의 새로운 객체(new_hello_world)를 만듦
        new_hello_world.text = temp  # 해당 객체의 text 라는 필드에 temp를 대입
        new_hello_world.save()  # db에 데이터를 저장

        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # render : 파이썬 폴더에서 직접 view 단을 만드는 것이 아니라 요청이 있을 때 보여줄 html 파일을 연결하는 것 context : 데이터 꾸러미 {'text': 'POST
        # method'} text 라는 이름을 가지고 있고 내용은 POST method! => html에서 {{ text }}로 사용할 수 있음 render 로 html 파일을 연결해주려면 ROOT
        # 폴더의 settings.py 에서 TEMPLATES 'DIRS': [os.path.join(BASE_DIR, 'templates')] 을 명시해줘야함

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # reverse : accountapp의 urls.py 에서 만들어 두었던 accountapp 과 hello_world 만으로도 해당 html로 갈 수 있도록
        # HttpResponseRedirect : 재연결 => method가 post인 현재페이지에서 새로고침을 하더라도 method가 post인 페이지로 연결되는 것이 아니라
        # get 인 페이지로 연결 될 수 있도록 함

    else:
        hello_world_list = HelloWorld.objects.all()  # HelloWorld 클래스와 연결되어 있는 db의 모든 내용을 긁어옴
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


def home(request):
    return HttpResponseRedirect(reverse('accountapp:home'))

# Class Based View



class AccountCreateView(CreateView):  # 회원가입
    model = User  # 장고에서 기본적으로 제공하는 model
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')  # 함수형에서는 reverse, 클래스형에서는 reverse_lazy
    template_name = 'accountapp/create.html'  # 어떤 html 로 연결할지 template 지정 => 함수형에서 return render 와 같은 역할



class AccountDetailView(DetailView):  # 개인 페이지
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):  # 회원정보 수정
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):  # 회원탈퇴
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
