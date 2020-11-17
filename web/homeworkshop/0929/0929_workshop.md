## ERD

### ERD

![ERD 캡처](C:\Users\Joodong\Desktop\박주동\TIL\web\homeworkshop\0929\ERD 캡처.PNG)



### models.py

```python
class Product(models.Model):
    name = models.CharField(max_length=30)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    brands = models.ManyToManyField(Brand, related_name='our_products')
    css = models.ManyToManyField(CS, related_name='supplied_products')

class Brand(models.Model):
    name = models.CharField(max_length=30)

class Delivery(models.Model):
    name = models.CharField(max_length=30)

class CS(models.Model):
    name = models.CharField(max_length=30)
```

