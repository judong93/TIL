path 괄호 맨뒤에 name을 붙여주는 이유.

url이 바뀌게 되면 주소 다찾아다니면서 바꿔줘야함. 이게 name 붙여주는거

이후 ex_) form action에 {% 'catch' %} 이런 식으로 하면 됨.



앱네임의 경우, 앱이 많아질 경우, 다른 앱과 중복될 수 있기 때문에

appname을 따로 붙여서 사용.

{% artices:catch %} 이런 식으로 사용. 

pages에  catch가 있어도 무관함.



템플릿츠 안에 앱 이름의 폴더를 넣고 html을 넣는 이유.

앱이 여러개고 html이 겹치는 것을 방지하기 위해

pages/lotto

artices/lotto 이런 식으로 나눠 접근.