
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)  # 사용자가 작성한 form(writer 제외)을 일시적으로 저장
        temp_article.writer = self.request.user  # writer 에 요청한 사용자를 대입
        temp_article.save()  # 최종적으로 저장

        return super().form_valid(form)

    def get_success_url(self):  # 성공한 경우 넘겨줄 url 이 개별 게시글 마다 고유한 아이디를 포함할 때
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    # CreateView 에는 object 가 없고 DetailView 에는 form 이 없는데 게시글 밑에 댓글 넣는 form 을 두고 싶으면
    # FormMixin 을 상속받고 form_class 를 지정해주면 된다
    context_object_name = 'target_article'  # html 에 target_article 로 넘겨줌
    template_name = 'articleapp/detail.html'  # html 연결
    # detailview 에서는 form이 없고 createview 에서는 context 가 없다
    # But 상세보기 페이지에서 댓글을 달고 싶으면 Form 이 필요하다 => Mixin 기능을 사용해야함





@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'  # html 에 target_article 로 넘겨줌
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'


    def get_success_url(self):  # 성공한 경우 넘겨줄 url 이 개별 게시글 마다 고유한 아이디를 포함할 때
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):  # listview : 여러 객체를 다룸
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 25


