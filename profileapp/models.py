from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# db 만들기
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    island = models.TextField(null=True)  # max_length 지정 안 해도 됨, null=True 면 사용자가 지정 안 해도 괜찮음(default = False)
