from django.db import models

# Create your models here.


# class 하나가 db 에서 item 하나가 됨
class HelloWorld(models.Model):  # Model 클래스 상속
    text = models.CharField(max_length=255, null=False)
# python manage.py makemigrations => migrations 폴더에 create model 이 됨 (현재 0001_initial.py)
# 파일을 만들고 나서 연동시켜주는 명령어도 입력해야함 python manage.py migrate

