## 1. media 파일 경로

```python
미디어 파일
실제 파일이 저장되는 위치:MEIA_ROOT = BASE/'프로젝트 이름'/'uploaded_files'
서버가 실행됐을 때 미디어 파일을 참조하는 URL:MEDIA_URL = '/media/'
```

## 2. DB True and False

``` python
1) RDBMS를 조작하기 위해 SQL문 사용한다. True
2)SQL에서 명령어는 반드시 대문자로 작성해야 동작한다. False
3) 일반적인 SQL 문에서는 세미콜론까지를 하나의 명령어로 간주한다. True
4) SQLite에서 .tables, .headers on과 같은 dot(.)로 시작하는 명령어는 SQL문이 아니다. True
(SQLite의 기능일 뿐이다.)
5) 하나의 데이터베이스 안에는 반드시 한 개의 테이블만 존재해야 한다. False
```

## 3. on_delete

```python
게시글과 댓글의 관계에서 댓글이 존재하는 게시글은 삭제할 수 없도록 하는 (a)
(a): PROTECT
on_delete=models.PROTECT
ProtectedError를 발생시킴.
```

## 4. like

```python
(a): ManyToManyField
(b): related_name
```

## 5. follow

```python
중계 테이블 이름:accounts_user_followings
필드 이름:from_user_id, to_user_id
```

