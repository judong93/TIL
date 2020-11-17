from django.shortcuts import render
from .models import Todo
from django.contrib.auth.decorators import login_required
from .forms import TodoForm

# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        pass
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/form.html', context)