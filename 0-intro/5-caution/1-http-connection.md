## 1. API 통신 시 주의 사항
{% hint style="caution" %}

로봇 제어기의 경우, close 연결 방식으로 API 요청이 반복적으로 이뤄지면 cpu 부하가 발생하여 로봇이 정지되는 에러가 발생할 수 있습니다.

지속적으로 API 를 여러번 호출하는 경우, 하기 메뉴얼에 따라 **Keep-Alive 방식**으로 기능 구현을 해주십시오.

{% endhint %}

<br>

#### 1-1. Keep-Alive 연결 vs Close 연결

<div style="max-width: fit-content">

| | Close | Keep-Alive |
|--| ----- | ----- |
|제안된 Http 버전| Http/1.0 | Http/1.1|
|특징| Multiple Connection | Persistent Connection |

<img src="../../_assets/07_http_connection.png" style="max-height: 37vh;">

</div>

- close 연결 방식은, 많은 요청과 응답이 필요한 상황에서도 매번 연결을 맺고 끊는 과정이 이루어집니다.<br>
  이러한 동작은 처리 시간과 리소스를 낭비하며, 서버와 클라이언트 모두에게 과도한 부담을 초래합니다.

- Hi6는 HTTP/1.1을 사용하고 있습니다. 따라서 별도의 설정을 바꾸지 않는 경우, 자동으로 Keep-Alive 방식으로 동작합니다.

- 아래 예제 코드를 참조하여, 반복 호출되는 API 들은 close 방식이 아닌 keep-alive 방식으로 구현하십시오.

<br>

#### 1-2. 예제 코드

- 간단하게 close 방식과, keep-alive 방식을 변경할 수 있습니다.
- close 연결 방식
  <div style="max-width:fit-content">

	```python
	import requests
	import time

	BASE_URL = "http://192.168.10.150:8888"
	URI = "/project/robot/po_cur"
	URL = BASE_URL + URI
	headers = { "Connection": "close" }

	response = requests.get(URL, headers=headers)
	```
	</div>
- keep-alive 연결 방식
  <div style="max-width:fit-content">

	```python
	import requests
	import time

	BASE_URL = "http://192.168.10.150:8888"
	URI = "/project/robot/po_cur"
	URL = BASE_URL + URI

	# default connection is Keep-alive
	response = requests.get(URL)
	```
	</div>
- 패킷 캡쳐 비교<br>
	<img src="../../_assets/08_packet_compare.png" style="max-width: 80vw;"><br>
	좌) Keep-Alive, 우) Close

<br><br>

참고 문서
  1) [HTTP/1.1 persistent connection](https://datatracker.ietf.org/doc/html/rfc2616#section-8)