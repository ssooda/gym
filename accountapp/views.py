from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):  # view 에서 만든 함수를 urls 에서 routing
    return HttpResponse("hello world")
