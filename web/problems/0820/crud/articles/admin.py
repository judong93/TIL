from django.contrib import admin
from .models import Article # 명시적 상대 경로 표현법 (같은 위치라는 뜻으로 '.'을 사용)

# Register your models here.
admin.site.register(Article)