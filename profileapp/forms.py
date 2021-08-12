from django.forms import ModelForm

from profileapp.models import Profile

# ModelForm : 기존에 있었던 Model(db) 을 Form 형식으로 변환해주는 기능


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message', 'island']  # model 에 있는 user 라는 필드는 서버에서 따로 처리


