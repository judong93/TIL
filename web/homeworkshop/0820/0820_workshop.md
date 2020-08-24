## 1. 결과사진

![캡처](C:\Users\Joodong\Desktop\캡처.PNG)

![캡처1](C:\Users\Joodong\Desktop\캡처1.PNG)

![캡처2](C:\Users\Joodong\Desktop\캡처2.PNG)

# 2. 코드 정리

## 1) base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
    CRUD - 
    {% block title %}
    {% endblock %}
    </title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
<body>
    <div class="container">
    {% block content %}
    {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>
```

## 2) articles/urls.py

```html
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

## 3) views.py

```html
from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pk') #DB단
    # articles = Article.objects.all()[::-1] #Python단
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1-2. DB에 새로운 게시글 저장하기
    article = Article(title=title, content=content)
    article.save()


    return redirect('articles:detail', article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

## 4) templates/artices/~~.html

### 4.1) detail.html

```html
detail

{% extends 'base.html' %}

{% block title %}
    {{ article.title }}
{% endblock %}

{% block content %}
    <h2 class="text-center">DETAIL</h2>
    <h3>{{ article.pk }}번째 글</h3>
    <hr>
    <p>글 제목: {{ article.title}}</p>
    <p>글 내용: {{ article.content}}</p>
    <p>작성 시각: {{ article.created_at|date:"SHORT_DATETIME_FORMAT"}}</p>
    <p>수정 시각: {{ article.updated_at}}</p>
    <hr>
    <a href="{% url 'articles:edit' article.pk %}" class="btn btn-primary">EDIT</a>

    <form action=" {% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="[DELETE]" class="btn btn-danger">
    </form>
    <a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock %}
```

### 4.2) edit.html

```html
{% extends 'base.html' %}

{% block content%}
    <h2 class="text-center">EDIT</h2>
    <hr>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        <label for="title">Title: </label> 
        <input type="text" name="title" id="title" value="{{ article.title }}"><br>
        <label for="content">Content : </label>
        <textarea name="content" id="content" cols="30" rows="5">{{ article.content }}</textarea><br>
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:detail' article.pk %}">[BACK]</a>
{% endblock %}
```

### 4.3) index.html

```html
{% extends 'base.html' %}

{% block title %}
Articles
{% endblock %}

{% block content %}
    <h2 class="text-center">Articles</h2>
    <a href="{% url 'articles:new' %}">[NEW]</a>
    <hr>
    {% for article in articles %}
    <p>글 번호: {{ article.pk }}</p>
    <p>글 제목: {{ article.title }}</p>
    <a href="{% url 'articles:detail' article.pk %}">
        [DETAIL]
    </a>
    <hr>
    <p>글 내용: {{ article.content }}</p>
    {% endfor %}
{% endblock %}
```

### 4.4) new.html

```html
{% extends 'base.html' %}

{% block content%}
<h2 class="text-center">NEW</h2>
<hr>
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label> 
    <input type="text" name="title" id="title"><br>
    <label for="content">Content : </label>
    <textarea name="content" id="content" cols="30" rows="5"></textarea><br>
    <input type="submit">
</form>
<hr>
<a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock %}
```

