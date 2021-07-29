from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):  # view 에서 만든 함수를 urls 에서 routing
    # return HttpResponse("hello world")
    # HttpResponse 는 직접 view 단을 만드는 것임
    return render(request, 'accountapp/hello_world.html')
    # render : 파이썬 폴더에서 직접 view 단을 만드는 것이 아니라 요청이 있을 때 보여줄 html 파일을 연결하는 것
    # render 로 html 파일을 연결해주려면 ROOT 폴더의 settings.py 에서 TEMPLATES 'DIRS': [os.path.join(BASE_DIR, 'templates')] 을 명시해줘야함

