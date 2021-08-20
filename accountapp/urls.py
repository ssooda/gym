
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    home

app_name = "accountapp"  # accountapp이라는 app_name 을 명시함으로써 app_name:path_name 방식을 활용할 수 있음

urlpatterns = [
    # path('hello_world/', hello_world, name="hello_world"),  # path(연결할 주소(route), 보여줄 함수 (view 파일에 있는 함수))

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name="login"),  # login, logout 은 필요한 변수가 많이 없어서 urls.py 에서 바로 class import 하고, template 를 지정
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name="create"),  # 함수형에서는 함수명만 명시하면 되지만 클래스형에서는 클래스명.as_view()해야함

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # datail/pk 라는 정수형 데이터를 받겠다

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    path('home/', home, name='home'),
]