from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    # 라우트 profiles/create/ 이 때 연결되는 view.py의 클래스 ProfileCreateView (클래스라서 as_view()), reverse_lazy 할 때 사용할 이름: create)
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]
