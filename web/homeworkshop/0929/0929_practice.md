## 결과사진

![Profile html캡처](C:\Users\Joodong\Desktop\박주동\TIL\web\homeworkshop\0929\Profile html캡처.PNG)

## accounts/views.py

```python
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)
```



## accounts/models.py

```python
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```



## profile.html

```python
{% extends 'base.html' %}

{% block content %}
<h1 class="text-center">{{ person.username }}의 프로필</h1>
<hr>
{% include 'accounts/_follow.html' %}

<hr>

<h2>{{ person.username }}이 작성한 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}이 작성한 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}이 좋아요 한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<a href="{% url 'articles:index' %}">[back]</a>

{% endblock %}
```

