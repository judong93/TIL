## 1. User 모델이 정의된 코드

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        
 
```

## 2. User ModelForm

```python
from django.contrib.auth.forms import UserCreationForm
```



## 3. decorators

```python
from django.views.decorators.http import require_POST
```

