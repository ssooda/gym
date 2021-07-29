from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    # UserCreationForm 을 상속받는 AccountUpdateForm 클래스 생성
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True  # UserCreationForm 에 있는 username 필드를 비활성화


