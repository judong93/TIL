# 0915_HOMEWORK



## 1. Static 파일 기본 설정

> 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부의 assets’ 에 있다 . 이 폴더 안에 Static 파일이 있다 라고 Django 프로젝트에게 알려 주기 위하여 settings.py 에 작성해야 하는 설정을 작성하시오.

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / '프로젝트이름' / 'assets',
]

```



## 2. media 파일 기본 설정

> 업로드 파일 저장 위치를 Django 프로젝트 폴더 내부의 uploaded_files’ 로 지정하고자 한다 . 이 때 , settings.py 에 작성해야 하는 설정 2 가지를 작성하시오

```python
MEDIA_URL = '/media/' 

MEDIA_ROOT = BASE_DIR / '프로젝트 이름' / 'uploaded_files'
```



## 3. Serving Files

> 프로젝트 내부로 사용자가 업로드한 파일이 들어올 수 있게 되었다. 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 볼 수 있도록 하기 위해선 업로드 된 파일에 대한 URL을 생성 해주는 설정이 필요하다.
> 빈칸 __(a)__, __(b)__, __(c)__, __(d)__에 들어 갈 코드를 작성하시오.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



