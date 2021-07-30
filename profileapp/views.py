from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile  # 어떤 테이블에서 객체 리스트를 가져올 것인지 정해주기
    context_object_name = 'target_profile'  # 탬플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    form_class = ProfileCreationForm  # 어떤 form 을 사용할 것인지
    success_url = reverse_lazy('accountapp:hello_world')  # reverse_lazy 는 연결을 편하게 => url과 연결
    template_name = 'profileapp/create.html'  # 탬플릿 파일 위치 지정 (templates라는 폴더 안에서의 경로: templates>profileapp)

    # model 에 있는 user 은 ProfileCreationForm 에서 다루지 않고 여기서 다룸
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # form 에는 form 으로 보낸 데이터가 들어가있음 => 임시로 저장
        temp_profile.user = self.request.user  # temp_profile 즉 지금 form으 으로 정보를 보낸 것의 user 는 현재 요청을 보낸 당사자로 지정
        temp_profile.save()  # 최종적으로 저장
        return super().form_valid(form)

