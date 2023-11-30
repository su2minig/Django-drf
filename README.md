# Django-drf

# 목표와 기능

## 목표

 * 서로의 지식을 공유하는 블로그
 * GPT API를 통해 질문을 하고 답변을 기록 및 공유

## 기능
 * 게시물 CRUD
 * 회원가입, 로그인, 로그아웃
 * CHAT GPT를 이용한 챗봇

# 개발 기술 및 환경
[FE]

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<!-- <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> -->

[BE]

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

[Tool]

<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white">

[WBS]




# 요구사항 및 기능명세

![요구사항 및 기능명세](https://github.com/su2minig/Django-drf/assets/141402694/84a5aef9-7599-4b70-8443-8034a7eee367)

# 데이터베이스

* ERD

![ERD](https://github.com/su2minig/Django-drf/assets/141402694/24aa62ee-de04-495a-aa39-997ac6895b20)


# 프로젝트 구조

```python
📦BE
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂chatbot
 ┃ ┣ 📂migrations
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┗ 📜chat.html
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂drf_project
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜db.sqlite3
 ┗ 📜manage.py
```

# API 명세서

![api 명세서](https://github.com/su2minig/Django-drf/assets/141402694/40b88cce-43be-4cbd-934a-1883a689ad84)

# 메인기능

## 회원가입

![회원가입](https://github.com/su2minig/Django-drf/assets/141402694/02188cbe-bd8e-4ebb-8dc2-588491e9a6ce)

## 로그인/로그아웃

![로그인 로그아웃](https://github.com/su2minig/Django-drf/assets/141402694/87efc680-209d-4f3c-979c-d4c4fc84ab48)

## 게시물 작성

![게시물작성](https://github.com/su2minig/Django-drf/assets/141402694/8045ebe5-f679-4f9d-bbf3-28426a566822)

## 게시물 수정

![게시물 수정](https://github.com/su2minig/Django-drf/assets/141402694/b6286a30-e80d-4916-b3a0-ea85118d1f92)

## 게시물 삭제

![게시물 삭제](https://github.com/su2minig/Django-drf/assets/141402694/f7adf25a-44e1-4a4c-b4bc-de975acc3f36)

# 트러블슈팅

* 게시물 수정에서 작성자를 입력해줘야하는 문제가 발생
    
    * 원인: PUT요청은 해당 리소스의 모든 상태를 대체하기 때문에 작성자 부분까지 입력을 해줘야하는 상황이 발생했습니다.

    * 해결방안:
    작성자 부분의 수정을 막기위해 author에 `read_only_fields`로 해주고 views.py에서 해당 코드에 partial=True를 추가해 부분 업데이트를 허용해 해결하였습니다.
    ```python
    # blog > serializers,py
    author = serializers.ReadOnlyField(source='author.username')

    read_only_fields = ['author']
    ```

    ```python
    class PostDetailAPIView(APIView):
        def put(self, request, pk):
            serializer = PostSerializer(post, data=request.data, partial=True) # partial=True 추가
    ```
