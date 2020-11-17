## 1. T/F

```python
- JS는 single threaded 언어로 한번에 한가지 일 밖에 처리하지 못한다. True

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다. False Event Loop에 들린 후 할당

- Promise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는 비동기 처리가 성공/실패 했을 경우 어떠한 값을 전달할지 결정한다. True

- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이며, .catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다. True
```

## 2. JS에서 동기와 비동기 함수의 차이점

```javas
동기 = 각각의 요청에 따라 그 결과가 나온 후 다음 요청이 들어감. 즉 순차적으로 진행되는 특징
비동기 = 요청과 결과로 이루어지는 실행흐름의 단위가 맞지 않음.
즉, 한 요청에 대한 결과가 나오지 않았음에도 다음 요청이 들어올 수 있음.(결과여부에 관계없이 순서대로 요청을 보냄)
```

## 3. 들어갈 코드 작성

```javascr
(a)get
(b)then
(C)response
```

