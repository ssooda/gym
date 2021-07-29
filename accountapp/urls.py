from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"  # accountapp이라는 app_name 을 명시함으로써 app_name:path_name 방식을 활용할 수 있음

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world")  # path(연결할 주소(route), 보여줄 파일 (view 파일))
]