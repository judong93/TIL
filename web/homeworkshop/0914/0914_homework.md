## Django Model Form

### 1) 모델 폼 정의

```PYTHON
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
	class Meta:
        model = Reservation
        filed = '__all__'
```



### 2) 문제 발생 원인과 해결방법 찾기


```PYTHON
def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
       
    else:
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)

```



### 3) 글 수정 기능

```PYTHON
def update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    context = {
        'reservation': reservation,
        'form': form
    }
    return render(request, 'reservations/update.html', context)
```



### 4) 글수정 기능

```PYTHON
<h2>edit</h2>
<form action="{% url 'reservations:update' reservation.pk %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit" value="submit">
</form>
as_table
as_ul
```







