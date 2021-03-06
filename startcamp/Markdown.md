# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로, 사용법이 쉽고 간결하여 빠르게 문서 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1.문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다.
>
> 단순히 글자의 크기를 표현하는 것이 아니라, 의미론적인 중요도를 나타냅니다.

- `<h1>`부터`<h6>`까지 표현 가능합니다.
- `#`의 개수로 표현하거나 <hl></h1>형태로 표현 가능합니다.



<h1>hl 태그입니다.</h1>

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5 태그입니다.

###### h6 태그입니다.



#### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 순서가 필요없는 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래에 순서가 없는 항목을 지정할 수도 있으며, 그 반대도 가능합니다.

- 순서가 있는 목록
  - `1.`을 작성하고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab`을 눌러서 하위 항목을 생성할 수 있고, `shift + tab`을 눌러서 상위 항목으로 이동할 수도 있습니다.
- 순서가 없는 목록
  - 하이픈(-) 또는 애스터리스크(*)를 작성하고 스페이스바를 누르면 생성할 수 있습니다.
  - `tab`을 눌러서 하위항목을 생성할 수 있고, `shift + tab`을 눌러서 상위 항목으로 이동할 수도 있습니다.



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다.
>
> 인라인과 블럭 단위로 구분할 수 있습니다.

- 인라인(Inline)

  - 인라인 블럭으로 처리하고 싶은 부분을 백틱(`)으로 감쌉니다.

- 블럭(Block)

  - 백틱을 3번 입력하고 엔터를 눌러 생성합니다.

  

  ```python
  hello = '안녕하세요!'
  print(hello)
  #=> 안녕하세요!
  ```

  


### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나, 이미지 URL을 통하여 이미지를 삽입할 수 있습니다.

- `![]()`를 작성하고,`()`안에 이미지 주소를 삽입합니다.`[]`안에는 이미지 이름을 작성합니다.

  

  ![](Markdown.assets/IU_MelOn_Music_Awards_2017_06.jpg)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

- `[]()`를 작성하고, `()`안에 주소를 적습니다.`[]`안에는 주소 제목을 적습니다.

[네이버](https://naver.com)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- 파이프(`|`)사이에 컬럼을 작성하고 엔터를 누릅니다.
- `ctrl + 엔터`를 통해 새로운 행을 작성합니다.



| 제목   | 설명            |
| ------ | --------------- |
| Python | 프로그래밍 언어 |
| HTML   | 마크업 언어     |



### 1.7 기타

#### 1.7.1 인용문

- `>`를 작성하고 스페이스바를 누릅니다.

> 이것은 인용문입니다.

- 인용문 안에 인용문을 중첩해서 작성할 수 있습니다.

> 인용문입니다.
>
> > 중첩 인용문입니다.



#### 1.7.2 수평선

- `---`또는 `***` 또는 `___`를 입력하여 수평선을 생성합니다.



첫 번째 단락

---

두 번째 단락

***

세 번째 단락

___



#### 1.7.3 강조

- 이탤릭체
  - 해당 부분을 애스터리스크(`*`)또는 언더스코어(`_`)로 감싸줍니다.
  - 이것은 *이탤릭체*입니다.

- 볼드체
  - 해당 부분을 애스터리스크 2개(`**`)또는 언더스코어 2개(`__`)로 감싸줍니다
  - 이것은 **볼드체**입니다.
- 취소선
  - 해당 부분을 물결표 2개(`~~`)로 감싸줍니다.
  - 이것은 ~~취소선~~입니다.



