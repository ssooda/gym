from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"  # accountapp이라는 app_name 을 명시함으로써 app_name:path_name 방식을 활용할 수 있음

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),  # path(연결할 주소(route), 보여줄 함수 (view 파일에 있는 함수))

    path('create/', AccountCreateView.as_view(), name="create"),  # 함수형에서는 함수명만 명시하면 되지만 클래스형에서는 클래스명.as_view()해야함
]