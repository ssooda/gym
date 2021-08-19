from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    # redirectview : 유튜브 구독기능을 생각해보면 구독을 누른다고 페이지가 바뀌지 않음 요청을 받자마자 처리할 건 처리하고 리다이렉트 하도록!

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    # 프로젝트 앱 안에서 디테일 뷰에서 구독버튼을 누르도록 할 것이므로 돌아갈 페이지는 프로젝트 앱에서 디테일뷰임
    # porject_pk를 get 방식으로 받아서 이 pk 를 가지고 있는 디테일 페이지로 redirect(되돌아감)


    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        # project_pk 를 가지고 있는 project를 찾는데 없으면 404 status code 를 돌려주도록
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():  # 이미 구독한 사람이 또 클릭 한 거면 구독 취소
            subscription.delete()
        else:  # 구독 안 한 사람이 누른거면 구독
            Subscription(user=user, project=project).save()




        return super(SubscriptionView, self).get(request, *args, **kwargs)


