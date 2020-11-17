# ECMAScript

[toc]

## 1. 변수와 식별자

### 1.1 식별자

> 변수명은 식별자(identifier)라고 불리며, 특정 규칙을 따른다.
>
> * 반드시 문자, 달러(`$`), 밑줄(`_`)로 시작해야 한다. 이후는 숫자도 가능하다.
> * 대소문자를 구분한다. 클래스명 외에는 대문자로 시작하지 않는 것이 좋다.
> * 예약어는 사용 불가능하다. (const, return, break, class, super, awiat, ...)

#### 식별자 작성 스타일

* 카멜 케이스(camelCase, lower-camel-case) : 객체, 변수, 함수

  ```javascript
  // 숫자, 문자, boolean
  let dog
  let variableName
  
  // 배열 : 복수형 이름 사용
  let cats = []
  
  // 정규표현식 : 'r'로 시작
  const rDesc = /.*/
  
  // 함수
  function getPropertyName () {}
  
  // 이벤트 핸들러 : 'on'으로 시작
  function onClick () {}
  function onKeyDown () {}
  
  // boolean 반환 함수 : 'is'로 시작
  let isAvailable = true
  
  ```

* 파스칼 케이스(PascalCase, upper-camel-case) - 클래스, 생성자

  ```javascript
  class User {
    constructor(options) {
      this.name = options.name
    }
  }
  
  const good = new User({
    name: '홍길동',
  })
  ```

* 대문자 스네이크 케이스(SNAKE_CASE) - 상수

  * 변수와 변수의 속성이 변하지 않는다는 것을 알려준다.

  ```javascript
  const API_KEY = 'SOMEKEY'
  const PI = Math.PI
  ```

### 1.2 변수

| 구분           | 재할당 | 재선언 | 스코프      |
| -------------- | ------ | ------ | ----------- |
| `var` (변수)   | O      | O      | 함수 스코프 |
| `let` (변수)   | O      | X      | 블록 스코프 |
| `const` (상수) | X      | X      | 블록 스코프 |



#### let (변수)

> **값을 재할당 할 수 있는 변수**를 선언하는 키워드

```javascript
// 재할당 O
let name = '채원'
name = '승아'
console.log(name) // 승아
```

```javascript
// 재선언 X
let name = '채원'
let name = '승엽' <- 안됨. Uncaught SyntaxError: redeclaration of 							let name
```

**블록 유효 범위(Block Scope)**

if, for문, 함수 등의 중괄호({}) 내부를 가리킨다.

```javascript
let x = 1
if (x === 1) {
    console.log('Yeah!')
} // Yeah!

if (x === 1 ) {
    let x = 2
    console.log(x) // 2
} 
console.log(x) // 1
```



#### const (상수)

> **값이 변하지 않는 상수(constant)**를 선언하는 키워드

```javascript
// 선언 시 반드시 초기값을 설정해야 한다.
const myFav = 7

const myFav <- Error뜸.
```

```javascript
// 재할당과 재선언이 불가능하다.
const myFav = 7
const myFav = 8 // Error(재선언)
myFav = 8 // Error(재할당)
```

```javascript
// let과 동일하게 블록 유효 범위를 가진다.
const myFav = 7
if (myFav === 7) {
    const myFav = 20
    console.log(myFav)
} // 20
console.log(myFav) // 7
```



#### var (변수)

> ES6 이전에 변수를 선언하는 키워드

* 예기치 않은 문제를 많이 발생시킨다. 절.대. 사용하지말자!

```javascript
// var 키워드로 재선언 할 수 있다.

```



**함수 유효 범위(Function Scope)**

* 변수의 범위는 현재 실행 문맥이며, 그 문맥은 둘러싼 함수 혹은 전역일 수 있다.

```javascript
var a = 1
let b = 2
if (a === 1) {
    var a = 11
    let b = 22
    
    console.log(a) // 11
    console.log(b) // 2
}
console.log(a) // 11
console.log(b) // 2
```





### 1.3 Hoisting

`var`로 선언된 변수는 선언 이전에 참조할 수 있다. 이 현상을 `hoisting(호이스팅)`이라고 한다.

```javascript
console.log(name)  // undefined (선언 이전에 참조)
var name = '홍길동'  // 선언
```



코드 실행 시 암묵적으로 다음과 같이 이해한다.

```javascript
var name  // undefined로 초기화
console.log(name)
var name = '홍길동'
```

코드 실행 시 **선언**만 코드 최상단으로 끌어 올려 진다. (hoisted)

`var`로 선언된 변수는 선언 시 초기화 작업이 동시에 일어난다.

* 초기화(Initialization) : 변수가 메모리에 할당되어 `undefined`로 값이 설정되는 과정

```javascript
console.log(name)  // Uncaught ReferenceError: Cannot access 'name' before initialization
let name = '홍길동'
```



## 2. 타입과 연산자

### 2.1 Primitive(원시값, 원시 자료형) 타입

#### Number (숫자)

```javascript
const a = 13 
const b = -5 
const c = 3.14      
const d = 2.998e8   // 2.998 * 10^8 = 299, 800, 000
const e = Infinity 
const f = -Infinity
const g = NaN       // Not a Number

console.log(a, b, c, d, e, f, g)
```

* `Infinity`와 `NaN`

  * 둘다 전역 객체(window)의 속성

  * `Infinity` : 양의 무한대와 음의 무한대로 나뉨

  * `NaN` : 표현할 수 없는 값, 자기 자신과 일치하지 않는 유일한 값을 표현
- 0/0, "문자" * 10, Math.sqrt(-9)



#### String (문자열)

```javascript
const sentence1 = 'Hello SSAFY' // single quote
const sentence2 = "Hello SSAFY" // double quote
```

```javascript
// 곱셈, 나눗셈, 뺄셈 X
// 덧셈 O

const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName

console.log(fullName)
```

```javascript
// Quote 사용 시 줄바꿈이 안된다.
// 대신 escape sequence를 사용할 수 있기 때문에 '\n'를 사용해야 한다.

const word = "안녕
하세요"
// Uncaught SyntaxError: Invalid or unexpected token

const word1 = "안녕 \n하세요"
console.log(word1)
```



**템플릿 리터럴(Template Literal)**

* ES6부터 지원한다.

* 줄바꿈이 되며, 문자열 사이에 변수 삽입도 가능하다.
* 단, escape sequence를 사용할 수 없다.

```javascript
let age = 10
let greeting = '안녕!
난 ${age}살이야.'
```



#### Boolean

참과 거짓을 표현하는 값

```javascript
true
false
```



#### Empty Value

값이 존재하지 않음을 표현하는 값. 큰 차이를 두지 않고 활용하면 된다.

* `null` : 값이 없음을 개발자가 표현하기 위해 인위적으로 사용하는 값

  ```javascript
  let name = null
  console.log(name) // null
  ```

* `undefined` : 값이 없는 경우 JS가 자동으로 할당해주는 값

  ```javascript
  var name
  console.log(namne) // undefined
  ```



* `null`과 `undefined`의 가장 대표적인 차이점은 `typeof` 연산자를 통해 타입을 확인 했을 때 나타난다. `null`의 타입이 `object`인 이유도 JS의 실수 때문인데 쉽게 타입을 바꾸지 못하는 이유는 `null` 타입에 의존성을 띄고 있는 많은 프로그램들이 망가질 수 있기 때문이다.

  ```javascript
  typeof null          // "object"
  typeof undefined     // "undefined"
  ```



### 2.2 연산자

#### 할당 연산자

> 연산과 동시에 변수에 할당하는 연산자

```javascript
let c = 0

c += 10 
console.log(c) // 10 - c에 10을 더한다

c -= 3 
console.log(c) // 7 - c에 3을 뺀다

c *= 10 
console.log(c) // 70 - c에 10을 곱한다

c++
console.log(c) // 71 - c에 1을 더한다(증감식)

c--
console.log(c) // 70 - c에 1을 뺀다.(증감식)
```



#### 비교 연산자

> 두 값을 비교하기 위한 연산자

```javascript
3 > 2    // true
3 < 2    // false
```

```javascript
// 문자열 비교
// 영어 소문자가 대문자보다 큰 값을 가진다.
// 알파벳은 오름차순으로 순서를 비교한다.

'A' < 'B'    // true
'Z' < 'a'    // true
'가' < '나'   // true
```



#### 동등 연산자 (`==`)

* 메모리의 같은 객체를 가리키거나, 같은 값을 갖도록 변환할 수 있다면 서로 갖다고 판단한다.
  (JS 엔진이 자동으로 형변환하여 두 값을 비교)
* 이러한 형변환은 예기치 못한 결과를 야기할 수 있기 때문에, **동등 연산자 사용은 지양**한다.

```javascript
const a = 1
const b = '1'
console.log(a == b) // true (자동 형변환)
console.log(a == Number(b)) // true
```



#### 일치 연산자 (`===`)

* 메모리의 같은 객체를 가리키거나, 타입 뿐만 아니라 같은 값인지 비교한다.
* **엄격한 비교를 하기 때문에 일치 연산자를 사용하는 것을 권장**한다.

```javascript
const a = 1
const b = '1'
console.log(a === b) // false
```



#### 논리 연산자

> boolean 타입을 연산할 수 있는 연산자
>
> and, or, not

* `and` -> `&&`

  ```javascript
  true && false  // false
  true && true   // true
  
  1 && 0  // 0
  0 && 1  // 0
  4 && 7  // 7
  ```

* `or` -> `||`

  ```javascript
  false || true    // true
  false || false   // false
  
  1 || 0  // 1
  0 || 1  // 1
  4 || 7  // 4
  ```

* `not` 연산 -> `!`

  ```javascript
  !true  // false
  ```

  

#### 삼항 연산자(Ternary operator)

> 조건식이 참이면 `:` 앞의 값이 반환되고, 거짓이면 `:` 뒤의 값이 반환되는 연산자

* 삼항 연산자는 중첩 되어서는 안되며, 일반적으로 한 줄에 표현한다.

  ```javascript
  true ? 1 : 2 // 1
  false ? 1 : 2 // 2
  ```

* 삼항의 결과를 변수에 할당할 수 있다.

  ```javascript
  const result = Math.PI > 4 ? 'Yeah!' : 'Nope!!!!'
  console.log(result) // 'Nope!!!!'
  ```



## 3. 조건문과 반복문

### 3.1 조건문

> `if`, `else if`, `else`

* if 괄호 안의 조건식이 참인 경우 해당 블럭을 실행한다.

  ```javascript
  const name = 'admin'
  
  if (name === 'admin') {
    console.log('관리자님 환영합니다!')
  }
  ```

* if의 조건식이 거짓인 경우 else 블럭을 실행한다.

  ```javascript
  const name = '황성훈'
  
  if (name === 'admin') {
    console.log('관리자님 환영합니다!')
  } else {
    console.log(`${name}님 환영합니다.`)
  }
  ```

* if 이후 else if로 추가 조건문을 작성할 수 있다.

  ```javascript
  const name = 'manager'
  
  if (name === 'admin') {
  	console.log('관리자님 환영합니다.')
  } else if (name === 'manager') {
  	console.log('매니저님 환영합니다.')
  } else {
  	console.log(`${name}님 환영합니다.`)
  }
  ```

* `switch`

  * 하나의 변수의 값에 따라 분기를 하는 조건문
  * `case` 키워드를 통해 조건을 분기하고, `break` 키워드를 통해 동작을 멈춘다.
  * `case`에 조건이 없을 시 `default` 구문이 실행된다.

  ```javascript
  const name = '홍길동'
  
  switch(name) {
  	case 'admin': {
  		console.log('관리자님 환영합니다.')
  		break
  	}
  	case 'manager': {
  		console.log('매니저님 환영합니다.')
  		break
  	}
  	default: {
  		console.log(`${name}님 환영합니다.`)
  	}
  }
  ```



### 3.2 반복문

#### while

while 키워드 뒤 괄호의 조건식이 true인 동안 반복한다.

```javascript
let i = 0

while (i < 6) {
	console.log(i)
	i++
}
```



#### for

for 키워드 뒤 괄호에서 **사용할 변수 하나를 정의**하고, 그 **변수가 특정 조건에 대해 false 값이 될 때까지 반복**한다.

```javascript
for (let i = 0; i < 6; i++) {
	console.log(i)
}
```



#### for of

배열에서 요소를 하나씩 순회하며 반복한다.

매 요소는 블럭 내에서 변수로 선언되기 때문에 변수 선언 키워드를 작성한다.

```javascript
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
	console.log(number)
}
```



#### for in

객체(object)의 key를 순회하는 반복문. 배열(array)인 경우 index를 순회한다.

```javascript
const fruits = { a: 'apple', b: 'banana' }

for (const key in fruits) {
	console.log(key) // a, b
	console.log(fruits[key]) // apple, banana
}
```

```javascript
const fruits = ['apple', 'banana']

for (const idx in fruits) {
	console.log(idx) // 0, 1
	console.log(fruits[idx]) // apple, banana
}
```



## 4. 함수

### 4.1 함수

#### 함수 선언식(statement, declaration)

```javascript
function add (num1, num2) {
	return num1 + num2
}

add(2, 7) // 9
```



#### 함수 표현식(expression)

````javascript
const sub = function (num1, num2) {
	return num1 - num2
}

sub(7, 2) // 5
````

* 위처럼 이름이 없는 함수를 **익명 함수(anonymous function)**라고 한다.

* 익명 함수는 함수 표현식에서 사용할 수 있으며, 이름을 지정할 수도 있다.

* 함수를 매개변수로 넘기거나 변수에 담아서 사용할 수 있는 이유는, JS에서는 함수를 일급 객체로 취급하기 때문이다.

  ```javascript
  const mySub = function namedSub (num1, num2) {
  	return num1 - num2
  }
  ```



#### 기본 인자(Default Args)

```javascript
const greeting = function (name = '재윤') {
    console.log('${name}님 하이! :)')
}
greeting() // 재윤님 하이! :)
```



### 4.2 선언식 vs 표현식

* **타입**

  * 함수도 하나의 값으로 평가되며, 위에서 선언한 add, sub의 타입을 확인하면 함수임을 확인할 수 있다.

  ```javascript
  typeof add // function
  typeof sub // function
  ```

* **Hoisting**

  * 함수 선언식으로 선언한 함수는 `var`로 정의한 변수처럼 hoisting된다. 함수호출 이후에 선언해도 동작한다.

    ```javascript
  console.log(add(5, 5)) // 10
    
  function add (num1, num2) {
        return num1 + num2
  }
    ```
  
  * 함수 표현식으로 선언한 함수는, 변수에 할당함으로 변수로 평가되어 변수의 scope 규칙을 따른다.

    ```javascript
  console.log(sub(7, 2)) // error
    const sub = function (num1, num2) {
        return num1 - num2
    }
    ```
  
  * 함수 표현식을 `var` 변수에 할당하면 `undefined`로 초기화 되어 다른 문제가 발생한다.
  
    ```javascript
    console.log(sub(7, 2)) // error
    var sub = function (num1, num2) { // var sub 부분만 위로 가져옴 -> undefined. 따라서 함수로 인식못함.
        return num1 - num2
    }
    ```



### 4.3 Arrow Function (화살표 함수)

> function과 중괄호를 줄이기 위해 고안된 단축 문법
>
> 1. `function` 키워드를 생략할 수 있다.
> 2. 함수 매개변수가 하나인 경우 `()`를 생략할 수 있다.
> 3. 함수 바디가 표현식 하나라면 `{}`와 `return`도 생략할 수 있다.



```javascript
// 항상 익명이기 때문에 '함수 표현식'에서만 선언할 수 있다.
const arrow = function (name) {
  return `hello! ${name}`
}

// 1. function 키워드 삭제
const arrow = (name) => {
  return `hello! ${name}`
}
arrow('주동') // "hello! 주동"
// 2. () 생략: 매개변수 하나인 경우
const arrow = name => {
  return `hello! ${name}`
}

// 3. {} & return 생략: 바디 표현식이 하나인 경우
const arrow = name => `hello! ${name}`

// 4. 매개변수 없는 경우
const arrow = () => console.log('안녕!')
```





## 5. Data Structure : Array & Object

> 자바스크립트에서 Array와 Object는 reference 타입으로 객체라고 표현한다.
>
> 객체는 속성들을 담고있는 가방(collection)이다.
>
> 각 속성들은 변수처럼 메모리에 할당되어 있으며, 객체는 할당되어있는 메모리의 주소값을 바라보고 있다.



### 5.1 Array (배열)

```javascript
const numbers = [1, 2, 3, 4]

numbers[0]     // 1
numbers[-1]    // undefined => 정확한 양의 정수 index만 가능
numbers.length // 4
```

#### 자주 쓰이는 배열의 메서드

* `reverse`

  * 원본 배열의 요소 순서를 반대로 정렬한다.

  ```javascript
  numbers.reverse()
  numbers  // [4, 3, 2, 1]
  
  numbers.reverse()
  numbers  // [1, 2, 3, 4]
  ```

* `push & pop`

  * 요소를 배열 가장 뒤에 추가하거나 제거한다.

  ```javascript
  numbers.push('a')  // 5 => 새로운 배열의 길이
  numbers  // [1, 2, 3, 4, 'a']
  
  numbers.pop()  // 'a' => 가장 마지막 요소
  numbers  // [1, 2, 3, 4]
  ```

* `unshift & shift`

  * 요소를 배열 가장 앞에 추가하거나 제거한다.

  ```javascript
  numbers.unshift('a')  // 5, 새로운 배열의 길이
  numbers  // ['a',1,2,3,4]
   
  numbers.shift()  // 'a', 가장 처음 요소
  numbers  // [1,2,3,4]
  ```

* `includes`

  * 배열에 특정 요소가 있는지 여부를 boolean 값으로 반환한다.

  ```javascript
  numbers.includes(1)  // true
  numbers.includes(0)  // false
  ```

* `indexOf`

  * 배열에 특정 요소가 있는지 여부를 확인한 후, 가장 처음 찾은 요소의 index 값을 반환한다.
  * 요소가 없으면 `-1`을 반환한다.

  ```javascript
  numbers.push('a', 'a')
  numbers  // [1,2,3,4,'a','a']
  numbers.indexOf('a')  // 4
  numbers.indexOf('b')  // -1
  ```

* `join`

  * 배열의 요소를 함수의 인자를 기준으로 이어서 문자열로 반환한다.
  * 인자가 없으면 `,` 문자를 기준으로 이어서 문자열을 반환한다.
  * 원본은 바뀌지 않는다.

  ```javascript
  numbers.join()    // '1,2,3,4,a,a'
  numbers.join('')  // '1234aa'
  numbers.join('-') // '1-2-3-4-a-a'
  ```

  

### 5.2 Object (객체/오브젝트)

Key와 Value 쌍으로 이루어진 프로퍼티들의 집합

- Key와 Value는 콜론으로 구분한다.
- 프로퍼티와 프로퍼티는 쉼표로 구분한다.

Object의 key는 문자열 타입, value는 모든 타입이 될 수 있다.

```javascript
const me = {
  name: '김효진',
  'phone number': '010-0000-0000',
  sayHello: function () {
    console.log('난 효진이야!')
  },
  appleProducts: {
    ipad: '2020Pro',
    iphone: 'XS',
    macbook: '2019Pro',
  },
}
```



키 값이 여러 문자일 경우 대괄호로 접근해야 한다.

```javascript
const me = {
 name: '효진',
 'phone number': '010-1234-1234',
 sayHello: function () {
     console.log('안녕!')
 },
 samsungProducts: {
     phone: 'Galaxy Note 20 Ultra', 
     tablet: 'Galaxy TAB S7 Plus',
     notebook: 'Galaxy Book Flex 15inch'
 }   
}

me.name or me['name']
me.'phone number' <= 이거는 안됨.
me['phone number'] 이걸 써야함.
me.samsungProducts.phone
me.sayHello()
```



#### Object 축약 문법 (ES6+)

객체를 정의할 때, key와 할당하는 변수의 이름이 같으면 축약할 수 있다.

```javascript
const students = ['강채원', '구영지', '박주동', '이재윤', '한승엽', '김수진']

const skills = {
  languages: ['Python', 'JavaScript'],
  frameworks: ['Django', 'Vue.js'],
}

const teacher = '유창오'

const seoul2 = {
    students: students,
    skills: skills,
    teacher: teacher
}
seoul2.students
위와 아래는 결과값이 같다.
const seoul2 = {
    students,
    skills,
    teacher
}
seoul02.students
```



메서드(Object 내에 정의된 함수)를 선언할 때, function 키워드를 생략한 축약 표현이 가능하다.

```javascript
const me = {
  name: '김효진',
  'phone number': '010-0000-0000',
  sayHello () {
      console.log('안녕!')
  }
}
```



**Object Destructuring (비구조화, 파괴)** 

```javascript
const userInformation = {
  name: '윤도훈', 
  userId: 'ssafyStudent1234',
  phoneNumber: '010-1234-1234',
  email: '도훈찡@ssafy.com'
}
```



* **ES5까지 사용했던 방식**

  ```javascript
  const name = userInformation.name
  const userId = userInformation.userId
  const phoneNumber = userInformation.phoneNumber
  const email = userInformation.email
  ```

* **ES6+**

  ```javascript
  const {name} = userInformation
  const {userId} = userInformation
const {phoneNumber, email} = userInformation
  
  console.log(name, userId, phoneNumber, email)
  ```

  ```javascript
  // ES5까지
  function getUserInfo (name, userId) {
      console.log(name, userId)
  }
  getUserInfo(userInformation.name,
  userInformation.userId)
  
  // ES6+
  function getUserInfo ({ name, userId }) {
      console.log(name, userId)
  }
  getUserInfo(userInformation)
  ```
  
  

### 5.3 JSON (JavaScript Object Notation - JS 객체 표기법)

> key-value 형태로 JS Object와 유사한 모습으로 데이터를 표현하는 표기법
>
> 모습만 비슷할 뿐이고, 실제로는 문자열 타입이다.
>
> Object처럼 사용하기 위해선 Parsing(구문 분석) 작업이 필요하다.
>
> JSON 형식의 파일을 다루기 위해 JS에서는 JSON 내장 객체를 제공한다.



#### Object -> JSON(string)

```javascript
const jsonData = JSON.stringify({
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
})

console.log(jsonData)
console.log(typeof jsonData) // string
```



#### JSON(string) -> Object

```javascript
const parsedData = JSON.parse(jsonData)

console.log(parsedData)
console.log(typeof parsedData) // object
```



### 5.4. Array Helper Methods

> Helper?
>
> 자주 사용하는 로직을 재활용할 수 있게 만든 일종의 라이브러리
> ES5.1 버전에 처음 등장했으며, ES6부터 본격적으로 사용되기 시작했다.



#### forEach

* 주어진 `callback`을 배열에 있는 각 요소에 대해 오름차순으로 한번씩 실행한다.
* return 값이 없다 (`undefined`)

```javascript
arr.forEach(callback(element, index, array))
```

* 예시

  ```javascript
  const colors = ['red', 'blue', 'green']
  colors.forEach(function (color) {
      console.log(color)
  })
  
  // refactoring (arrow function)
  colors.forEach (color => console.log(color))
  ```

* 연습

  * images 배열안에 있는 정보(height, width)를 곱해 넓이를 구하여 areas 배열에 저장하세요.

  ```javascript
  const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 }
  ]
  
  const areas = []
  
  images.forEach(function (image) {
      areas.push(image.height * image.width)
})
  areas
  ```
  
  

#### map

* 배열 내의 모든 요소에 대해 주어진 callback 함수를 실행하며, **callback 함수의 반환값을 요소로 하는 새로운 배열을 반환**한다.
* **배열을 다른 형식으로 바꿔야 할 때 사용**한다.

```javascript
arr.map(callback(element, index, array))
```

* 예시

  ```javascript
  const numbers = [1, 2, 3]
  
  const doubledNumbers = numbers.map(function (number) {
      return number * 2
  })
  doubledNumbers
  ```

* 연습

  * 숫자가 담긴 배열로 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드세요.

  ```javascript
  const newNumbers = [4, 9, 16]
  
  const roots = newNumbers.map(function (number) {
      return number ** 0.5
  })
  
  const roots = newNumbers.map(Math.sqrt)
  roots
  ```



#### filter

* 주어진 **callback 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환**한다.
* 즉, 주어진 callback 함수로 원하는 요소만 filtering 할 수 있다.

```javascript
arr.filter(callback(element, index, array))
```

* 예시

  ```javascript
  const products = [
    { name: 'cucumber', type: 'vegetable' },
    { name: 'banana', type: 'fruit' },
    { name: 'carrot', type: 'vegetable' },
    { name: 'apple', type: 'fruit' },
  ]
  
  const fruits = products.filter(function (product) {
      return product.type === 'fruit'
  })
  
  // arrow function
  ```

* 연습

  * numbers 배열 중 50보다 큰 값들만 모은 배열 filteredNumbers을 만드세요.

  ```javascript
  const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
  
  const filterdNumbers = numbers.filter(function (number) {
      return number > 50
})
  
  const filterdNumbers = numbers.filter(number => number > 50)
  ```
  
  

#### reduce

* 배열의 각 요소에 reduce 함수를 실행하고, 하나의 결과값을 반환한다.
* reduce는 배열 내의 숫자 총합, 평균 계산 등 배열의 값을 하나로 줄이는 동작을 한다.

```javascript
arr.reduce(callback(acc, element, index, array), initialValue)
```

* map, filter 등 여러 배열 메서드의 동작을 대부분 대체할 수 있다.
* `acc` : 누적 값 (전 단계의 결과)
* `initialValue` : 반환할 누적 값의 초기 값 (없을 시 첫번째 요소 값이 누적 값이 된다)



* 예시

  ```javascript
  const numbers = [5, 5, 10, 7]
  
  const result = numbers.reduce(function (total, number) {
    return total + number
  })
  ```

  

#### find

* 주어진 판별 함수를 만족하는 첫번째 요소의 값을 반환한다.
* 값이 없다면 `undefined`를 반환한다.

```javascript
arr.find(callback(element, index, array))
```

* 예시

  ```javascript
  const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32 },
    { name: 'Thor', age: 40 },
  ]
  
  const avenger = avengers.find(function (avenger) {
    return avenger.name === 'Tony Stark'
  })
  
  
  // refactoring
  const avenger = avengers.find(avenger => avenger.name === 'Tony Stark')
  ```

  

#### some

* 배열 안의 어떤 요소라도(=== 하나라도) 주어진 판별 함수를 통과하면 `true`를 반환, 아닐 시 `false`를 반환한다.

* 단, 빈 배열에서 호출 시 `false`를 반환한다.

```javascript
arr.some(callback(element, index, array))
```

* 예시

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  
  const result = numbers.some(function (number) {
    return number === 3
  }) // True
  
  
  // refactoring
  
  ```

  

#### every

* 배열 안의 모든 요소가 주어진 판별 함수를 통과하면 `true`를 반환, 아닐 시 `false`를 반환한다.

* 단, 빈 배열에서 호출 시 `true`를 반환한다.

```javascript
arr.every(callback(element, index, arrary))
```

* 예시

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  
  const result = numbers.every(function (number) {
    return number !== 0
  })
  
  
  // refactoring
  
  ```

  

