from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):  # view 에서 만든 함수를 urls 에서 routing
    # return HttpResponse("hello world")
    # HttpResponse 는 직접 view 단을 만드는 것임

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')  # html 에서 name 이 hello_world_input

        new_hello_world = HelloWorld  # 데이터베이스를 연결한 HelloWorld 라는 클래스의 새로운 객체(new_hello_world)를 만듦
        new_hello_world.text = temp
        new_hello_world.save()  # db에 데이터를 저장

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    # render : 파이썬 폴더에서 직접 view 단을 만드는 것이 아니라 요청이 있을 때 보여줄 html 파일을 연결하는 것
    # render 로 html 파일을 연결해주려면 ROOT 폴더의 settings.py 에서 TEMPLATES 'DIRS': [os.path.join(BASE_DIR, 'templates')] 을 명시해줘야함
    # context : 데이터 꾸러미 {'text': 'POST method'} text 라는 이름을 가지고 있고 내용은 POST method! => html에서 {{ text }}로 사용할 수 있음

    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET method!!'})

