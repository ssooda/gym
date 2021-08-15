# account 의 경우에는 별도의 forms 를 안 만들어도 괜찮았지만 대부분 forms 파일을 별도로 만들어야한다
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):  # model 에 있는 정보를 바탕으로 form 을 만들어줌
    class Meta:
        model = Article
        fields = ['title', 'content', 'project', 'image']  # 이 3 가지를 입력 받을 수 있는 model form 을 만들어줌
        # writer 은 서버에서

