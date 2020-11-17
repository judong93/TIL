## 1. T/F

```javascript
- Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하는 역할을 한다. True
- XMLHttpRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다. True
- axios는 XHR을 보내고 응답결과를 Promise 객체로 반환해주는 라이브러리다. True
```



## 2. 동작 서술.

```javascript
Hello SSAFY가 먼저 실행된 후
setTimeout API가 실행되면서 Call Stack에서 Web API 파트(?)로 넘어간다. 이때 Bye SSAFY 부분은 순차적으로 출력이 되고, setTimeout 부분은 Task Queue에서 대기하다가 Event Loop에 의해 빈 Call Stack으로 보내진 후 처리된다.
```



## 3. 2번을 순서대로 실행되도록 다시 작성

```javascript
console.log('Hello SSAFY!') 
    
const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
    console.log('I am from setTimeout')
    resolve('Bye SSAFY!')
  }, 1000)})

promise.then(bye_message => {
    console.log(bye_message);
})    
```

