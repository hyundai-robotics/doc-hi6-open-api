# 1.4 Postman을 활용한 POST 시험

Postman으로 POST 요청을 시험할 수 있습니다.

1. `Request Header` 작성 
	- Headers 탭에 아래의 Key-Value를 입력합니다.
  	- Content-Type 관련 ([postman](https://blog.postman.com/what-are-http-headers/#Content-type) 참조)
	<br>
	![postman_headers](../_assets/02_postman_headers.png)

<br>

2. `Request Body` 작성 
	- API method 를 `POST` 로 선택하고 URL을 입력합니다.
	- Body 탭 클릭 후 요청하려는 `body-parameter`를 입력합니다. ([2.2.1 `task/cur_prog_cnt` - request body](../2-project/2-post/1-task-cur_prog_cnt.md/#request-body) 참조)
	- Send를 클릭합니다.
	<br>
	![postman_post](../_assets/03_postman_post.png)

<br>

3. `Response` 확인 및 `Code Snippet` 참조
	- `request` 요청이 정상적으로 완료되면 아래 그림과 같이 `HTTP Status` 가 `200 OK`로 응답합니다. ([HTTP Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 참조)
	- 해당 url 이 적용된 언어별 `Code snippet` 또한 확인 가능합니다.
	![postman_post_result](../_assets/04_postman_post_result_check.png)
		- `(1) Response body` : `post` 에 대한 응답 결과 ([2.2.1 `task/cur_prog_cnt` - response body](../2-project/2-post/1-task-cur_prog_cnt.md/#response-body) 참조)
		- `(2) Request` 에 대한 python `Code snippet`