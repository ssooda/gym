from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # on_delete => User 가 탈퇴하면 게시글이 사라지는 것이 아니라 알 수 없음
    # User 객체에서 article 에 접근할 때 쓰는 이름 User.article 이런 식을 해야하니까? 음 이게 user.article 인건가?

    title = models.CharField(max_length=200, null=True)  # null=True : 없어도 됨
    image = models.ImageField(upload_to='article/', null=False)  # 이미지는 media 의 하위폴더 인 article 에 저장됨
    content = models.TextField(null=True)
    location = models.CharField(max_length=100, null=False)

    created_at = models.DateField(auto_now_add=True, null=True)


# python manage.py makemigrations
# python manage.py migrate