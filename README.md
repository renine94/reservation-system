# 코드 실행
1. `docker-compose -f infra/docker-compose.yml up -d`
- 실행전, 본인 로컬에서 8000, 5432, 6379, 80번 포트 사용중인걸 모두 종료해주세요.
- Backend: 8000
- PostgresQL: 5432
- Redis: 6379
- Nginx: 80
- Docker-Compose 로 실행하지 않는다면 로컬에서 압축푼뒤, runserver 명령을 통해서도 가능 (sqlite3 삭제후 재생성 권장)
  - 로컬에서는 sqlite3
  - docker-compose는 prod 환경일때를 가정하여 db, cache, nginx 등 붙였습니다.

  
2. 회원가입과 같은 특수한 API 를 제외하고 대부분의 API는 유저인증이 되어있어야 합니다.<br>아래의 API 명세 또는 [Swagger](http://localhost/swagger/) 을 통해 회원가입과 로그인후 access_token 을 header 에 넣어주셔야 합니다.


# ERD
![ERD](assets/images/img.png)


# 사용 기술
- python3.12
- django==4.2.7
- djangorestframework==3.15.2
- authentication (token based jwt)
- permission
- pagination

# API 명세

> [Swagger](http://localhost/swagger/) 을 참고하거나 postman_example.json 파일을 import 하셔도 됩니다.

### User

|                  | Method | Endpoint                     | Data                                 | Auth required |
| ---------------- | ------ | ---------------------------- | ------------------------------------ | ------------- |
| 유저 목록 조회   | GET    | /api/v1/users/               |                                      |               |
| 유저 단일 조회   | GET    | /api/v1/users/{id}/          |                                      |               |
| 유저 회원 가입   | POST   | /api/v1/users/               | username, email, password, password2 |               |
| 유저 회원 탈퇴   | DELETE | /api/v1/users/{id}/          |                                      | O             |
| 유저 로그인      | POST   | /api/v1/users/login/         | email, password                      |               |
| 유저 로그인 갱신 | POST   | /api/v1/users/login/refresh/ |                                      |               |
| 유저 로그아웃    | POST   | /api/v1/users/logout/        | refresh                              | O             |
| **내 정보 조회** | GET    | /api/v1/users/me/            |                                      | O             |



### Reservation
- TBD


# 특별히 신경 쓴 부분
1. TBD

# 최종 구현된 범위
- TBD


# ENV
```
# DJANGO
SECRET_KEY='django-insecure-c4!s(6lk2km#d&2+cnelljxgtg@shv_w@@avq0(mv4%8*h16c1'

# DB
DB_NAME='postgres'
DB_USER='postgres'
DB_PASSWORD='postgres'
DB_HOST='db'
DB_PORT='5432'

# Cache
REDIS_HOST='redis://redis:6379/0'
```
