# accountapp 에는 미리 내장된 form 이 있지만 그게 아니면 만들어야함
# ModelForm : 기존에 있었던 Model(db) 을 Form 형식으로 변환해주는 기능
from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 사용자에게 입력받는 건 content 하나 뿐 ! 나머지는 다른 앱의 models.py 와 연결


# 모델을 만들고 난 다음에는 migration 작업
# python manage.py makemigrations
# python manage.py migrate

