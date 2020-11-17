## 1. T/F

```javascript
- let&const와 var의 유일한 차이점은 변수의 유효범위다. False

- '값이 없음'을 표현하는 값으로 null과 undefined 두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다. False null의 경우, object가 반환.

- for in 문을 통해 배열의 각 요소를 순회할 수 있다. False

- '==' 연산자는 두 변수의 값과 타입이 같은지 비교한다. False 타입은 자동 변환

- JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결과값으로 반환할 수는 없다. False 결과값으로 변환 가능함.
```

### 2. Array Helper Method의 동작을 간략히 서술.

```javascript
map 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환
filter 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
find 주어진 판별 함수를 만족하는 첫 번째 요소의 값을 반환. 그런 요소가 없다면 undefined를 반환
every 배열 안의 모든 요소가 주어진 판별 함수를 통과하는지 테스트
some 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트
reduce 배열의 각 요소에 대해 주어진 리듀서(reducer) 함수를 실행하고, 하나의 결과값을 반환
```





### 3. 3제곱을 한 새로운 배열 만드는 코드

```javascript
const nums = [1, 2, 3, 4]
const numbers = nums.map(num => Math.pow(num, 3))
const numbers = nums.map(function (num) {
    return num ** 3
})
```

