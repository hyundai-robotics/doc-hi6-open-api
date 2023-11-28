## 1.1 Hi6 Open API 개요

### 1.1.1 API 란?

`API`(Application Programming Interface)란 어플리케이션 소프트웨어를 빌드하고 통합하기 위한 `정의 및 프로토콜 세트`입니다 ([참조](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)).
사용자가 `특정한 방식으로 구성된 요청`을 보내면 제공자의 소프트웨어가 이에 `응답하는 방식`입니다.
이를 통해 구현 방식을 알지 못하는 제품 또는 서비스와도 통신할 수 있으며 어플리케이션 개발을 간소화하여 시간과 비용을 절약할 수 있습니다.

<br>


### 1.1.2 REST API 란?

`REST`(Representational State Transfer)는 API 작동 방식에 대한 조건을 부과하는 `소프트웨어 아키텍처`입니다.
`REST API`는 REST 아키텍처 스타일을 따르는 API 를 뜻합니다. RESTful API 라고도 합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)). HTTP 요청을 통해 통신함으로써 리소스 내에서 레코드의 작성(Create), 읽기(Read), 업데이트(Update) 및 삭제(Delete) 등의 표준 데이터베이스 기능(CRUD)을 수행합니다. <br>

개발자는 종종 4가지의 일반적인 Hypertext Transfer Protocol(HTTP) 메서드를 사용하여 RESTful API를 구현합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)).

- `GET` : 클라이언트는 GET을 사용하여 서버의 지정된 URL에 있는 리소스에 액세스합니다. GET 요청을 캐싱하고 RESTful API 요청에 파라미터를 넣어 전송하여 전송 전에 데이터를 필터링하도록 서버에 지시할 수 있습니다.
- `POST` : 클라이언트는 POST를 사용하여 서버에 데이터를 전송합니다. 여기에는 요청과 함께 데이터 표현이 포함됩니다. 동일한 POST 요청을 여러 번 전송하면 동일한 리소스를 여러 번 생성하는 부작용이 있습니다.
- `PUT` : 클라이언트는 PUT을 사용하여 서버의 기존 리소스를 업데이트합니다. POST와 달리, RESTful 웹 서비스에서 동일한 PUT 요청을 여러 번 전송해도 결과는 동일합니다.
- `DELETE` : 클라이언트는 DELETE 요청을 사용하여 리소스를 제거합니다. DELETE 요청은 서버 상태를 변경할 수 있습니다. 하지만 사용자에게 적절한 인증이 없으면 요청은 실패합니다.

<br>

### 1.1.3 Hi6 Open API 에 대하여

HD현대로보틱스는 로봇 제어기에서 활용되는 여러 REST API 들을 해당 문서에서 Hi6 Open API 로 정리하여 공개합니다. 외부 어플리케이션 개발자는 Hi6 제어기의 소스코드 구현에 대한 이해 없이도 해당 문서를 통해 필요한 정보들을 직접 로봇 제어기에 요청하고 결과를 확인할 수 있습니다. 현재 공개되는 API 는 초기 버전으로 이후 버전 업데이트가 있을 수 있습니다. HTTP REST API 클라이언트 기능 개발에 익숙한 개발자라면 해당 문서의 `1.1 Hi6 Open API 개요`부터 `1.5 postman` 까지의 기본적인 api 사용법 및 api 검증 방법을 숙지할 필요는 없습니다.