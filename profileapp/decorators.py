from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])  # model(database) 인 Profile (model.py 에서 Profile 클래스)

        if not profile.user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated
