```python
  <script>
    function addTodo () {
      // 1. input 선택해서, 사용자가 입력한 값 가져오기
      const input = document.querySelector('input')
      const content = input.value

      // 2. li 요소를 새롭게 생성하고, 사용자가 입력한 값을 넣기
      const li = document.createElement('li')
      li.innerText = content
      
      // 3. ul 요소를 선택해서
      const ul = document.querySelector('ul')
      ul.appendChild(li)

      // 4. 작성한 내용은 초기화
      input.value = ''
    }

    // 요소 선택하기
    const form = document.querySelector('#todo-form')
    // 이벤트 리스너 추가
    form.addEventListener('submit', function() {
      // 요청이 발생하는 form의 기본 작업을 중단시킨다.
      event.preventDefault()
      // Todo를 생성하는 함수 실행
      addTodo()
    })
  </script>
```

