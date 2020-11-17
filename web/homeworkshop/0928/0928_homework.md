## 1. MTV

```python
Model => 데이터베이스 관리
Template => 사용자가 보는 화면
View => 중간 관리자, 징검다리 역할
```

## 2. 404

```python
메인페이지로 들어왔을 때,
articles에 있는 index.html 렌더링 시키기.

from articles import views

path('', views.index)
```

## 3. Templates & Static

```python
(a) settings.py
(b) STATICFILES_DIRS
(c) TEMPLATES = [
    'DIRS' = [이 부분]
    ]
STATIC_URL => 브라우저에서 동작할 임의의 URL 주소(사용자한테 보여질 주소)
```

## 4. migration

```python
1) python manage.py makemigrations
2) python manage.py showmigrations
3) python manage.py sqlmigrate app이름 migration번호
4) python manage.py migrate
```

## 5. ModelForm True or False

```python
1) F
2) T
3) F
4) T
```

