## 9월 22일 Practice

1. user 테이블 전체 데이터 조회

   ```python
   User.objects.all()
   ```

2. id 19인 사람의 age 조회

   ```python
   User.objects.get(id=19).age
   ```

3. 모든 사람의 age 조회

   ```python
   User.objects.values('age')
   ```

4. age가 40 이하인 사람들의 id와 balance 조회

   ```python
   users = User.objects.filter(age__lte=40).values('id', 'balance')
   
   for user in users:
       print(user.get('id'))
       print(user.get('balance'))
   ```

5. last_name이 '김'이고 balance가 500 이상인 사람들의 first_name 조회

   ```python
   User.objects.filter(last_name='김', balance__gte=500).values('first_name')
   ```

6. first_name이 수로 끝나고 행정구역이 경기도인 사람들의 balance 조회

   ```python
   User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
   ```

7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수

   ```python
   from django.db.models import Q
   
   User.objects.filter(Q(balnace__gte=2000) | Q(age__lte=40)).count()
   ```

8. phone 앞자리가 010 으로 시작하는 사람의 총 인원수

   ```python
   User.objects.filter(phone__startswith='010').count()
   ```

9. 이름이 김옥자인 사람의 행정구역을 경기도로 수정

   ```python
   User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
   ```

10. 이름이 백진호인 사람 삭제

    ```python
    User.objects.filter(first_name='진호', last_name='백').delete()
    ```

11. balance 기준으로 상위 4명의 first_name, last_name, balance 조회

    ```python
    users = User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')
    
    for user in users:
        print(user.get('first_name'))
        ...
    ```

12. phone에 123을 포함하고 age가 30 미만인 정보를 조회

    ```python
    User.objects.filter(phone__contains='123', age__lt=30)
    ```

13. phone이 010으로 시작하는 사람들의 행정구역을 중복 없이 조회

    ```python
    User.objects.filter(phone__startswith='010').values('country').distinct()
    ```

14. 모든 인원의 평균 age

    ```python
    from django.db.models import Avg
    
    User.objects.aggregate(Avg('age'))
    ```

15. 박씨들의 평균 balance

    ```python
    User.objects.filter(last_name='박').aggregate(Avg('balance'))
    ```

16. 경상북도 사람 중 가장 많은 balance

    ```python
    from django.db.models import Max
    
    User.objects.filter(country='경상북도').aggregate(Max('balance'))
    ```

17. 제주도의 가장 많은 balance 사람의 first_name

    ```python
    User.obejcts.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]
    ```

    







