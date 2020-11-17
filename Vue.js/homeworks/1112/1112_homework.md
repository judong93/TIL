```javascript
1. T/F
- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향한다. False
- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달받은 함수를 실행한다. True
- 컴포넌트에서 클릭 이벤트 발생 시 특정 함수를 실행하고자 할 때, @click 혹은 v-on:click 디렉티브를 사용한다. ex) <Todo @click.native="" />  따라서 False .native 사용해야함.
- 부모는 props를 통해 자식에게 이벤트를 보내고 자식은 부모에게 emit을 통해 데이터를 보낸다. False props는 데이터 보내고, emit은 이벤트 보냄
```

```
2. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크이다. 그 이유를 서술하시오.
모든 props는 하위 속성과 상위 속성 사이의 단방향 바인딩을 형성합니다. 상위 속성이 업데이트되면 하위로 흐르게 되지만 그 반대는 안됩니다. 이렇게하면 하위 컴포넌트가 실수로 부모의 상태를 변경하여 앱의 데이터 흐름을 추론하기 더 어렵게 만드는 것을 방지할 수 있습니다.
```

```
3.
(a)this.$emit
(b)@addTodo="onAddTodo"
(c)onAddTodo: function (text) {
 console.log(text)
}
```

