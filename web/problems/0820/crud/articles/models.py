from django.db import models

# Create your models here.
class Article(models.Model): #상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): #데이터베이스 설계도에 영향을 주지 않으므로, 메이크 마이그레이션해도 안먹힘.
        return self.title