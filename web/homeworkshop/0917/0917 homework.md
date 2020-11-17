## 1) User Model BooleanField

django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의한다.



1) BolleanField로 정의 된 칼럼을 작성하시오

```python
is_staff
is_active
is_superuser
```

## 2) username max length

django에서 기본적으로 사용하는 User 모델의 사용할 수 있는 칼럼 중 username에 저장할 수 있는 최대 길이를 작성하시오

```python
max_length = 150
```

## 3) login validation

로그인 했는지 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.

```python
is_authenticated
```

## 4) Login

```python
(a)AuthenticationForm
(b)login
(c)form.get_user()
```

## 5) Who are you?

로그인을 하지 않았을 경우 templates에서 user 변수를 출력했을 때 나오는 클래스의 이름

```python
AnonymousUser
```

## 6) 암호화 알고리즘

Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘. 그리고 함께 사용된 해시 함수를 작성하시오.

```python
PBKDF2 알고리즘, SHA256 해시함수
```

## 7) Logout

로그아웃 기능을 구현하기 위하여 다음과 같이 코들르 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오.

```python
재귀 호출이 되어버림.
그래서 import 할때 as~~~ 이런식으로 이름 바꿔줘야함.
```

