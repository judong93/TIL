# 0914_WORKSHOP



## 1. Compiled Bootstrap

> CSS, JS 파일을 다운로드 받아 Django 프로젝트에 Static 파일로 추가하시오.

```
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
  {% block css %}{% endblock %}
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <scrpit src="{% static 'js/bootstrap.js' %}"></script>
</body>
</html>
```

