## 1. T/F

```python
URI는 정보의 자원 표현, 자원에 대한 행위는 HTTP Method로 표현한다. True
HTTP Method는 GET과 POST 두 종류만 있다. False
일반적으로 URI 마지막에 슬래시(/)는 포함하지 않는다. True
https://www.fifa.com/worldcup/teams/team/43822/create/는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다. False
```

## 2. HTTP status code의 의미를 간략하게 작성하시오.

```python
200 요청이 성공적으로 되었습니다
400 이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.
401 비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다.
403 클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않습니다. 예를들어 그들은 미승인이어서 서버는 거절을 위한 적절한 응답을 보냅니다. 401과 다른 점은 서버가 클라이언트가 누구인지 알고 있습니다.
404 서버는 요청받은 리소스를 찾을 수 없습니다. 브라우저에서는 알려지지 않은 URL을 의미합니다. 이것은 API에서 종점은 적절하지만 리소스 자체는 존재하지 않음을 의미할 수도 있습니다. 서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위하여 이 응답을 403 대신에 전송할 수도 있습니다. 이 응답 코드는 웹에서 반복적으로 발생하기 때문에 가장 유명할지도 모릅니다.
500 서버가 처리 방법을 모르는 상황이 발생했습니다. 서버는 아직 처리 방법을 알 수 없습니다.
```

## 3. StudentSerializer 작성하기

```python
class Student(models.Model):
    name = models.Textfield()
    age = models.CharField(max_length=5)
    adress = models.TextField()

from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

## 4. Serializers 간략하게 설명하시오

```python
쿼리셋이나 모델 인스턴스 같은 복잡한 데이터를 쉽게 JSON이나 XML 혹은 다른 컨텐트 타입으로 렌더될 수 있는 네이티브 파이썬 데이터 타입으로 변환해주는 것을 의미한다.
```

