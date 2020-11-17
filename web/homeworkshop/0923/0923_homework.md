## 1) 1:N True or False

```python
1) ForeignKey는 부모 테이블의 데이터를 참조하기 위한 키이다.
True
2) 1:N 관계에서 1은 N의 데이터를 직접 참조할 수 있다.
False 못해서 django의 힘으로 역참조해야함. _set
3) on_delete 속성은 ForeignKey 필드의 필수 인자이다.
True
4) 1:N 관계에서 ForeignKey는 반드시 부모 테이블의 PrimaryKey여야 한다.
False 굳이 그럴 필요 없음. unique하면 됨. 일반적으로는 PK를 씀.
```

## 2) ForeignKey column name

```python
answer_id
articles_comment
```

## 3) 1:N ORM in template

```python
question.comment_set.all
```

## 4) ?next=

```python
Login 페이지 가서, 로그인 끝내고 Redirect 돼서 다시 돌아옴.(GET Method)
허용되지 않은 Method인 경우 상태 코드
=> 405

@login_required
def delete(request,article_pk):
    if request.method == 'POST':
```

