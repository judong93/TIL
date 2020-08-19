## 1. Model 반영하기

```html
emigrate
makeemigrations
emigrate
sqlemigrate
showemigrations
```

## 2. Model 변경사항 저장하기

```html
0001_initial.py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

SQL문
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" 
datetime NOT NULL);
```

## 3. shell

```html
pip install django-extensions
installed app 위에 django-extensions 추가 후
python manage.py shell_plus
```

## 4. Django Model Field

```html
AutoField
BigAutoField
Charfield
DateField
DateTimeFiled
```

