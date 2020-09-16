## 1. /accounts/


```python
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    members = User.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'accounts/index.html', context)
```

## 2. /accounts/signup/

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

