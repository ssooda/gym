from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "projectapp/create.html"

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    # Artilce 에서는 기사(detail)와 밑에 댓글(입력가능한 form)이 같이 보일 수 있도록 FormMixin 사용
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:  # 유저가 로그인 되어있으면
            subscription = Subscription.objects.filter(user=user, project=project)  # 구독정보가 있는지 없는지 확인
            # filter(user=user, project=proejct) 이렇게 쓰는 것은 and function : user & project 값을 넘겨주는 것
            # 그렇다면 or, where 은 어떻게 쓰는 것일까?
            # Articles.objects.filter(project__in=projects) => 장고에서 말하는 Field Lookups(double underscore) =>
            # 이건 sql(db) 안에서 select where project in()이런 식으로 쓰임 목적은 복잡한 db 쿼리르 구현할 수 있도록 만들어 줌
            # sql+장고를 사용할 때 field lookup을 활용하면 복잡한 쿼리를 실행할 수 있다
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25

