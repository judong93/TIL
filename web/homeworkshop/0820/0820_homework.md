##  Django Model

### 1) 마이그레이션 작업을 위한 두 개의 명령어

```html
python manage.py makemigrations
python manage.py migrate
```



### 2)

```html
#3
```



### 3)

```html
Negative indexing (i.e. Entry.objects.all()[-1]) is not supported
#2
```



### 4)

```html
>>> article = Article.objects.get(pk=1)
>>> article.title
'안녕하세요'

# 값을 변경하고 저장
>>> article.title = '안녕하세요'
>>> article.content = '반갑습니다'
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'안녕하세요'
```



### 5)

```html'
(a)objects
(b)all
```

