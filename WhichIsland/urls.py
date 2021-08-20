# ROOT폴더의 urls.py에서 라우팅 : 라우팅 하는 파일
"""WhichIsland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from accountapp.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),  # accountapp 폴더의 urls 라는 파일에서 다시 분기해나감
    path('profiles/', include('profileapp.urls')),   # profileapp 폴더의 urls 라는 파일에서 다시 분기해나감
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    re_path(r'^accounts/', include('accountapp.urls')),
    re_path(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 프로필 사진 화면에 띄우기
