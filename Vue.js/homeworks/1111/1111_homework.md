1111 Homework

```javascript
T/F
- Vue에는 라이프사이클 훅에서 created Hook은 Vue template에 작성된 요소들이 DOM에 다 그려지는 시점에 실행된다. False
- npm은 Node Package Manager의 약자이며, npm을 통해 설치한 package 목록은 package.json파일에 자동으로 작성된다. True
- vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM 조작이나 WEB API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다. False
```



```javascript
history mode가 무엇인지 서술.
디폴트인 해쉬모드의 경우, 해쉬 뒤쪽을 주소로 인지하는 반면, 히스토리 모드의 경우 해쉬 없는 URL 창을 활용할 수 있음.
```



```javascript
created -> vue 인스턴스가 만들어지고 난 후, DOM에는 아직
mounted -> 돔에 부착 완료
updated -> 돔이랑 연동된 데이터가 수정됐을 때, 즉 돔이 수정됐을 때
Vue application이 실행되면 created, mounted만 찍힘(created와 mounted에 기술된 함수만 수행됨. update는 앱 실행단계에서 이루어지지 않으므로.)
```

