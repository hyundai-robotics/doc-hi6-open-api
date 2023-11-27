# 1.4 REST API 테스트

REST API 테스트를 하는 방법은 여러가지가 있습니다. 해당 섹션에서는 다양한 방법 중 대표적인 방법에 대해서 살펴보겠습니다.

1.3.1 `postman` 프로그램 활용하기 <br>
1.3.2 웹 브라우저 활용하기 <br>
1.3.3 간단한 client 소스 코드 작성 및 실행

<br>

## 1.4.1 `postman` 프로그램 활용하기
- `postman` 은 세계적으로 많이 사용되는 API 테스팅 플랫폼 입니다.
- `workspace` 기능을 통해 프로젝트 단위의 API 테스트와 history 추적이 가능하고 언어별 Code snippet, 직관적 ui 를 갖추고 있습니다.
- [1.5 Postman 사용법](./5-postman.md)에서 간단한 사용법을 확인할 수 있습니다.


<br>


## 1.4.2 웹 브라우저 활용하기
- `get` 요청은 웹 브라우저를 통해 보다 간편하고 신속하게 확인할 수 있습니다.
- 순서는 다음과 같습니다.
	1. 웹 브라우저 엽니다.
	2. 주소 창에 `get` 요청의 서버 측 url 을 입력합니다.
		- 서버 측 url 은 `http://<Hi6 제어기의 ip 주소>:<http 통신 포트>`로 시작되며 추출하려는 정보에 맞는 경로와 쿼리를 이어 적습니다.
		- ex) ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
	3. 해당 url 의 페이지가 열리고 아래와 같이 response 값이 출력됩니다.
		```json
		{
			"_type" : "JObject",
			"val" : -99
		}
		```
- 추가로, 크롬 브라우저를 사용하는 경우, 크롬 확장 프로그램을 통해 `get` 요청 이외의 api 들을 테스트할 수 있습니다.
	- 크롬 확장 프로그램 : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)
	- 사용법은 앞서 언급한 `postman` 사용법과 비슷하므로 해당 문서에서는 생략합니다.


<br>


## 1.4.3 간단한 client 소스 코드 작성 및 실행
- 소스 코드를 통해 간단한 테스트 가능합니다.
- 테스트하고 싶은 path-parameter 와 query-parameter 를 API method 에 맞게 작성하면 됩니다.
- [1.3 예제 코드](./3-sample-code/README.md) 와 이후 API 설명 페이지에서 확인하실 수 있습니다.