# Generated by Django 3.2.5 on 2021-07-29 04:42
# migrations 폴더, 그 안의 파일은 임의로 지우면 안 됨 !!! 함부로 지우지 말 것

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
