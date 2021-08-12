from django.shortcuts import render

# Create your views here.

# ROOT 폴더의 settings는 어떤 앱(라우팅), 라이브러리와 연결되는지
# 각 기능별 앱에서는 models.py : 데이터베이스, urls.py : 라우팅, view.py : html 과 연결되는 부분
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST["article_pk"])
        # commentapp/craete.html 에서 hidden 으로 보낸 pk 값으로 게시글을 저장하는 db 인 Article 에서 해당 게시글을 찾아서 저장
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})  # object=comment, artilce의 pk


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

