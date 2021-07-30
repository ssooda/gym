from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# db 만들기
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Profile.user 을 profile 로 나타낸다
    image = models.ImageField(upload_to='profile/', null=True)  # media 폴더 하위 폴더로 profile 이 생김
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    island = models.TextField(blank=True, null=True)
    # TextField : max_length 지정 안 해도 됨, null=True, blank=True 면 사용자가 지정 안 해도 괜찮음(default = False)
    # 현재 null=True 지만 입력 안하면 입력하라고 함
# python manage.py makemigrations => migrations 폴더에 create model 이 됨 (현재 0001_initial.py)
# 파일을 만들고 나서 연동시켜주는 명령어도 입력해야함 python manage.py migrate

