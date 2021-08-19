from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')
    # on_delete+models.CASECADE : User가 지워지면 같이 지워지도록

    class Meta:
        unique_together = ("user", "project")
        # 유저와 프로젝트 한 쌍이 가지는 구독은 오직 하나만 존재하도록(한 명의 유저가 한 프로젝트를 여러번 구독하지 못하게)

