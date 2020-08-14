import random
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    name = '주동'
    context = {
        'name': name,
    }
    return render(request, 'index.html', context)


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'pick': pick,})


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    empty_list = []
    today = datetime.datetime.now()
    context = {
        'menus' : menus,
        'empty_list': empty_list,
        'today' : today
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw에서 보낸 form데이터(request.GET)를 받아야함.
    message = request.GET.get('name')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)