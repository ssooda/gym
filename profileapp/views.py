from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile  # 어떤 테이블에서 객체 리스트를 가져올 것인지 정해주기
    context_object_name = 'target_profile'  # 탬플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    form_class = ProfileCreationForm  # 어떤 form 을 사용할 것인지 (user 빼고 나머지 필드만 자동으로 생성됨 : ModelForm 사용해서)
    # success_url = reverse_lazy('accountapp:detail')  # reverse_lazy 는 연결을 편하게 => url과 연결
    template_name = 'profileapp/create.html'  # 탬플릿 파일 위치 지정 (templates라는 폴더 안에서의 경로: templates>profileapp)

    # model 에 있는 user 은 ProfileCreationForm 에서 다루지 않고 여기서 다룸
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # form 에는 form 으로 보낸 데이터가 들어가있음 (현재는 user 정보는 없음)=> commit=False 임시로 저장
        temp_profile.user = self.request.user  # temp_profile 즉 지금 form 으로 정보를 보낸 것의 user 는 현재 요청을 보낸 당사자로 지정
        temp_profile.save()  # 최종적으로 저장
        return super().form_valid(form)

    # success_url 로 보내려는 url 에 <int:pk>를 넣어주기 위해서
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
    # 이 클래스에서 object 가 가리키는 건 model 인 Profile 임
    # Profile.user 의 pk


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")  # 클래스에 데코레이터 추가할 때는 method_decorator
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    # 현재 보고 있는 사용자의 profile 은 Profile 이라는 db 에 저장되어있고, 이 사람은 탬플릿에서 target_profile 로 지칭함
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
