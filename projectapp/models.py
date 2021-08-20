from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # 파이썬 내부 함수
        return f'{self.pk} : {self.title}'

