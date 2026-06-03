
[__SOURCE](README.md)
# ${cont_model} 제어기 기능설명서 - Open API

{% hint style="warning" %}

${cont_model} Open API 설명서에 공식적으로 언급되지 않은 API 를 활용하여 발생하는 모든 피해 및 문제에 대해서는 책임을 지지않습니다.

{% endhint %}

{% hint style="warning" %}

외부 장치, 상위 제어 시스템 또는 네트워크로부터 수신된 신호는 제조자의 직접적인 통제 범위에 포함되지 않으며, 이러한 신호로 인한 오동작 또는 사고에 대한 책임은 사용자에게 있습니다.

{% endhint %}


[__SOURCE](0-about-this-manual/precautions.md)
# 사전 주의사항


{% include file="ko/precautions.md" %}

[__SOURCE](0-intro/README.md)
# 0. 개요

${cont_model} Open API 와 관련된 아래의 기본적인 내용들을 확인하실 수 있습니다.

- [0.1 ${cont_model} Open API 개요](./1-concept/README.md)  
- [0.2 필요한 사전 지식](./2-prerequisite/README.md)  
- [0.3 ${cont_model} Open API 예제 코드](./3-sample-code/README.md)  
- [0.4 코딩하지 않고 쉽게 API 호출 해보기](./4-api-test/README.md)  
- [0.5 시작 전 주의사항](./5-caution/README.md)  


[__SOURCE](0-intro/1-concept/README.md)
## 0.1 ${cont_model} Open API 에 대하여

HD현대로보틱스는 어플리케이션 개발자들이 편리하게 로봇 제어기(이하, ${cont_model})를 모니터링하고 원격으로 제어하기 위한 API 를 해당 문서에서 공개합니다.<br>
이를 통해 개발자들은 ${cont_model} 개발에 적용된 소스코드에 대한 깊은 이해 없이도 ${cont_model} 다양한 데이터를 읽고 쓸 수 있습니다.<br>
아래 그림을 통해서 Open API 역할을 보다 쉽게 이해할 수 있습니다.


<img src="../../_assets/05_open_api_flow.png" style="max-height: 24vh;">


위 그림에서 주황색으로 표시된 부분들은 Open API 의 역할을 보여주고 있습니다.  

<div style="width: fit-content;">

|화살표|설명|
|:---|:---|
|`실선`|개발자(클라이언트)가 정해진 4가지 방법(GET, POST, PUT, DELETE)을 이용하여 ${cont_model}(서버)에 정보를 `요청`하는 것을 의미|
|`점선`|요청을 받은 제어기가 그에 맞는 `응답`을 json 혹은 text 형식으로 반환하는 것을 의미|

</div>

이처럼 개발자는 해당 문서의 Open API 를 활용해서 ${cont_model} 와 이더넷으로 연결된 본인의 데스크탑, 노트북, 태블릿 pc 등을 http 와 REST API 기반으로 원격 제어 또는 모니터링을 할 수 있게 됩니다.


<br><br>


#### 시작하기 전에 꼭 확인하세요!

* 현재 문서는 ${cont_model} Open API 스키마 버전 `5`를 기준으로 작성되었습니다. [API](../../2-version/1-get/1-api_ver.md) 를 통해 확인 가능합니다.

* HTTP REST API 클라이언트 기능 개발에 익숙한 개발자의 경우, [`0.2 필요한 사전 지식`](../2-prerequisite/README.md)부터 [`0.4 코딩하지 않고 쉽게 API 호출 해보기`](../4-api-test/README.md) 까지 건너뛰어도 좋습니다.


{% hint style="warning" %}

본 문서에 설명된 API들은 별도의 지원버전 명기가 없으면 ${cont_model} V60.24-00부터 지원됩니다.

본 문서에 명시되지 않은 URL 및 속성은 동일 API 버전에서 예고없이 변경될 수 있으므로, 주의 바랍니다.

{% endhint %}

[__SOURCE](0-intro/2-prerequisite/README.md)
## 0.2 필요한 사전 지식

Open API를 활용하기 위해서는 ${cont_model} 제어기의 기본적인 사용법을 습득해야 합니다.<br>
아래 설명서를 참고하시거나 HD현대로보틱스 공동훈련센터의 교육을 수강하시기 바랍니다.

- [${cont_model} 로봇제어기 조작설명서](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/ko-tp630/README?cont_model=${cont_model})
- [HD현대로보틱스 공동훈련센터](https://hd-hyundairobotics.com/community/robot-edu-info)

<br>

Open API는 HTTP 프로토콜 기반의 REST API입니다.<br>
다양한 개발 언어들에서 REST API (일명 RESTful API) 호출을 위한 라이브러리를 제공하고 있으며 많은 개발자들이 이를 이용해 프로그램을 개발하고 있습니다.<br>
이러한 숙련된 개발자가 아니라면, [0.1 ${cont_model} Open API 에 대하여](.././1-concept/README.md)에서 언급한 웹 기반의 서비스 호출과 응답이 어떻게 이뤄지는지에 대한 기본적인 개념에는 익숙한 상태여야만 합니다.<br>

이와 관련하여 아래 사항들을 참고하시기 바랍니다.

* 아래의 간단한 API 관련 설명이 낯설거나 이를 응용한 개발 경험이 풍부한 숙련자가 아니면 먼저 학습을 한 후에 해당 문서를 활용하기 바랍니다. 
* 학습이 필요한 경우, REST API 호출을 통한 클라이언트 기능의 코딩 방법을 학습하시기 바랍니다.

<br>


{% hint style="warning" %}

당사는 통상적인 REST API 클라이언트 코딩 방법에 대한 문의는 받지 않습니다.

당사는 ${cont_model} Open API 설명서에 공식적으로 언급되지 않은 API 사용에 의해 발생하는 모든 피해 및 문제에 대해서는 책임을 지지않습니다.

{% endhint %}

---- 

#### 0.2.1 API 란?

`API`(Application Programming Interface)란 어플리케이션 소프트웨어를 빌드하고 통합하기 위한 `정의 및 프로토콜 세트`입니다 ([참조](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)).  
사용자가 `특정한 방식으로 구성된 요청`을 보내면 제공자의 소프트웨어가 이에 `응답하는 방식`입니다.  
이를 통해 구현 방식을 알지 못하는 제품 또는 서비스와도 통신할 수 있으며 어플리케이션 개발을 간소화하여 시간과 비용을 절약할 수 있습니다.

<br>


#### 0.2.2 REST API 란?

`REST`(Representational State Transfer)는 API 작동 방식에 대한 조건을 부과하는 `소프트웨어 아키텍처`입니다.<br>
`REST API`는 REST 아키텍처 스타일을 따르는 API 를 뜻합니다. RESTful API 라고도 합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)).<br>
HTTP 요청을 통해 통신함으로써 리소스 내에서 레코드의 작성(Create), 읽기(Read), 업데이트(Update) 및 삭제(Delete) 등의 표준 데이터베이스 기능(CRUD)을 수행합니다.<br>

개발자는 종종 4가지의 일반적인 Hypertext Transfer Protocol(HTTP) 메서드를 사용하여 RESTful API를 구현합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)).<br>

- `GET` : 클라이언트는 GET을 사용하여 서버의 지정된 URL에 있는 리소스에 액세스합니다. GET 요청을 캐싱하고 RESTful API 요청에 파라미터를 넣어 전송하여 전송 전에 데이터를 필터링하도록 서버에 지시할 수 있습니다.
- `POST` : 클라이언트는 POST를 사용하여 서버에 데이터를 전송합니다. 여기에는 요청과 함께 데이터 표현이 포함됩니다. 동일한 POST 요청을 여러 번 전송하면 동일한 리소스를 여러 번 생성하는 부작용이 있습니다.
- `PUT` : 클라이언트는 PUT을 사용하여 서버의 기존 리소스를 업데이트합니다. POST와 달리, RESTful 웹 서비스에서 동일한 PUT 요청을 여러 번 전송해도 결과는 동일합니다.
- `DELETE` : 클라이언트는 DELETE 요청을 사용하여 리소스를 제거합니다. DELETE 요청은 서버 상태를 변경할 수 있습니다. 하지만 사용자에게 적절한 인증이 없으면 요청은 실패합니다.

[__SOURCE](0-intro/3-sample-code/README.md)
## 0.3 예제 코드

다양한 개발 언어들은 REST API 호출을 위한 라이브러리를 제공하고 있습니다. 활용방법은 각 개발언어의 기술 문서들을 쉽게 검색하여 참고할 수 있습니다.

- 여기서는 C#과 python을 활용한 GET과 POST 메소드의 호출만 설명하도록 하겠습니다.

- IP 주소가 192.168.1.150인 ${cont_model} 제어기에 대해 요청을 수행한다고 가정하겠습니다.

[__SOURCE](0-intro/3-sample-code/1-csharp.md)
#### 0.3.1 예제 코드 - C#

JSON parsing을 위한 라이브러리인 `Newtonsoft.Json`를 사용했습니다.
VisualStudio 프로젝트에 설치되어 있지 않다면, NuGet Package Manager로 설치하시기 바랍니다.

* [Newtonsoft.Json 라이선스 정보](https://github.com/JamesNK/Newtonsoft.Json/blob/master)

1) project 속성 열기
2) `Manage NuGet Packages...`
3) `Online/nuget.org`에서 `Json.NET (James Newton-King)`을 찾아 Install 수행.  
   (혹시, NuGet Package Manager의 버전이 낮아 설치가 안된다는 메시지가 나오면, 주 메뉴의 `TOOLS/Extensions and Updates...`를 선택 후 Updates에서 NuGet 업데이트를 수행하십시오.)  
4) 예제 코드
	<div style="width: fit-content;">

	```csharp
	using System;
	using System.Net;
	using System.IO;
	using Newtonsoft.Json;
	using Newtonsoft.Json.Linq;

	var respText = string.Empty;

	var uri = "http://192.168.1.150:8888";
	var path = "/project/control/ios/dio/do_val";
	var query = "?type=dob&blk_no=2&sig_no=3";

	var request = (HttpWebRequest)WebRequest.Create(uri+path+query);
	request.Method = "GET";
	request.Timeout = 5 * 1000; // 5초

	using (var resp = (HttpWebResponse)request.GetResponse())
	{
		var respStream = resp.GetResponseStream();
		using (var sr = new StreamReader(respStream))
		{
			respText = sr.ReadToEnd();
		}
	}

	var jobj = JObject.Parse(respText);
	var str = "fb2.do3=" + jobj["val"].ToString();
	Console.WriteLine(str);
	```
	</div>

위 소스코드가 포함된 실행 가능한 C# WinForms 샘플 프로그램을 아래 Github 링크를 통해 확인하실 수 있습니다.

<div style="width: fit-content;"> 

> 링크 : [https://github.com/hyundai-robotics/OpenAPI](https://github.com/hyundai-robotics/OpenAPI)

</div>

[__SOURCE](0-intro/3-sample-code/2-python.md)
#### 0.3.2 예제 코드 - python

예제 코드는 크게 `a. 동기식 요청(blocking & 동기식)`방식과 `b. 비동기식 요청(non-blocking & 비동기식)`   
두 가지 방식 중 `a. 동기식 요청`에 대해서 설명합니다.

<div style="width: fit-content;">

||동기식|비동기식|
|:---|:---|:---|
|blocking|`a. 동기식 요청`||
|non-blocking||`b. 비동기식 요청`|

</div>

두 가지 방법의 차이점은 TP와 컨트롤러에 다음과 같은 심각한 결과를 초래할 수 있습니다.
1. UI 스레드에서 빈번한 동기 함수 호출로 인해 UI가 원활하게 실행되지 않고 정지될 수 있습니다(`Hanging 문제`).
2. 서버(컨트롤러) 측의 문제로 인해 응답을 받지 못하는 경우, 애플리케이션 UI가 정지될 수 있습니다(`Hanging 문제`).

따라서 실제 애플리케이션을 개발할 때에는 비동기식 요청 기반으로 작성하시기 바랍니다.
- ${cont_model} Open API 설명에 작성된 Python 스크립트 예시는 이해하기 쉽도록 동기적으로 작성되었으니 유의하시기 바랍니다.

<br><br>

* a. 동기식 요청
동기식은 하나의 요청이 끝나고 응답이 올 때까지 다른 task 의 실행이 불가능한 blocking 상태의 요청 방식 입니다.  
python 에서 `동기식` HTTP 요청을 위해 많이 사용되는 라이브러리는 `requests` 입니다.  
`requests` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다.   	

<div style="width: fit-content;">

```sh
$pip install requests
```
</div>

- 통신시 응답을 받지 못하거나 응답을 받는데 시간이 오래 걸리는 경우에는 hanging 문제가 발생할 가능성이 매우 높으니 주의 바랍니다.
<div style="width: fit-content;">

```python
# sync.py - 동기식, 사용자 IO 출력 값 얻기와 설정하기
import requests
import time

url='http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) fb2.do3 값 설정하기
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
start_time = time.time()
resp = requests.post(url + path, headers=head, json=req_body)
end_time = time.time()
print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

# (GET) fb2.do3 값 가져오기
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")
```
```bash
$python sync.py
[post] 0x79 to fb2.do3 Time taken: 0.00573277473449707 seconds
[get] 0x79 from fb2.do3 Time taken: 0.054880380630493164 seconds
[get] 0x79 from fb2.do3 Time taken: 0.060916900634765625 seconds
[get] 0x79 from fb2.do3 Time taken: 0.06047677993774414 seconds
[get] 0x79 from fb2.do3 Time taken: 0.04827427864074707 seconds
[get] 0x79 from fb2.do3 Time taken: 0.06168508529663086 seconds
total request time : 0.2869541645050049 seconds
```
</div>

[__SOURCE](0-intro/4-api-test/README.md)
## 0.4 코딩하지 않고 쉽게 API 호출 해보기

[앞선 예제 코드](../3-sample-code/README.md)처럼 client 어플리케이션을 개발하면서 Open API 를 사용하는 경우, 코딩을 따로 하지 않고도 손쉽게 API를 호출해 볼 수 있습니다.  
이러한 호출 과정을 통해서 요청이 제대로 동작했는지, 응답으로 어떠한 데이터가 반환되는지 확인 가능 합니다.  
이를 위한 방법은 여러가지가 있습니다. 해당 섹션에서는 대표적인 2가지를 다루고 있습니다.

<br>

#### 1) `postman` 활용하기

`postman` 은 세계적으로 많이 사용되는 API 테스팅 플랫폼 입니다.  
`workspace` 기능을 통해 프로젝트 단위의 API 테스트와 history 추적이 가능하고 언어별 Code snippet, 직관적 ui 를 갖추고 있습니다.  
[0.4.1 Postman 에서 POST 요청하기](./1-postman.md)에서 간단한 사용법을 확인할 수 있습니다.


<br>


#### 2) `웹 브라우저` 활용하기

간단한 `get` 요청은 웹 브라우저를 통해 간편하고 신속하게 확인할 수 있습니다.  
추가로 웹 브라우저의 확장 프로그램을 활용하여 `get` 요청과 다른 API 요청들을 직접 호출하고 결과를 볼 수 있습니다.  
[0.4.2 웹 브라우저에서 API 호출하기](./2-web-browser.md)에서 간단한 사용법을 확인할 수 있습니다.

[__SOURCE](0-intro/4-api-test/1-postman.md)
#### 0.4.1 `Postman` 에서 `POST` 요청하기

해당 페이지에서는 `postman` 을 활용해서 REST API 의 `POST` 요청을 호출하고 결과를 확인합니다.  
추가로 간단한 UI 구성을 통해 사용법을 파악합니다.

<br>

##### a. 주요 UI 구성

아래 그림을 통해 주요 UI 구성을 확인할 수 있습니다. <br>

<img src="../../_assets/01_postman_desc.png" style="max-height: 40vh;">

<blockquote style="width: fit-content;">

(1) `+` 버튼을 통해 request 요청을 간단하게 생성할 수 있습니다. </br>
(2) `request` 요청에 대한 정보들을 입력하는 공간 입니다. </br>
(3) `response` 에 대한 정보들을 확인하는 공간입니다. </br>
(4) `request` url 이 적용되어 자동으로 생성된 언어별 `Code snippet`을 확인하는 공간입니다. </br>

</blockquote>

<br>

##### b. POST 요청 시험하기

1. `Request Header` 작성 
	- Headers 탭에 아래의 Key-Value를 입력합니다.
  	- Content-Type 관련 ([postman](https://blog.postman.com/what-are-http-headers/#Content-type) 참조)
	<br><img src="../../_assets/02_postman_headers.png" style="max-height: 14vh;">

<br>

2. `Request Body` 작성 
	- API method 를 `POST` 로 선택하고 URL을 입력합니다.
	- Body 탭 클릭 후 요청하려는 `body-parameter`를 입력합니다. ([9.2.1 `task/cur_prog_cnt` - request body](../.././9-task/2-post/1-cur_prog_cnt.md) 참조)
	- Send를 클릭합니다.  
		<img src="../../_assets/03_postman_post.png" style="max-height: 30vh;">

<br>

3. `Response` 확인 및 `Code snippet` 참조
	- `request` 요청이 정상적으로 완료되면 아래 그림과 같이 `HTTP Status` 가 `200 OK`로 응답합니다. ([HTTP Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 참조)
	- 해당 url 이 적용된 언어별 `Code snippet` 또한 확인 가능합니다.  
	<img src="../../_assets/04_postman_post_result_check.png" style="max-height: 40vh;">

		<blockquote style="width: fit-content;">

		`(1) Response body` : `post` 에 대한 응답 결과 ([9.2.1 `task/cur_prog_cnt` - response body](../.././9-task/2-post/1-cur_prog_cnt.md) 참조)</br>
		`(2) Request` 에 대한 python `Code snippet`

		</blockquote>

[__SOURCE](0-intro/4-api-test/2-web-browser.md)
#### 0.4.2 웹 브라우저에서 API 호출하기

##### a. 간단한 `GET` 요청하기

`get` 요청은 웹 브라우저를 통해 보다 간편하고 신속하게 확인할 수 있습니다. 순서는 다음과 같습니다.
1. 웹 브라우저 엽니다.
2. 주소 창에 `get` 요청의 서버 측 url 을 입력합니다.
	- 서버 측 url 은 `http://<${cont_model:lower} 제어기의 ip 주소>:<http 통신 포트>`로 시작되며 추출하려는 정보에 맞는 경로와 쿼리를 이어 적습니다.
	- ex) ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
3. 해당 url 의 페이지가 열리고 아래와 같이 응답이 출력됩니다.

	<div style="width: fit-content;">

	```json
	{
		"_type" : "JObject",
		"val" : -99
	}
	```
	</div>

<br>

##### b. `확장 프로그램`으로 API 호출하기  
크롬 또는 엣지 브라우저를 사용하는 경우, 크롬 확장 프로그램을 통해 `get` 요청 이외의 api 들을 테스트할 수 있습니다.  
하기 확장 프로그램은 세계적으로 여러 개발자들이 사용하는 API 테스터 입니다.
- 크롬 확장 프로그램 : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)  

해당 프로그램을 통해 `postman` 처럼 다양한 API 들에 대해서 간편하게 호출을 해볼 수 있습니다.

<img src="../../_assets/06_Talend_api_tester.png" style="max-height: 60vh;">


<blockquote style="width: fit-content;">

`(1) Requests/Senarios` : 하나의 API 에 대해서 호출을 테스트할지, 여러 API 들로 시나리오를 작성하여 순차적으로 테스트할 지 설정할 수 있습니다.<br>
`(2) Request` : 요청할 내용을 입력합니다.  
`(3) Response` : 요청에 대한 응답을 확인할 수 있습니다.  
`(4) History` : 요청 이력을 출력합니다.  
`(5) History 탭` : 열었다 닫았다 할 수 있는 `(4)`의 요청 이력 리스트보다 많은 양의 이력이 확인 가능한 탭입니다.

</blockquote>

[__SOURCE](0-intro/5-caution/README.md)
## 0.5 주의 사항

{% hint style="warning" %}

로봇 제어기에 심각한 에러를 유발할 수 있는 주의 사항과 관련된 내용들을 정리합니다.
해당 내용들을 인지하여 API 를 사용하여 주십시오.

{% endhint %}


[__SOURCE](0-intro/5-caution/1-http-connection.md)
#### 0.5.1. Keep-Alive vs Close connection

{% hint style="warning" %}

로봇 제어기의 경우, close 연결 방식으로 API 요청이 반복적으로 이뤄지면 cpu 부하가 발생하여 로봇이 정지되는 에러가 발생할 수 있습니다.
지속적으로 API 를 여러번 호출하는 경우, 하기 메뉴얼에 따라 **Keep-Alive 방식**으로 기능 구현을 해주십시오.

{% endhint %}

<br>

##### 1-1. Http 연결 방식 비교

<div style="max-width: fit-content">

| | Close | Keep-Alive |
|--| ----- | ----- |
|제안된 Http 버전| Http/1.0 | Http/1.1|
|특징| Multiple Connection | Persistent Connection |

<img src="../../_assets/07_http_connection.png" style="max-height: 37vh;">

</div>

- close 연결 방식은, 많은 요청과 응답이 필요한 상황에서도 매번 연결을 맺고 끊는 과정이 이루어집니다.<br>
  이러한 동작은 처리 시간과 리소스를 낭비하며, 서버와 클라이언트 모두에게 과도한 부담을 초래합니다.

- ${cont_model} HTTP/1.1을 사용하고 있습니다. 따라서 별도의 설정을 바꾸지 않는 경우, 자동으로 Keep-Alive 방식으로 동작합니다.

- 아래 예제 코드를 참조하여, 반복 호출되는 API 들은 close 방식이 아닌 keep-alive 방식으로 구현하십시오.

<br>

##### 1-2. 예제 코드

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

[__SOURCE](1-release-note/README.md)
# 1. release note 

- COM 버전을 기준으로 API 변경사항에 대해서 정리를 해두었습니다.
- 본인이 사용 중인 제어기 버전보다 더 높은 버전에서 동작하는 API 를 사용하려면 버전업을 진행해야 합니다.
- 
	<div style="width: fit-content;">

	|COM 버전|배포 일정|링크|
	|:--:|:--:|:--:|
	|v70-00.00|2026.03|[🔗](70-00.md)|
	|v60-32.00|2025.11|[🔗](60-32.md)|
	|v60-30.00|2025.03|[🔗](60-30.md)|
	|v60-28.00|2024.08|[🔗](60-28.md)|

	</div>

[__SOURCE](1-release-note/70-00.md)
<link rel="stylesheet" href="../_assets/style.css">

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  Release Notes - v70.00-00
  <span style="
    background: #F44336; 
    color: #FFFFFF; 
    border: 2px solid #FFD700; 
    padding: 1px 5px; 
    border-radius: 8px; 
    font-weight: bold; 
    font-size: 14px; /* h2 크기에 맞춤 */
    text-transform: uppercase; 
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    display: inline-flex;
    align-items: center;
    height: 1.6em; /* h2 높이에 맞게 조정 */
  ">
    PREVIEW
  </span>
</h4>

<br>

<h4 style="
  background: linear-gradient(135deg, rgb(34, 160, 98), rgb(12, 85, 54)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  margin: 0; 
  font-size: 14px; 
  font-weight: bold; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  New Feature
</h4>

- joint_states<br>
  - 로봇의 현재 조인트 각도(°), 속도, 토크를 조회하는 API로, 전체 축 또는 지정한 축 구간만 선택적으로 조회할 수 있습니다.
- joint_traject_insert_point<br>
  - 실행 중인 조인트 궤적에 다음 목표 조인트 포인트를 순차적으로 추가하여, 로봇의 연속적인 조인트 이동을 구성할 수 있는 API입니다.




<div style="
  background: linear-gradient(135deg, rgb(58, 78, 160), rgb(38, 48, 90)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Improvement & Change
</div>

- none



<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Deprecated
</div>

- none



<div style="
  background: linear-gradient(135deg, rgb(255, 140, 0), rgb(160, 88, 7)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Updated API List
</div>


- \[<b style="color: #4CAF50">get</b>\] [joint_states](../5-robot/1-get/8-joint_states.md)
- \[<b style="color: #FF9800">post</b>\] [joint_traject_insert_point](../5-robot/2-post/9-joint_traject_insert_point.md)

[__SOURCE](1-release-note/60-32.md)
<link rel="stylesheet" href="../_assets/style.css">

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
Release Notes - v60.32-00
  <span style="
    background: #F44336; 
    color: #FFFFFF; 
    border: 2px solid #FFD700; 
    padding: 1px 5px; 
    border-radius: 8px; 
    font-weight: bold; 
    font-size: 14px; /* h2 크기에 맞춤 */
    text-transform: uppercase; 
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    display: inline-flex;
    align-items: center;
    height: 1.6em; /* h2 높이에 맞게 조정 */
  ">
    NEW
  </span>
</h4>

<br>

<h4 style="
  background: linear-gradient(135deg, rgb(34, 160, 98), rgb(12, 85, 54)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  margin: 0; 
  font-size: 14px; 
  font-weight: bold; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  New Feature
</h4>

- joint_traject_init<br>
  - 로봇 정지 상태에서 새로운 스텝에 대한 궤적을 요청할 때 **<u>필수적으로</u>** 진행해야하는 버퍼 인덱스 초기화 API 추가
- joint_traject_insert_points<br>
  - 외부로부터 복수의 궤적 포인트들을 수신하여 로봇의 모션에 반영하는 API 추가
- joint_traject_buf_avail<br>
  - 외부에서 궤적을 요청할 때, 현재 요청 가능한 상태의 버퍼 개수 조회 기능 API 추가



<div style="
  background: linear-gradient(135deg, rgb(58, 78, 160), rgb(38, 48, 90)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Improvement & Change
</div>

- set_cur_pc_idx<br>
  - 프로그램 재생 중 호출을 방지하는 유효성 검사 추가
- emergency_stop<br>
  - 호출 시 notice 팝업 출력
- emergency_stop_test<br>
  - 즉시정지(category 0) 요청 시 403 BAD Request 응답 버그 수정
  - 유효성 검사 별 에러코드 세분화
  - 호출 시 notice 팝업 출력
- execute_move<br>
  - 응답 관련 버그 수정 및 에러 코드 세분화
  - 원격모드에서만 동작하도록 유효성 검사 추가
- motor_on API<br>
  - 원격모드에서 프로그램 재생 중 수동 모드 전환 후 motor_on 시도 시 동작 안하는 버그 수정
  - 원격모드에서만 동작하도록 유효성 검사 추가
- start<br>
  - 원격모드에서 호출 안되는 버그 수정
  - 원격모드에서만 동작하도록 유효성 검사 추가
- stop<br>
  - 원격모드에서 호출 안되는 버그 수정
  - 호출 시 notice 팝업 출력
- reset<br>
  - 원격모드에서 정상 동작하지 않는 버그 수정
- 하기 시퀀스로 API 호출시 프로그램 중복 실행되는 버그 수정<br>
  - 모터온 -> R0 -> Delete Job -> Upload Job -> Reload Job -> Current PC 설정 -> 로봇 재생



<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Deprecated
</div>


- none



<div style="
  background: linear-gradient(135deg, rgb(255, 140, 0), rgb(160, 88, 7)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Updated API List
</div>


- [<b style="color: #4CAF50">get</b>\] [joint_traject_buf_avail](../5-robot/1-get/7-joint_traject_buf_avail.md)
- \[<b style="color: #FF9800">post</b>\] [joint_traject_init](../5-robot/2-post/7-joint_traject_init.md)
- \[<b style="color: #FF9800">post</b>\] [joint_traject_insert_points](../5-robot/2-post/8-joint_traject_insert_points.md)
- \[<b style="color: #FF9800">post</b>\] [set_cur_pc_idx](../9-task/2-post/6-set_cur_pc_idx.md)
- \[<b style="color: #FF9800">post</b>\] [emergency_stop_test](../5-robot/2-post/6-emergency_stop_test.md)
- \[<b style="color: #FF9800">post</b>\] [execute_move](../9-task/2-post/8-execute_move.md)
- \[<b style="color: #FF9800">post</b>\] [motor_on](../5-robot/2-post/1-motor-on.md)
- \[<b style="color: #FF9800">post</b>\] [start](../5-robot/2-post/2-start-stop.md)
- \[<b style="color: #FF9800">post</b>\] [stop](../5-robot/2-post/2-start-stop.md)
- \[<b style="color: #FF9800">post</b>\] [reset](../9-task/2-post/2-reset.md)

[__SOURCE](1-release-note/60-30.md)
<link rel="stylesheet" href="../_assets/style.css">

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  Release Notes - v60.30-00
</h4>

<br>

<h4 style="
  background: linear-gradient(135deg, rgb(34, 160, 98), rgb(12, 85, 54)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  margin: 0; 
  font-size: 14px; 
  font-weight: bold; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  New Feature
</h4>


- emergency_stop - 상태 확인 요청 API 추가, 비상정지 버튼과 동일한 기능의 API 추가




<div style="
  background: linear-gradient(135deg, rgb(58, 78, 160), rgb(38, 48, 90)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Improvement & Change
</div>


- emergency_stop_test - v60.28-00 의 emergency_stop 과 동일
- task reset - <span u>R 코드 0</span>를 활용하는 방식으로 변경됨



<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Deprecated
</div>


- <font style="color: #FE2E64">motor off</font> - HRSpace 환경을 고려한 API로, 실기 환경에서의 혼선을 방지하기 위해 Deprecated 처리. 비상정지 API 로 대체 됨  
- <font style="color: #FE2E64">task reset</font> - <span u>/project/context/tasks/reset</span>, <span u> /project/context/tasks[{task index}]/reset</span> path 는 더 이상 지원하지 않음.



<div style="
  background: linear-gradient(135deg, rgb(255, 140, 0), rgb(160, 88, 7)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Updated API List
</div>


- \[<b style="color: #4CAF50">get</b>\] [emergency_stop](../5-robot/1-get/6-emergency_stop.md)  
- \[<b style="color: #FF9800">post</b>\] [emergency_stop](../5-robot/2-post/5-emergency_stop.md)  
- \[<b style="color: #FF9800">post</b>\] [emergency_stop_test](../5-robot/2-post/6-emergency_stop_test.md)
- \[<b style="color: #FF9800">post</b>\] [task reset](../9-task/2-post/2-reset.md)
- ~~\[<b style="color: #FF9800">post</b>\] [motor_off](../5-robot/2-post/1-motor-on.md)~~  

[__SOURCE](1-release-note/60-28.md)
<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  Release Notes - v60.28-00 
</h4>  


<br>

<h4 style="
  background: linear-gradient(135deg, rgb(34, 160, 98), rgb(12, 85, 54)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  margin: 0; 
  font-size: 14px; 
  font-weight: bold; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  New Feature
</h4>


- emergency_stop - 비상정지 API 추가. step_no, stop_at 등의 값을 입력하여 특정 시점에 원하는 카테고리의 비상정지를 수행할 수 있도록 지원
- execute_move - 지정된 포즈로 이동하는 API가 추가
- execute_cmd - ${cont_model:upper} COM의 콘솔 명령어를 실행하는 API 추가  


<div style="
  background: linear-gradient(135deg, rgb(58, 78, 160), rgb(38, 48, 90)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Improvement & Change
</div>

- none


<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Deprecated
</div>


- none


<div style="
  background: linear-gradient(135deg, rgb(255, 140, 0), rgb(160, 88, 7)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white; 
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  Updated API List
</div>

- \[<b style="color: #FF9800">post</b>\] [emergency_stop](../5-robot/2-post/6-emergency_stop_test.md)  
- \[<b style="color: #FF9800">post</b>\] [execute_move](../9-task/2-post/8-execute_move.md)
- \[<b style="color: #FF9800">post</b>\] [execute_cmd](../10-console/2-post/1-execute_cmd.md)

[__SOURCE](2-version/README.md)
# 2. version

- 현재 api 의 버전 또는 로봇제어기의 시스템 버전을 확인합니다.

[__SOURCE](2-version/1-get/README.md)
## 2.1 version/get

- 현재 api 의 버전 또는 로봇제어기의 시스템 버전 관련 정보에 대하여 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.

[__SOURCE](2-version/1-get/1-api_ver.md)
#### 2.1.1 api_ver 

##### 설명

불가피하게 API 의 스키마 버전에 따라 제어기와 통신하는 방법이나 데이터 구조가 변경될 수 있습니다.  
이는 클라이언트 프로그램에 문제를 야기할 수 있으므로 해당 함수를 통해 확인하는 과정이 필요합니다.  
각 API 함수들에 대해 스키마 버전 변경이 생길 경우 설명 페이지에 별도의 표기를 통해 안내됩니다.


- `GET` : Open API 스키마 버전을 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /api_ver
```
##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - Open API 스키마 버전


##### 사용 예

```python
request url:
GET /api_ver

response:
(200, 5)
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests

def get_api_ver() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/api_ver"
    response = requests.get(url=base_url + path_parameter, timeout=5)
    return response

print(get_api_ver())
```
```sh
$python test.py
(200, 5)
```
</div>

[__SOURCE](2-version/1-get/2-sysver.md)
#### 2.1.2 sysver

##### 설명

- `GET` : 로봇제어기 시스템의 소프트웨어 버전을 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /versions/sysver
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - modules : 모듈 버전 정보의 배열
     - `name` : 모듈명(`com` : 로봇 제어기, `tp` : 티칭 펜던트)
      - `ver` : 버전번호
      - `build-date` : 빌드 날짜
      - `build-time` : 빌드 시간
      - `commit-id` : 소스코드의 커밋 ID

##### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /versions/sysver

response:
(200,{"modules" : [{"build-date": ..., "build-time": ..., "ver": ...}]})
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_sysver() -> dict:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/versions/sysver"
    response = requests.get(url=base_url + path_parameter)

    return response


print(get_sysver())

```
```sh
$python test.py
(200, {'modules': [{'build-date': 'Aug 13 2025', 'build-time': '12:50:21', 'commit-id': 'a11c02406c', 'name': 'com', 'sub-modules': [{'build-date': '', 'build-time': '', 'commit-id': '', 'name': 'fbr', 'ver': '2.1-1(1.1-3)'}], 'ver': '61.01-01.dev'}, {'build-date': 'Aug 13 2025
', 'build-time': '12:59:33', 'commit-id': 'fadf82cbb9', 'name': 'tp', 'ver': '61.01-01.dev'}]})
```
</div>

[__SOURCE](3-project/README.md)
# 3. project

- 조건설정, 프로젝트 정보, job 파일 정보들을 읽습니다.
- 업데이트된 job 파일들을 새로이 로드하거나 특정 job 파일들을 삭제할 수 있습니다.
[__SOURCE](3-project/1-get/README.md)
## 3.1 project/get

- 조건설정, 프로젝트 정보, job 파일 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](3-project/1-get/1-rgen.md)
#### 3.1.1 `rgen`

##### 설명

- `GET` : 제어기에 설정된 일반적인 정보들을 읽습니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/rgen
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	##### 2-1) 모드 정보
	<div style="width: fit-content;">

	|key|value|type|description|
	|:---|:---|:---|:---|
	|`cur_mode`| `0` : 수동 <br> `1` : 수동, 시스템 설정 <br>`3` : 자동, 1-cycle <br> `4` : 자동, 연속 (cycle 반복)|`int`|수동/자동 모드|
	|`enable_state`|`0번` 바이트(`LSB`) : 모터 ON (0: On / 1: Off / 2: Busy) <br> `1번` 바이트 : TP Enable (deadman) 스위치 (0: OFF / 1: ON)<br>`2번` 바이트 : 머신 Lock (0: OFF / 1: ON)<br>`3번` 바이트 : 건(gun) Lock (0: OFF / 1: ON)<br>`4번` 바이트 : 건(gun) (0: OFF / 1: ON)|`int`||
	|`is_playback`|`0` : 정지 중 <br>`1` : 재생 중|`int`||
	|`is_remote_mode`|`0`: False <br> `1`: True|`int`|원격(Remote) 모드 여부|
	|`is_ext_start`|`0`: False <br> `1`: True|`int`|외부 기동 여부|
	|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|외부 프로그램 선택 여부|

	</div>

	<br>


	##### 2-2) current 프로그램 카운터
	수동모드나 자동모드에서 티치펜던트 JOB 패널의 막대형 커서가 위치한 지점입니다. 현재 실행되고 있는 명령문, 혹은 편집의 대상 위치입니다.


	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`cur_prog_no`|`int`|current 프로그램 번호|
	|`cur_step_no`|`int`|current 스텝 번호|
	|`cur_func_no`|`int`|current 펑션 번호|

	</div>

	<br>

	##### 2-3) moving 프로그램 카운터

	재생 중 로봇이 이동하고 있는 목표 스텝입니다.

	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`mov_prog_no`|`int`|moving 프로그램 번호|
	|`mov_step_no`|`int`|moving 스텝 번호|
	|`mov_func_no`|`int`|moving 펑션 번호|

	</div>

	<br>

	##### 2-4) 속도


	<div style="width: fit-content;">

	|key|type|description|
	|:---|:---|:---|
	|`spd_lev`|`int`|수동모드 조그 속도 레벨 (1~8)|
	|`manual_spd_max`|`int`|수동모드 최대 속도 (mm/sec)|
	|`auto_spd`|`int`|자동모드 재생 속도 (%)|
	|`jog_inch_status`|`int`|조그 인칭 상태 (0:OFF/ 1:ON)|
	|`step_execute_unit_status`|`int`|StepFWD의 실행단위 (run to)<br>0: Cmd (명령문)<br>1: Step (스텝)<br>2: End (end문까지)|
	|`cont_path`|`int`|연속 모션 모드 (0~2)|

	</div>

<br>

##### 사용 예
Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_rgen() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
	 # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/rgen"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_rgen())
```
```sh
$python test.py
(200, {'_type': 'JObject', 'plc_mode': 4, 'safety_recovery_mode': 0, 'arcon_welder_0': 0, 'job_sub_state': 0, 'arcon_welder_1': -1, 'maintenance_status': 0, 'cur_mode': 0, 'cur_crd': 0, 'eid_last_err': 50033, 'eid_last_con_out': -1, 'is_manual_full_spd': 0, 'axis_ctrl': [1, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'reducer_status': 0, 'cur_mech_no': 0, 'in_position': [1, 0, 0, 0, 0, 0, 0, 0], 'posi_sync': 0, 'job_state': 0, 'shift_state': 0, 'enable_state': 256, 'apps_sync_seq': 0, 'task_no': 0, 'a
uto_spd': 100, 'battery_status': 0, 'cooper_ctrl': 16128, 'cur_scm_status': 0, 'base_intp': 0, 'eid_last_start_stop': -1, 'is_ext_prog_sel': 0, 'arc_welder_no': 0, 'is_remote_mode': 0, 'is_playback': 0, 'axis_lock': 0, 'mov_prog_no': 3344, 'call_pno': -1, 'spot_seq_no': [0, 0, 
0, 0], 'eid_last_history': 50761, 'arcon_cnd_no_-1': 1, 'task_enable': [1, 0, 0, 0, 0, 0, 0, 0], 'ucrd_no': 0, 'high_load': 0, 'cur_prog_no': 3344, 'arc_weld_appl': 1, 'rec_step_ex_sw': 0, 'job_state_msg': '', 'spot_gun_no': [0, 0, 0, 0], 'step_execute_unit_status': 0, 'direct_
teaching': 0, 'jog_inch_status': 0, 'gun_search_status': 0, 'eid_last_noti': 36154, 'tool_no': 0, 'next_exe_pno': -1, 'paint_gun_no': 0, 'n_forced_io': 0, 'load_esti': 1, 'chk_brake_release': [1, 1, 1, 1, 1, 1], 'eng_code': 0, 'spd_lev': 1, 'spot_cnd_no': [0, 0, 0, 0], 'mov_fun
c_no': 0, 'confirm_command_delete': 1, 'paint_block_state': 0, 'cont_path': 1, 'cur_mech_axis_info': 63, 'arcon_cnd_no_0': 1, 'spot_panel_thickness': 0.0, 'robot_model': 'HA006B-01', 'manual_spd_max': 250, 'cur_step_no': 1, 'cur_func_no': 0, 'is_ext_start': 0, 'opc_ua_server_st
ate': -1, 'n_prompt': 0, 'svgun_state': 0, 'mov_step_no': 1, 'step_goback_resume': 0, 'call_depth': 0, 'eid_last_warn': -1})
```
</div>

[__SOURCE](3-project/1-get/2-jobs_info.md)
#### 3.1.2 `jobs_info`

##### 설명

- `GET` : job 프로그램 관련 정보들을 받는 함수입니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/jobs_info
```
</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

   - [job 파일 관련 정보](../../99-schema/jobs_info.md)

##### 사용 예


<div style="width: fit-content;">

```python
request url:
GET /project/jobs_info

response-body:
{
	{
		"_type": "JObject",
		"fname": "0001.job",
		"job_comment": "",
		"n_step": 0,
		"n_aux_ax": 0,
		"n_total_ax": 6
	},
	{
		"_type": "JObject",
		"fname": "0002.job",
		"job_comment": "",
		"n_step": 9,
		"n_aux_ax": -1,
		"n_total_ax": -1
	},
	{
		"_type": "JObject",
		"fname": "0003.job",
		"job_comment": "",
		"n_step": 0,
		"n_aux_ax": -1,
		"n_total_ax": -1
   },
	      ...
}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_jobs_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/jobs_info"
    res = requests.get(url=base_url + path_parameter)

    return res


print(get_jobs_info())
```
```sh
$python test.py
(200, [
	{'_type': 'JObject', 'fname': '0055.job', 'n_step': 1, 'n_total_ax': 6, 'job_comment': '', 'n_aux_ax': 0},  
	{'_type': 'JObject', 'fname': '0001.job', 'n_step': 2, 'n_total_ax': -1, 'job_comment': '', 'n_aux_ax': -1}, 
	{'_type': 'JObject', 'fname': '9999.job', 'n_step': 1, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	{'_type': 'JObject', 'fname': '1111.job', 'n_step': 13, 'n_total_ax': -1, 'job_comment': '', 'n_aux_ax': -1}, 
	{'_type': 'JObject', 'fname': '0005.job', 'n_step': 0, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	{'_type': 'JObject', 'fname': '0021.job', 'n_step': 3, 'n_total_ax': 12, 'job_comment': '', 'n_aux_ax': 6}, 
	...
])
```
</div>

[__SOURCE](3-project/2-post/README.md)
## 3.2 project/post

- 조건설정, 프로젝트 정보, job 파일 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.

[__SOURCE](3-project/2-post/1-reload_updated_jobs.md)
#### 3.2.1 `reload_updated_jobs`

##### 설명

- `POST` : 작업 파일들을 갱신하는 요청을 보냅니다.
- FTP 로 job 파일을 제어기에 전송하는 경우, 해당 API 를 통해 reload 요청을 해야 전송된 job 파일이 메모리에 반영이 됩니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/reload_updated_jobs
```

##### request-body

```json
{}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	```json
	{'_type': 'JObject'}
	```


##### 사용 예

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_reload_updated_jobs() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/reload_updated_jobs"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_reload_updated_jobs())
```
```sh
$python test.py
(200, {'_type': 'JObject'})        
```
</div>

[__SOURCE](3-project/2-post/2-jobs-delete_job.md)
#### 3.2.2 `delete_job`

##### 설명

- `POST` : 작업 파일을 제거하는 요청을 보냅니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/jobs/delete_job
```

##### request-body

```json
{
  "fname": "0001.job"
}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   ```json
	{}
	```

##### 사용 예

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
	"fname": "0001.job"
}
```

</div>

Python Script 예시


<div style="width: fit-content;">

```python
#test.py
import requests


def post_delete_job(file_name: str = "0001.job") -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/jobs/delete_job"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"fname": file_name}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_delete_job())
```
```sh
$python test.py
(200, {})
```
</div>

[__SOURCE](4-control/README.md)
# 4. control

- 제어기(controller)의 설정값 적용 및 입출력 값을 처리합니다.
- 시스템 입출력, 디지털 입출력, 조건설정, 사용자 좌표계 관련 정보를 다룹니다.

<br>
[__SOURCE](4-control/1-get/README.md)
## 4.1 control/get

- 제어기의 설정 정보, 입출력 값에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](4-control/1-get/1-op_cnd.md)
#### 4.1.1 `op_cnd`

##### 설명

- `GET` : 조건설정 값을 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/control/op_cnd
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [조건설정 파라미터](../../99-schema/op_cnd.md)

		```json
		{
			"_type": "CondGrp",
			"step_goback_max_spd": 200,
			"playback_mode": 1,
			"step_go_func_ex": 1,
			"robot_lock": 0,
			"playback_spd_rate": 100,
			"intp_base": 0,
			"ucrd_num": 0,
			"path_recov_confirm": 2,
			"func_reexe_on_trace": 1,
			"plc_mode": 1
		}
		```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_operation_condition() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888" # hrspace
    path_parameter = "/project/control/op_cnd"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_operation_condition())
```
```sh
$python test.py
(200, {'plc_mode': 1, 'step_go_func_ex': 1, '_type': 'CondGrp', 'intp_base': 0, 'playback_spd_rate': 100, 'step_goback_max_spd': 250, 'robot_lock': 0, 'func_reexe_on_trace': 1, 'ucrd_num': 0, 'playback_mode': 1, 'path_recov_confirm': 2})
```
</div>

[__SOURCE](4-control/1-get/2-ucss-ucs_nos.md)
#### 4.1.2 `ucss/ucs_nos`

##### 설명

- `GET` : 현재 사용 중인 사용자 좌표계들을 리스트로 얻습니다.
- `[F2: 시스템] - 2: 제어 파라미터 - 6: 좌표계 등록` 을 통해 등록한 사용자 좌표계 리스트를 출력합니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ucss/ucs_nos
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 현재 사용중인 사용자 좌표계(list)  
  	  ex) [1]


##### 사용 예

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
[1]
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_ucs_nos() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ucss/ucs_nos"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_ucs_nos())
```
```sh
$python test.py
(200, [1])
```
</div>

[__SOURCE](4-control/2-post/README.md)
## 4.2 control/post

- 제어기의 설정 정보, 입출력 값에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](4-control/3-put/README.md)
## 4.3 control/put

- 제어기의 설정 정보, 입출력 값에 대한 PUT 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](4-control/3-put/1-op_cnd.md)
#### 4.3.1 `op_cnd`

##### 설명

- `PUT` : 로봇의 `조건설정값`을 변경합니다.
- TP 에서 조건 설정 창을 열고 해당 메서드를 요청한 경우, 창을 닫았다 다시 열어야 값이 반영됩니다.

##### path-parameter

<div style="width: fit-content;">

```python
PUT /project/control/op_cnd
```

##### request-body

- [조건설정 파라미터](../../99-schema/op_cnd.md)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - {'_text': ''}

##### 사용 예

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}

response-body:
{'_text': ''}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def put_op_cnd() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/op_cnd"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "playback_mode": 2,
        "step_goback_max_spd": 130,
        "step_go_func_ex": 0,
        "func_reexe_on_trace": 1,
        "path_recov_confirm": 0,
        "playback_spd_rate": 80,
        "robot_lock": 0,
        "intp_base": 0,
        "ucrd_num": 0,
        "plc_mode": 0,
    }

    response = requests.put(url=base_url + path_parameter, headers=head, json=body)
    return response


print(put_op_cnd())
```
```sh
$python test.py
(200, {'_text': ''})
```
</div>

[__SOURCE](5-robot/README.md)
# 5. robot

- 로봇과 툴 데이터에 대한 원격 제어와 모니터링을 확인할 수 있습니다.
- 모터 on/off, 로봇 자세, 툴, 조그 좌표계 등을 다루고 있습니다.

[__SOURCE](5-robot/1-get/README.md)
## 5.1 robot/get

- 로봇과 툴 데이터에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](5-robot/1-get/1-motor_on_state.md)
#### 5.1.1 `motor_on_state`

##### 설명

- `GET` : 모터 온 상태를 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/motor_on_state
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val :
     - `0` : on
     - `1` : off
     - `2` : busy (상태 전환 중)

##### 사용 예
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
    "_type" : "JObject",
    "val" : 1
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_motor_on_state() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/motor_on_state"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_motor_on_state())

```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': 1})
```

</div>

[__SOURCE](5-robot/1-get/2-po_cur.md)
#### 5.1.2 `po_cur`

##### 설명

- `GET` : 현재 로봇이 취하고 있는 pose(자세)를 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/po_cur
```

##### query-parameter

- `task_no` : task 번호 (0~7).
  - 미지정 : task 0으로 적용됨.
  - &gt;=0 : mechinfo 미지정 시, task의 현재 mechinfo가 적용됨.
- `crd` :  
  - 미지정 : tcp, axis, encoder를 모두 얻음.
  - <0 : 현재 기록 좌표계를 따름.
  - &gt;=0 : [좌표계](../../99-schema/crdsys.md)
- `ucrd_no` : 사용자 좌표계 번호 (crd가 user일 때만 지정함.)
- `mechinfo` : [메커니즘 정보](../../99-schema/mechinfo.md)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [포즈 정보](../../99-schema/pose.md)


##### 사용 예

로봇 6축(j1~j6) + 주행 1축(j7) + 포지셔너 2축(j8, j9)인 시스템의 사례.

- 로봇의 base 좌표만 얻기

```python
request url:
GET /project/robot/po_cur?crd=0&mechinfo=1

response-body:
{
    "nsync" : 0,
    "_type" : "Pose",
    "rx" : 0.000000,
    "x" : 1782.000000,
    "ry" : 90.000000,
    "y" : 0.000000,
    "rz" : 0.000000,
    "z" : 1938.000000,
    "mechinfo" : 1,
    "crd" : "base"
}
```

- 전 축의 축좌표 얻기

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=-1

response-body:
{
    "nsync" : 0,
    "_type" : "Pose",
    "mechinfo" : 65535,
    "j9" : 0.000000,
    "crd" : "joint",
    "j1" : 0.000000,
    "j2" : 90.000000,
    "j3" : 0.000000,
    "j4" : 0.000000,
    "j5" : 0.000000,
    "j6" : 0.000000,
    "j7" : 0.000000,
    "j8" : 0.000000
}
```

- 포지셔너 2축 (즉, 메커니즘 M2)의 축좌표 얻기

```python
request url:
GET /project/robot/po_cur?crd=2&mechinfo=2

response-body:
{
    "nsync": 0,
    "_type": "Pose",
    "rx": 0.000000,
    "x": 0.000000,
    "ry": 0.000000,
    "y": 0.000000,
    "rz": 0.000000,
    "z": 0.000000,
    "mechinfo": 2,
    "crd": "joint",
    "j1": -0.690000,
    "j2": 84.448000,
    "j3": 22.304000,
    "j4": 0.000000,
    "j5": 0.000000,
    "j6": 0.000000
}
```
</div>


<div style="width: fit-content;">

Python Script 예시

```python
# test.py
import requests


def get_po_cur() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/po_cur"
    query_parameter = {"crd": 2, "mechinfo": 1}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_po_cur())
```
```sh
$python test.py
(200, {'_type': 'Pose', 'nsync': 0, 'crd': 'joint', 'mechinfo': 1, 'j2': 90.106, 'j3': 0.0, 'j1': 0.0, 'j6': 0.0, 'j4': 0.0, 'j5': -90.0})
```

</div>

[__SOURCE](5-robot/1-get/3-cur_tool_data.md)
#### 5.1.3 `cur_tool_data`

##### 설명

- `GET` : 로봇의 현재 툴 데이터 얻기.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/cur_tool_data
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val : [툴 데이터](../../99-schema/tool_data.md)

##### 사용 예

```python
request url:
GET /project/robot/cur_tool_data

response-body:
{
    "_type": "Tool",
    "x": 0.000000,
    "rx": 0.000000,
    "y": 0.000000,
    "ry": 0.000000,
    "z": 0.000000,
    "rz": 0.000000,
    "cy": 0.000000,
    "mass": 20.000000,
    "cx": 100.000000,
    "cz": 65.000000,
    "ixx": 0.059000,
    "iyy": 0.061000,
    "izz": 0.075000,
    "mass_esti": 20.000000,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_cur_tool_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/cur_tool_data"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_cur_tool_data())
```
```sh
$python test.py
(200, {'_type': 'Tool', 'mass': 6.0, 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'y': 0.0, 'izz': 0.013, 'z': 0.0, 'iyy': 0.024, '
ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0})
```

</div>

[__SOURCE](5-robot/1-get/4-tools.md)
#### 5.1.4 `tools`

##### 설명

- `GET` : 로봇의 모든 툴 정보 얻기. T0~T31까지의 툴 중 존재하는 툴만 얻습니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/robot/tools
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - t_0 : [툴 데이터](../../99-schema/tool_data.md)
   - t_1 : 툴 데이터
   - t_2 : 툴 데이터  
   ...
   - t_31 : 툴 데이터

##### 사용 예

```python
request url:
GET /project/robot/tools

response-body:
{
    "_type" : "Tools",
    "t_0" : { ... },
    "t_1" : { ... },
	 ...
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def get_tools_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/tools"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_tools_data())
```
```sh
$python test.py
(200, {'_type': 'Tools', 't_1': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0,
 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_0': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.
0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_31': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias
_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}, 't_15': {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.
0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, 'ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0}})
```

</div>

[__SOURCE](5-robot/1-get/5-tools_t.md)
#### 5.1.5 `tools/t_{number}`

##### 설명

- `GET` : 특정 툴의 설정값 정보를 받는 함수입니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/robot/tools/t_{number}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [툴 데이터](../../99-schema/tool_data.md)

##### 사용 예

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "_type" : "Tool",
    "x"     : 0.0,
    "y"     : 0.0,
    "z"     : 0.0,
    "rx"    : 0.0,
    "ry"    : 0.0,
    "rz"    : 0.0,
        ...
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_tool1_data() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/tools/t_1"

    response = requests.get(url=base_url + path_parameter)

    return response


print(get_tool1_data())
```
```sh
$python test.py
(200, {'mass': 6.0, '_type': 'Tool', 'rz': 0.0, 'rx': 0.0, 'ry': 0.0, 'mass_esti': 6.0, 'bias_4': 0.0, 'bias_5': 0.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_0': 0.0, 'bias_1': 0.0, 'x': 0.0, 'izz': 0.013, 'y': 0.0, 'z': 0.0, 'iyy': 0.024, '
ixx': 0.016, 'cz': 70.0, 'cy': 0.0, 'cx': 100.0})
```

</div>

[__SOURCE](5-robot/1-get/6-emergency_stop.md)
#### 5.1.6 `emergency_stop`

##### 설명

- `GET` : 비상정지 버튼이 눌려져있는 상태에 대해서 정보를 얻습니다.
-  API 로 비상정지를 요청하는 경우에 대해서는 API 가 들어오는 시점에 1이 반환됩니다.  

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/emergency_stop
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject", "val": 0}
	```
	</div>

	- 0: released 상태
   - 1: pressed 상태

##### 사용 예

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "val": 0,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_emergency_stop() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}

	 response = requests.get(url=base_url + path_parameter, headers=head)
	 return response

print(f"{get_emergency_stop()}")
```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': 0})
```
</div>

[__SOURCE](5-robot/1-get/7-joint_traject_buf_avail.md)
#### 5.1.7 `joint_traject_buf_avail`

##### 설명
- 지원 버전 : `60.32-00` &uparrow;
- `GET` : 현재 궤적을 저장하는 버퍼의 사용가능한 크기를 반환합니다.
- 궤적을 연속해서 요청을 하는 경우, 해당 함수를 활용해 남은 저장 공간의 크기 이내의 크기의 궤적을 요청해야합니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - val: 현재 사용 가능한 버퍼의 수 (최대 2048개)

		<div style="width: fit-content;">

		```json
		{"val": 2048}
		```
		</div>


##### 사용 예

```python
request url:
GET /project/robot/trajectory/joint_traject_buf_avail

response-body:
{
    "val": 2048,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_jt_buff_avail_num(base_url: str, session: requests.Session):
    uri = f"{base_url}/project/robot/trajectory/joint_traject_buf_avail"
    try:
        ret = session.get(url=uri)
        ret.raise_for_status()
        return ret.json()
    except Exception as e:
        print(f"[ERROR] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        ret = get_jt_buff_avail_num(base_url, session)
        print(ret)
```
```sh
$python test.py
(200, {'val': 2048})
```
</div>

[__SOURCE](5-robot/1-get/8-joint_states.md)
#### 5.1.8 `joint_states`

##### 설명
- 지원 버전 : `70.00-00` ↑
- `GET` : 로봇의 현재 조인트 상태를 조회합니다.
- 각 조인트의 **각도(position, °), 속도(velocity), 토크(effort)** 정보를 반환하며, 전체 축 또는 지정한 축 구간만 선택적으로 조회할 수 있습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

##### query-parameter

* * 파라미터를 지정하지 않으면 전체 조인트를 조회합니다.
* jno_start (optional)
  * 조회를 시작할 조인트 번호 (1-base)
* jno_n (optional)
  * 조회할 조인트 개수


##### response

1. status code

   * 200 : OK
   * 400 : Bad Request
     * query parameter 가 유효성 검사에서 실패한 경우
   * 403 : Forbidden
   * 404 : Not Found

2. response-body

   * position : 조인트 각도 배열 (deg)
   * velocity : 조인트 속도 배열
   * effort : 조인트 토크 배열 (Nm)

		<div style="width: fit-content;">

		```json
		{
			"position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
			"velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
			"effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
		}
		```

        </div>

##### 사용 예

<div style="max-width: 60vw;">

```python
request url:
GET /project/robot/joint_states?jno_start=1&jno_n=6

response-body:
{
    "position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
    "velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
}
```

Python Script 예시

```python
# test.py
import requests

def get_joint_states() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path = "/project/robot/joints/joint_states"
    query = {"jno_start": 1, "jno_n": 6}

    res = requests.get(url=base_url + path, params=query)

    print(res.json())

    return res


get_joint_states()


```

```sh
$python test.py
{'_type': 'JObject', 'position': [0.949533, 90.949655, 0.949155, 0.948415, -89.050195, 0.948001], 'effort': [0.0, 93.988759, 93.925036, 0.179785, -5.312434, 0.102171], 'velocity': [-0.0, -0.0
, 0.0, 0.0, -0.0, 0.0]}
```

</div>

[__SOURCE](5-robot/2-post/README.md)
## 5.2 robot/post

- 로봇과 툴 데이터에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](5-robot/2-post/1-motor-on.md)
#### 5.2.1 `motor_on`

- <b style="color:orange"> `motor_off` API 는 [v60.30-00](../../1-release-note/60-30.md)부터 지원되지 않습니다.</b>

<div style="width: fit-content;">

##### 설명

- `POST` : 모터 ON을 수행합니다.

##### path-parameter


```python
POST /project/robot/motor_on
```

##### request-body

```json
{}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 원격모드가 아닌 상태에서 요청한 경우(v60.30-09 부터 적용)
   - 404 : Not Found

2) response-body
	```json
	{ "_type": "JObject"}
	```

3) error code
   - -38500: 원격 모드가 아닌 상태로 해당 api 요청

##### 사용 예

```python
POST /project/robot/motor_on

request-body:
{}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
import requests


def post_motor_on() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/motor_on"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_motor_on())

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```

</div>

[__SOURCE](5-robot/2-post/2-start-stop.md)
#### 5.2.2 `start / stop`

##### 설명

- `POST` : 로봇 기동(start)과 로봇 정지(stop)를 수행합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /project/robot/start
POST /project/robot/stop
```

##### request-body

```json
{}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - start 요청 시 원격모드가 아닌 상태에서 요청한 경우(v60.30-07 부터 적용)
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{ "_type": "JObject"}
	```
	</div>


1) error code
   - -38500: 원격 모드가 아닌 상태로 해당 api 요청

##### 사용 예

```python
POST /project/robot/start or /project/robot/stop

request-body:
{}

response-body:
{}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests


def post_start() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/start"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response

def post_stop() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_start())
print(post_stop())
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](5-robot/2-post/3-tool_no.md)
#### 5.2.3 `tool_no`

##### 설명

- `POST` : 현재 툴 번호를 설정합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /project/robot/tool_no
``` 

##### request-body

- `val` : 툴 번호
  - `로봇 툴` : `0` ~ `31`
  - `정치 툴` : `0` ~ `3`

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	```json
	{ "_type": "JObject"}
	```

##### 사용 예

```json
POST /project/robot/tool_no

request-body
{
	"val": 1
}
```

</div>

Python Script 예시



```python
import requests


def set_tool_no(tool_no: int = 0) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace

    url = f"{base_url}/project/robot/tool_no"
    body = {"val": tool_no}

    response = requests.post(url, json=body)
    return response


print(set_tool_no(tool_no=1))

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](5-robot/2-post/4-crd_sys.md)
#### 5.2.4 `crd_sys`

##### 설명

- `POST` : 현재 조그(jog) 좌표계를 설정합니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/crd_sys
```

##### request-body

- [좌표계](../../99-schema/crdsys.md)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{
		"_type": "JObject",
		"cur_crd": 1,
		"ucrd_no": 1
	}
	```
	</div>

##### 사용 예

```json
POST /project/robot/crd_sys

request-body
{
	"val": 1
}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
import requests


def post_crd_sys(x: int = 0) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/crd_sys"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"val": x}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_crd_sys(1))
```
```sh
$python test.py
(200, {'_type': 'JObject', 'cur_crd': 1, 'ucrd_no': 0})
```

</div>

[__SOURCE](5-robot/2-post/5-emergency_stop.md)
#### 5.2.5 `emergency_stop`

##### 설명

- 지원 버전 : `60.30-00` &uparrow;
- `POST` : 비상 정지를 실행합니다.  
- 비상정지 버튼을 눌렀을 때와 동일한 감속 프로파일이 적용됩니다.
- API 호출 시, 네트워크 지연(Latency) 또는 요청 처리 시간 때문에 물리적 버튼보다 늦게 반응할 가능성이 있습니다.


##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/emergency_stop
```

##### request-body
```python 
{}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
   - 404 : Not Found
2) response-body
	- v60.30 이하
		<div style="width: fit-content;">

		```json
		{"err_code": 200}
		```
		</div>
	- v60.32 이상
		<div style="width: fit-content;">

		```json
		{"_type": "JObject"}
		```
		</div>

##### 사용 예

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_emergency_stop())

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](5-robot/2-post/6-emergency_stop_test.md)
#### 5.2.6 `emergency_stop_test`

- <b style="color:orange"> 해당 API 는 `60.28-00` 까지 `emergency_stop` API 로 사용되었습니다. </b>  

##### 설명

- 지원 버전 : `60.30-00` &uparrow;
- `POST` : 비상 정지 테스트 요청을 보냅니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/emergency_stop_test
```
</div>

##### request-body

<div style="width: fit-content;">

-  |key|type|contents|validation|
	|---:|:---:|---|---|
	|`step_no`| int | 비상정지 타겟 스텝 번호, 현재 진행 중인 job 의 총 step 번호 이내| 1 ~ 999 |
	|`stop_at`| double | 지정위치의 몇 % 에서 멈출지 설정| 1 ~ 100 |
	|`stop_at_corner`| int | 0: 일반정지, 1: 코너정지| 0 or 1 |
	|`category`| int | 0: 즉시정지, 1: 감속정지, 2: 일시정지| 0 or 1 or 2 |

</div>

- `0: 즉시정지`  
  &rightarrow; 로봇 재생 중에 제어기가 꺼져버리는 경우와 동일한 경우. 정지 후 모터 오프가 됨  

    {% hint style="warning" %}
    사양변경

    - V60.29-08 ~ V60.30-10: 타겟 스텝에서만 즉시 정지 API 호출 가능
    - V60.32-00 이상: 해당 사양 삭제

    {% endhint %}

- `1: 감속정지`  
	&rightarrow;  비상정지 버튼을 눌렀을 동작하는 경우. 정지 후 모터 오프가 됨  
- `2: 일시정지`  
	&rightarrow;  로봇 모션을 잠시 정지하는 경우. 정지 후 모터 오프가 되지 않음

##### response 

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - v60.32-00 미만
       - 400 반환
     - v60.32-00 이상 (에러 세분화)
       - -38502: step number 유효성 검사 실패
       - -38503: stop at 유효성 검사 실패
       - -38504: stop at corner 유효성 검사 실패
       - -38505: category 유효성 검사 실패
       - -38506: request-body key 유효성 검사 실패
   - 404 : Not Found

2) response-body
	- v60.30 이하
		<div style="width: fit-content;">

		```json
		{"err_code": 200}
		```
		</div>
	- v60.32-00 이상
		<span>
		<div style="width: fit-content;">

		```json
		{"_type": "JObject"}
		```
		</div>
		<div style="width: fit-content;">

		```json
		{"err_code": "-38502"}
		```
		</div>
		</span>


##### 사용 예

<div style="width: fit-content;">

```emergency_stop
POST /project/robot/emergency_stop

request-body
{
  "step_no": 1,
  "stop_at": 50,
  "stop_at_corner": 0,
  "category": 1,
}
```

Python Script 예시

```python
import requests


def post_emergency_stop_test() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/robot/emergency_stop_test"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body_0 = {
        "step_no": 1,
        "stop_at": 1,
        "stop_at_corner": 0,
        "category": 1,
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body_0)

    return response


ret = post_emergency_stop_test()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](5-robot/2-post/7-joint_traject_init.md)
#### 5.2.7 `joint_traject_init`

##### 설명

- 지원 버전 : `60.32-00` &uparrow;
- `POST` : 버퍼를 초기화를 진행합니다.
- 로봇이 정지 상태에서 궤적을 요청할 때, 직전에 저장된 궤적을 지워줍니다.
- 다음과 같은 상황에서도 버퍼 초기화를 진행해주어야 합니다.
  - traj1 요청 &rightarrow; 로봇 이동 중 에러 발생 후 정지 &rightarrow; **버퍼 초기화** &rightarrow; traj2 요청
  - 에러가 발생한 시점의 궤적이 버퍼에 저장되어있어 버퍼 초기화 없이 traj2 요청을 하면 에러가 발생할 수 있습니다.
- [joint_traject_insert_points](./8-joint_traject_insert_points.md) api 로 궤적을 이동중에 <u>해당 함수를 호출하면 그 즉시 버퍼가 갱신</u>이 됩니다.
  - 기존 버퍼에 저장된 궤적 포인트들이 사라지면 로봇이 정지되면서 에러가 발생할 수 있으므로 사용에 주의 하시기 바랍니다.


##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

##### request-body

<div style="width: fit-content;">

- {}

</div>



##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
     - `err_code` (<0) : 초기화 실패
   - 404 : Not Found

2) response body

	<div style="width: fit-content;">

	```json
	{ "_type": "JObject"}
	```
	</div>

##### 사용 예

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}

response-body
{'_type': 'JObject'}
```

Python Script 예시
```python
# test.py
from typing import Union
import requests


def post_init_trajectories(
    base_url: str, session: requests.Session
) -> Union[requests.Response, None]:
    uri = f"{base_url}/project/robot/trajectory/joint_traject_init"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = session.post(url=uri, headers=headers)
        response.raise_for_status()
        print(f"[INFO] Initialization successful: status={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to initialize trajectory buffer: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace

    with requests.Session() as session:
        response = post_init_trajectories(base_url, session)
        print(response)


if __name__ == "__main__":
    main()

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](5-robot/2-post/8-joint_traject_insert_points.md)
#### 5.2.8 `joint_traject_insert_points`

##### 설명

- 지원 버전 : `60.32-00` &uparrow;
- `POST` : 복수 개의 joint trajectory 포인트를 제어기 내부 버퍼에 저장하여 모션에 반영합니다.

---

##### 주의 사항

1. **프로그램이 <u>실행 중인</u> 상태**에서만 본 API가 동작합니다.
   - ex) job 프로그램에 "wait di1" 와 같은 구문을 자동모드에서 실행한 상태로 api 요청
   - 해당 조건을 만족하지 않고 요청하는 경우, [외부지령 동작 불능상태 (E01554)](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) 에러가 발생합니다.

2. 한 번에 POST 가능한 궤적의 최대 포인트 수는 <u>**2048개**</u>입니다.
   - 궤적의 포인트를 저장하는 <u>**버퍼의 최대 크기가 2048**</u>입니다.

3. 요청된 궤적의 포인트들은 모션에 반영되기 전까지 사라지지 않으며 해당 위치로 도달할 때까지 로봇이 움직입니다.
   - [joint_traject_init](./7-joint_traject_init.md) api 로 버퍼를 강제로 초기화하지 않는 이상 모션 수행 전까지 버퍼의 궤적은 유지됩니다.

4. 궤적에 따라 [축속도 제한값 초과 (E159)](https://hr-alarms.web.app/#/${cont_model}/ko/E159) 에러가 발생할 수 있으며, 해당 에러가 발생하면 로봇은 정지합니다.

5. 해당 API 는 <u>**2개 이상**</u>의 포인트들로 구성된 궤적에 대해서 처리합니다.

6. 부가축 사용 시, 축 좌표 값의 단위에 유의하시기 바랍니다.
---

##### path-parameter

<div style="width: fit-content;">

```joint_traject_insert_points
POST /project/robot/trajectory/joint_traject_insert_points
```
</div>

##### request-body

<div style="width: fit-content;">

- 	|               키 값 |       타입      | 설명                          | 비고                                           |
	| ----------------: | :-----------: | --------------------------- | -------------------------------------------- |
	|     `joint_names` | array(string) | 궤적 대상 joint 이름 리스트          | ex) 6축, `"j1"` \~ `"j6"` 형식, **순서까지 정확히 기입** |
	|          `points` |     object({})    | 실행될 trajectory 포인트 목록       | key: `"point_n"`, n은 1부터 시작, **2개 이상 필수**    |
	|       `positions` | array(double) | 각 joint의 목표 위치<br>(radian, **<u>부가축은 축좌표 단위 고려</u>**) | 현재 축 수만큼 위치를 선정하여 요청해야 함 |
	| `time_from_start` |     number    | 해당 포인트의 시작 시간 (초 단위)        | `0.0 이상`, **이전 포인트보다 커야 함**          |

</div>

- ```
	{
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [0, 1.570796, 0.0, 0.0, 0.0, 0.0],
					"time_from_start": 0.0
			},
			"point_2": {
					"positions": [0.049999, 1.570796, 0.0, 0.0, 0.0, 0.0],
					"time_from_start": 0.4
			}
		}
	}

  ```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
     - `err_code` (<0) : 초기화 실패
   - 404 : Not Found

2) response body

	<div style="width: fit-content;">

	```json
	{ "_type": "JObject"}
	```
	</div>

##### error code (response 403)

<div style="width: fit-content;">

- 	| 에러코드     | 에러 상수명                   | 설명                                             |
	| ---------- | --------------------------- | ----------------------------------------------------- |
	| `-2`       | `ERR_MISSING_JOINT_NAMES`   | joint\_names 필드가 누락된 경우 |
	| `-3`       | `ERR_INVALID_JOINT_NAMES`   | joint\_name 형식이 잘못되거나("x1"), 요청한 축들의 수가 현재 로봇 축수와 일치하지 않거나, joint 이름 표기 순서 오류(["j1", "j3", "j2", ... ,"j6"]) |
	| `-4`       | `ERR_MISSING_POINTS`        | points 필드가 누락된 경우                                       |
	| `-5`       | `ERR_INVALID_POINTS`        | points 값이 객체(= python의 dict)가 아닌 경우 (예: 정수나 문자열 등) |
	| `-6`       | `ERR_TOO_FEW_POINTS`        | 궤적의 포인트 개수가 2개 미만인 경우                                |
	| `-7`       | `ERR_TOO_MANY_POINTS`       | 허용 가능한 포인트 개수 2048개를 초과하여 궤적을 요청한 경우            |
	| `-8`       | `ERR_POINTS_EXCEED_BUFFER`  | 현재 비어있는 버퍼공간보다 많은 포인트로 이루어진 궤적을 요청한 경우          |
	| `-9`      | `ERR_INVALID_POINT_OBJECT`  | point\_n 값이 객체(= python의 dict)가 아닌 경우 (예: 정수나 문자열 등)  |
	| `-10`      | `ERR_MISSING_POSITIONS`     | positions 필드가 누락된 경우                     |
	| `-11`      | `ERR_INVALID_POSITIONS`     | positions 가 배열이 아니거나, position 값이 number가 아니거나, 길이가 축 수와 일치하지 않거나 |
	| `-12`      | `ERR_MISSING_TIME`          | time\_from\_start가 누락된 경우         |
	| `-13`      | `ERR_INVALID_TIME`          | time\_from\_start가 number가 아니거나, time\_from\_start가 0보다 작거나, 움직이는 상태에서 이전 값보다 작은 값을 요청한 경우 |

</div>

##### 사용 예

**예시1. 정지 상태에서 궤적 요청하기**

<img src="../../_assets/09_online_trajectory_insert_points_single.png" style="max-height: 280px;">

1) 정지 후 궤적을 요청을 할 때는 [joint_traject_init](./7-joint_traject_init.md) api를 활용하여 기존 궤적이 저장된 버퍼를 초기화합니다.
2) 궤적을 요청하기 전, 프로그램이 실행 중인지 확인하고 남아있는 버퍼의 수를 확인합니다.
3) 최소 **2개의 포인트**로 이루어진 궤적을 요청합니다.
   - 시작 포인트(point_1)의 `position` 은 **현재 로봇의 위치**로 설정합니다.
   - 시작 포인트(point_1)의 `time_from_start` 는 **0.0**으로 설정합니다.
   - 이후 포인트들은 직전 포인트에서 이동가능한 position 과 time_from_start 를 설정하여 post 합니다.
4) 에러가 발생하여 멈춘 경우, 재시작 시 joint_traject_init 으로 초기화를 진행 후 1-3의 과정을 진행합니다.

<br>

**예시2. 불연속 모션으로 궤적 요청하기 (궤적과 궤적 사이 정지 시간이 존재)**

<img src="../../_assets/10_online_trajectory_insert_points_two.png" style="max-height: 240px;">

1) 예시1 의 조건들에 맞춰 traj1 과 traj2 를 요청해야합니다.
2) 하기 사항에 유의하십시오.
   - traj2 의 P1 의 positions == traj1 의 Pn 의 positions
   - traj2 의 P1 의 time_from_start 는 0.0 이어야합니다.

<br>

**예시3. 연속 모션으로 궤적 요청하기**

<img src="../../_assets/11_online_trajectory_insert_points_continuous.png" style="max-height: 350px;">

1) 예시1 의 조건들에 맞춰서 traj1 을 요청합니다.
2) Pn-1 의 위치로 로봇이 이동 중일 때 하기 사항에 유의하여 traj2 를 요청해야합니다.
   - traj1 의 Pn 과 traj2 의 P1 은 로봇이 자연스럽게 연속해서 이동가능하도록 설정해야합니다.
     - traj2 의 P1 의 time_from_start 는 traj1 의 마지막 포인트 Pn 의 Δ(>0) 만큼 누적 증가된 값이어야 합니다.
     - traj2 의 P1 의 position 는 traj1 의 Pn 에서 Δ 동안 이동 가능한 위치여야 합니다.
   - 자연스럽게 이어지지 않는 궤적을 연속해서 요청하는 경우, [축속도 제한값 초과 (E159)](https://hr-alarms.web.app/#/${cont_model}/ko/E159) 에러가 발생할 수 있습니다.

<div style="width: fit-content;">

<br>

##### Python Script 예시

- 로봇 기준자세(6축 기준, [0,90,0,0,0,0] 로 이동)
- 아래 0001.job 을 생성하여 자동모드에서 실행하여 프로그램 재생 상태로 진입합니다.
- 0001.job
	```job
	Hyundai Robot Job File; { version: 1.6, mech_type: "-1()", total_axis: -1, aux_axis: -1 }
	  > wait di1
		end
	```
- 테스트 스크립트 실행 (예시3. 두 개의 궤적을 연속 모션으로 요청하기)

	```
	조건1. traj_2 의 point_1 의 time_from_start 는 traj_1 의 point_2 에서 Δ(>0) 만큼 누적 증가된 값
	조건2. traj_2 의 point_1 의 positions 는 traj_1 의 point_2 에서 Δ 동안 이동 가능한 위치
	```

	```python
	import requests
	import time
	import math

	session = requests.Session()


	traj_1 = {
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [
						0,
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 0.0,
			},
			"point_2": {
					"positions": [
						math.radians(2.86),
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [
						math.radians(5.73),
						0.0,
						0.0,
						0.0,
						0.0,
						0.0,
					],
					"accelerations": [0.0] * 6,
					"time_from_start": 3.0,
			},
		},
	}

	traj_2 = {
		"joint_names": ["j1", "j2", "j3", "j4", "j5", "j6"],
		"points": {
			"point_1": {
					"positions": [
						math.radians(2.89),
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 5.0,
			},
			"point_2": {
					"positions": [
						0,
						math.radians(90),
						0,
						0,
						0,
						0,
					],
					"velocities": [0.0] * 6,
					"accelerations": [0.0] * 6,
					"time_from_start": 7,
			},
		},
	}

	post_cnt = 0


	def is_prog_running(base_url: str) -> bool:
		uri = f"{base_url}/project/rgen"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.get(url=uri, headers=headers)
			return ret.json()["is_playback"]
		except Exception as e:
			print(f"Error in is_prog_running")
			return None


	def get_jt_buff_avail_num(base_url) -> int:
		uri = f"{base_url}/project/robot/trajectory/joint_traject_buf_avail"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.get(url=uri, headers=headers)
			return ret.json()["val"]
		except Exception as e:
			print(f"Error in get_jt_buff_avail_num: {e}")
			return None


	def post_trajectories(base_url: str, trajects: dict):
		global post_cnt
		uri = f"{base_url}/project/robot/trajectory/joint_traject_insert_points"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		if is_prog_running(base_url) == False:
			print("Program is not running!")
			return None

		n_jt_buff_avail = get_jt_buff_avail_num(base_url)
		if n_jt_buff_avail <= 0:
			print("Current joint trajectory buffer is full.")
			return None

		try:
			start = time.time()
			ret = session.post(url=uri, headers=headers, json=trajects)
			end = time.time()
			elapsed_ms = (end - start) * 1000

			print(
					f"[{post_cnt}] elapsed_ms: {elapsed_ms:.3f} ms. available jt buff: {n_jt_buff_avail - 1}/2048"
			)
			post_cnt += 1

			print((ret.status_code, ret.json()))

			ret.raise_for_status()
			return ret
		except Exception as e:
			print(f"Error in post_trajectories: {e}")
			return None


	def post_init_trajectories(base_url: str):
		uri = f"{base_url}/project/robot/trajectory/joint_traject_init"
		headers = {"Content-Type": "application/json; charset=utf-8"}

		try:
			ret = session.post(url=uri, headers=headers)
			ret.raise_for_status()
			return ret
		except Exception as e:
			print(f"Error in post_init_trajectories: {e}")
			return None


	if __name__ == "__main__":
		base_url = "http://192.168.1.150:8888"
		# base_url = "http://127.0.0.1:8888"  # hrspace

	while True:
		post_init_trajectories(base_url)
		ret = post_trajectories(base_url, traj_1)
		time.sleep(1)  # 1초 후 연속적으로 궤적을 post
		ret = post_trajectories(base_url, traj_2)
		time.sleep(8)  # 최종 time_from_start 를 고려하여 1초를 더한 8초로 설정
	```

  ```sh
		$python test.py
		[0] elapsed_ms: 6.122 ms. available jt buff: 2047/2048
		<Response [200]> {'_type': 'JObject'}
		[1] elapsed_ms: 3.997 ms. available jt buff: 2046/2048
		<Response [200]> {'_type': 'JObject'}
		...
	```


</div>

[__SOURCE](5-robot/2-post/9-joint_traject_insert_point.md)
#### 5.1.9 `joint_traject_insert_point`

##### 설명
- 지원 버전 : `70.00-00` ↑
- `POST` : 조인트 궤적 실행을 위해 **다음 조인트 목표 포인트를 순차적으로 추가**합니다.
- 해당 API를 반복 호출하여 연속적인 조인트 궤적을 구성할 수 있습니다.


##### 주의 사항

동작 조건: 프로그램 실행 상태 유지
* API는 반드시 제어기 프로그램이 실행 중일 때만 호출해야 합니다.
* 정상 예시: 자동 모드에서 `wait di1` 구문 실행 상태
* 발생 에러: [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) (외부지령 동작 가능 상태 에러)

물리 조건: 제한 속도 및 토크 준수
* 시스템이 허용하는 최대 속도 및 토크를 초과하는 지령은 에러가 발생합니다.
* 기본 에러: [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) (축속도 제한값 초과 에러)

과토크 지령 시 발생하는 연쇄 알람
* 감속기 과토크: [E249](https://hr-alarms.web.app/#/${cont_model}/ko/E249) · [E6402](https://hr-alarms.web.app/#/${cont_model}/ko/E6402) · [E6403](https://hr-alarms.web.app/#/${cont_model}/ko/E6403)
* 감속기 과전류: [W153](https://hr-alarms.web.app/#/${cont_model}/ko/W153) · [W181](https://hr-alarms.web.app/#/${cont_model}/ko/W181) · [W182](https://hr-alarms.web.app/#/${cont_model}/ko/W153)
* 위치편차 초과: [E2630](https://hr-alarms.web.app/#/${cont_model}/ko/E2630) · [E2636](https://hr-alarms.web.app/#/${cont_model}/ko/E2636) · [E2638](https://hr-alarms.web.app/#/${cont_model}/ko/E2638)

참고: 실제 표출되는 알람은 축 구성, 하중(Payload), 동작 상황에 따라 다를 수 있습니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
```

##### request-body

```json
{
	"interval": 0.01,
	"time_from_start": 0.0,
	"look_ahead_time": 0.5,
	"point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

* interval

  * 증분 방식으로 포인트를 추가할 때 사용되는 시간 간격
* time_from_start

  * 궤적 시작 시점으로부터의 누적 시간
* look_ahead_time

  * 궤적 실행을 위한 look-ahead 시간
* point

  * 각 조인트의 목표 각도 배열 (deg)


##### response

1. status code
   * 200 : OK
   * 400 : Bad Request
     * request body 가 유효성 검사에서 실패한 경우
   * 403 : Forbidden
   * 404 : Not Found


##### 사용 예

```python
request url:
POST /project/robot/trajectory/joint_traject_insert_point

request-body:
{
    "interval": 0.01,
    "time_from_start": 0.0,
    "look_ahead_time": 0.5,
    "point": [0.0, 10.0, -20.0, 30.0, 0.0, 15.0]
}
```

</div>

Python Script 예시

사전준비
1. 로봇 기준자세로 이동. (예시 - 6축 기준, [0, 90, 0, 0, -90, 0])
2. job 에서 ```wait di1``` 의 구문을 입력한다
3. 자동모드로 전환하고 프로그램을 재생한다.
4. 그 상태로 하기 테스트 코드를 실행한다.

<div style="width: fit-content;">

```python
# test.py
import time

import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888" # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}

    try:
        r = session.get(BASE_URL + path, params=params)
        return r.json().get("position")
    except Exception:
        return None


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }

    try:
        session.post(BASE_URL + path, json=body)
    except Exception as e:
        print(f"[ERROR] {e}")


def fmt6(arr):
    if arr is None:
        return None
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02, 89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04, 89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06, 89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08, 89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10, 89.90, 0.0, 0.0, -90.0, 0.0],
    ]

    with requests.Session() as s:
        before = get_joint_positions(s)
        print("BEFORE: ", fmt6(before), end="\n\n")

        t = 0.0
        for i, p in enumerate(points, 1):
            t += interval
            insert_point(s, p, interval, look_ahead_time, t)
            print(f"[INSERT {i}] OK  t={t:.6f}s")
            time.sleep(0.001)

        time.sleep(0.05)

        after = get_joint_positions(s)
        print("\nAFTER:", fmt6(after))


if __name__ == "__main__":
    main()
```

```sh
$python test.py
BEFORE:  ['0.000000', '90.000000', '0.000000', '0.000000', '-90.000000', '0.000000']

[INSERT 1] OK  t=0.002000s
[INSERT 2] OK  t=0.004000s
[INSERT 3] OK  t=0.006000s
[INSERT 4] OK  t=0.008000s
[INSERT 5] OK  t=0.010000s

AFTER: ['0.072196', '89.928004', '0.000000', '-0.000574', '-90.000000', '-0.001393']
```

</div>

[__SOURCE](6-io_plc/README.md)
# 6. I/O PLC

- 내장 PLC(built-in plc)의 입출력 값을 읽어오거나 설정합니다.
[__SOURCE](6-io_plc/1-get/README.md)
## 6.1 io_plc/get

- 내장 PLC(built-in plc)의 입출력 값에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](6-io_plc/1-get/1-relay-value.md)
#### 6.1.1 `get relay values`

##### 설명

- `GET` : relay 값을 객체.타입 전체에 대해 얻습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

##### path-variable

[릴레이명](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/ko/3-relay/2-relay-expression?cont_model=${cont_model}) (소문자 표기)

* `di`, `do`, `x`, `y`에는 `{obj_type}{obj_idx}_`를 지정해야 합니다.  
  나머지 `relay_type`에는 지정하지 않습니다.

- `obj_type` : 객체 타입 (`fb`, `fn`)

- `obj_idx` : 객체 인덱스 (`fb`: `0` ~ `9`, `fn`: `0` ~ `63`)

- `relay_type` : `di`, `do`, `x` , `y` , `m` , `s` , `r`, `k`



##### query-parameter

- `st` : 시작 byte index (default: 0)
- `len` : dword 개수 (default: 8)

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 정상 응답 시 relay 값(list) 반환. e.g [0, 0, 0, 0]

##### 사용 예

```python
request url:
GET /project/plc/s/val_s32

response-body:
[
    16975105,
    132579331,
    252449291,
    406585366,
    327681,
    712706500,
    118947845,
    28
]
```

```python
request url:
GET /project/plc/m/val_s32?st=32&len=4

response-body:
[
    0,
    -2139095040,
    0,
    134217728
]
```
</div>

Python Script 예제

<div style="width: fit-content;">

```python
# test.py
import requests


def get_relay_value() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/plc/m/val_s32"
    query_parameter = {"st": "32", "len": "4"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_relay_value())
```
```sh
$python test.py
(200, [0, 0, 0, 0])
```
</div>

[__SOURCE](6-io_plc/1-get/2-ios-dio.md)
#### 6.1.2 `ios/dio/{dio_val}`

##### 설명

- `GET` : 사용자 IO 값을 얻습니다.
- 시스템 입출력에 대한 값은 [sio api](./3-ios-sio.md)를 참조하십시오.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ios/dio/{dio_val}
```
</div>

##### path-variable

- `dio_val` :
  - `di_val` : 입력(di) 값을 얻습니다.
  - `do_val` : 출력(do) 값을 얻습니다.

##### query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- 정상 응답 시 signed decimal 값 반환
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : -99}
		```
		</div>


##### 사용 예

- fb2.dob3 값 얻기. (결과값 : 0b11001000 = 0xc8 = -56)

<div style="width: fit-content;">

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```
</div>

Python Script 예시

<div style="width: fit-content;">

```python
import requests

BASE_URL = "http://127.0.0.1:8888"


def get_do_val(sig_no: int = 0) -> requests.Response:
    path = "/project/control/ios/dio/do_val"
    params = {"type": "dob", "blk_no": 0, "sig_no": sig_no}
    return requests.get(BASE_URL + path, params=params)


def get_di_val(sig_no: int = 0) -> requests.Response:
    path = "/project/control/ios/dio/di_val"
    params = {"type": "dib", "blk_no": 0, "sig_no": sig_no}
    return requests.get(BASE_URL + path, params=params)


def extract_u8(res: requests.Response) -> int:
    assert res is not None, "response is necessary."

    res.raise_for_status()

    payload = res.json()
    if "val" not in payload:
        raise KeyError(f"no 'val' in response: {payload}")

    # MSB (Most Significant Bit) -> LSB (Least Significant Bit)
    return int(payload["val"]) & 0xFF


def lsb_first(u8: int) -> str:
    # LSB -> MSB
    return format(u8, "08b")[::-1]


do_u8 = extract_u8(get_do_val(2))
di_u8 = extract_u8(get_di_val(1))

print("do value:", lsb_first(do_u8))
print("di value:", lsb_first(di_u8))

```
```sh
# (when fb0.do18 = 1, fb0.do20 = 1 / fb0.di14 = 1)
$python test.py
do value: 00101000
di value: 00000010
```

</div>

[__SOURCE](6-io_plc/1-get/3-ios-sio.md)
#### 6.1.3 `ios/sio/{sio_val}`

##### 설명

- `GET` : 시스템 IO 값을 얻습니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /project/control/ios/sio/{sio_val}
```

##### path-variable

- `sio_val` :
  - `si_val` : 입력(si) 값을 얻습니다.
  - `so_val` : 출력(so) 값을 얻습니다.

##### query-parameter

- `type` : io 값의 타입
  - si or so : bit
  - sib or sob : signed-byte
  - siw or sow : signed-word (2byte)
  - sil or sol : signed-dword (4yte)
  - sif or sof : float
- `sig_no` : 신호 인덱스 (0~)

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- 정상 응답 시 decimal 값 반환
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : 6}
		```
		</div>
		이를 binary 로 표현하면 0b0110 으로, 시스템 출력의 둘째,셋째 칸에 녹색 불이 들어오게 됨

##### 사용 예

- sob2 값 얻기. (결과값 : 6 = 0x06 = 0b0110)

```python
request url:
GET /project/control/ios/sio/si_val?type=sob&sig_no=2

response-body:
{
    "_type" : "JObject",
    "val" : 2,
}
```
</div>

Python Script 예시


<div style="width: fit-content;">

```python
# test.py
import requests


def get_sio_val() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ios/sio/so_val"
    query_parameter = {"type": "sob", "sig_no": 2}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_sio_val())
```
```sh
$python test.py
(200, {'_type': 'JObject', 'val': 6})
```
</div>

[__SOURCE](6-io_plc/2-post/README.md)
## 6.2 io_plc/post

- 내장 PLC(built-in plc)의 입출력 값에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](6-io_plc/2-post/1-set_relay_value.md)
#### 6.2.1 `set relay values`

##### 설명

- `POST` : relay 값 설정합니다.

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/plc/set_relay_value
```

##### request-parameter

- `name` : 설정하려는 릴레이명을 [표기법](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/ko/3-relay/2-relay-expression?cont_model=${cont_model})에 맞춰 입력합니다.
- `value` : 상기 표기법의 `data-type` 에 유의하여 설정하려는 값을 입력합니다.
```json
{
    "name": "fb3.dof14",
    "value": "2.718"
}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{ "_type":"JObject" }
	```
	</div>
</div>

##### 사용 예

<div style="width: fit-content;">

```json
request url:
POST /project/plc/set_relay_value

request-body:
{
    "name": "fb1.do0",
    "value": "1"
}

response-body:
{ "_type":"JObject" }
```
</div>

<div style="width: fit-content;">

Python Script 예제

```python
# test.py
import requests


def get_relay_value() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/plc/fb1_do/val_s32"

    response = requests.get(url=base_url + path_parameter)

    return response


# @measure_api
def post_set_relay_value() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/plc/set_relay_value"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"name": "fb1.do0", "value": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret1 = get_relay_value()
ret2 = post_set_relay_value()
ret3 = get_relay_value()

print((ret1.status_code, ret1.json()))
print((ret2.status_code, ret2.json()))
print((ret3.status_code, ret3.json()))

```
```sh
$python test.py
(200, [0, 0, 0, 0, 0, 0, 0, 0])
(200, {'_type': 'JObject'})
(200, [1, 0, 0, 0, 0, 0, 0, 0])
```
</div>

[__SOURCE](6-io_plc/2-post/2-ios-dio.md)
#### 6.2.2 `ios/dio/{do_val}`

##### 설명

- `POST` : 디지털 출력을 변경합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /project/control/ios/dio/do_val
```
</div>

##### request-body


<div style="width: fit-content;">

```json
{
  "type": "do",
  "blk_no": 1,
  "sig_no": 1,
  "val": 1
}
```
</div>

##### query-parameter

- `type` : io 값의 타입
  - do : bit
  - dob : signed-byte
  - dow : signed-word (2byte)
  - dol : signed-dword (4yte)
  - dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)
- `val` : 변경하고자 하는 설정값


##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_text": ""}
	```
	</div>


##### 사용 예

<div style="width: fit-content;">

```python
request url:
POST /project/control/ios/dio/do_val

request-body:
{
    "type": "do",
    "blk_no": 2,
    "sig_no": 3,
    "val": -99
}
```
</div>

Python Script 예시

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.


<div style="width: fit-content;">

```python
# test.py
import requests


def post_do_val() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/control/ios/dio/do_val"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"type": "dob", "blk_no": 2, "sig_no": 3, "val": -99}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_do_val())
```
```sh
$python test.py
(200, {'_text': ''})
```
</div>

[__SOURCE](7-log_manager/README.md)
# 7. event-log

- 제어기에 기록되는 에러, 경고, 실행이력 등을 출력합니다.

[__SOURCE](7-log_manager/1-get/README.md)
## 7.1 log_manager/get

- 제어기에 기록되는 에러, 경고, 실행이력에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](7-log_manager/1-get/1-search.md)
#### 7.1.1 search

##### 설명

- `GET` : 지정한 필터 조건으로 이벤트 이력(event log)를 열람합니다.  

##### path-parameter

<div style="width: fit-content;">

```python
GET /logManager/search
```
</div>

##### query-parameter

- `n_item` : 요청 event 개수 (default=100)
- `cat_p` : 요청 범주 필터 (category positive). 각 타입을 의미하는 글자를 쉼표(,)로 결합하여 지정합니다.
            (cat_p=E,W,N)
  - `E` : 에러 (Error)
  - `W` : 경고 (Warning)
  - `N` : 알림 (Notice)
  - `S` : 기동/정지 (Start/Stop)
  - `O` : 사용자 조작 (user's Operation)
  - `I` : I/O, 릴레이 값 (I/O, relay value)
  - `P` : 주기적 상태 기록 (Periodic state)
  - `H` : 실행 이력 (History)
  - `C` : 콘솔 출력 (Console out)
  - `M` : 기타 (Miscellany)
- `id_min` : 최소 id 필터. (optional)
  - 모든 이벤트는 유일한 이벤트 ID(eid)를 가지고 있습니다. (0~)  
    기존에 수신한 이벤트들의 id 중 최대값에 1을 더해 `id_min`에 지정하여 이력 요청을 하면,  
    기존에 이미 수신한 이벤트들은 제외하고, 새로 발생한 이력만 얻을 수 있습니다.   
  - 단, 제어기 내의 이벤트 id는 최대값(0xffffffffffffffff)이 되면, 다시 0부터 생성됩니다.  
    필터링은 이러한 상황까지 고려하여 적절히 적용됩니다.  
    예를들어, id_min이 0xfffffffffffffffa 인 경우, 0, 1, 2 같은 id를 갖는 이벤트들을 필터 아웃되지 않고 응답에 포함됩니다.  
- `id_max` : 최대 id 필터. (optional)
- `ts_min` : 최소 timestamp 필터. (optional)
  - 년/월/일 시:분:초.밀리초 형식. e.g. 2023/11/20 18:50:30.955
- `ts_max` : 최대 timestamp 필터. (optional)
  - 년/월/일 시:분:초.밀리초 형식. e.g. 2023/11/20 18:50:30.955

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - `id` : 이벤트 ID (event ID)
   - `ts` : timestamp
   - `cat` : 이벤트 범주 (event category)
   - `code` : 이벤트 코드번호
   - `aux` : 이벤트 보조정보 (event auxiliary info.). 최대 280자입니다.
     - 에러와 경고, 기동/정지의 경우에는 스냅샷(snapshot) 정보를 담습니다.
   - "_text" 를 키값으로 로그 내용이 반환됩니다.
		<div style="width: fit-content;">

		```json
		{ "_text": "..." }
		```
		</div>

##### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /logManager/search?cat_p=O&id_max=24258&id_min=24253

response-body:
{
    { "id" : 24258, "ts" : "2023/11/28 16:53:31.239", "cat" : "O", "code" : "K.Click", "aux" : "Right" }
    { "id" : 24257, "ts" : "2023/11/28 16:53:30.462", "cat" : "O", "code" : "K.Down", "aux" : "SHIFT" }
    { "id" : 24256, "ts" : "2023/11/28 16:53:23.450", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24255, "ts" : "2023/11/28 16:53:23.045", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
    { "id" : 24254, "ts" : "2023/11/28 16:53:13.695", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24253, "ts" : "2023/11/28 16:53:13.202", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
}
```
Python Script 예시


```python
# test.py
import json
import requests


def get_log_search() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/logManager/search"
    query_parameter = {"cat_p": "H"} # get history log

    responses = requests.get(url=base_url + path_parameter, params=query_parameter)

    return responses


print(get_log_search())

```

```sh
$python test.py
(200, {'_text': '{ "id" : 63010, "ts" : "2025/08/19 12:24:14.325485", "cat" : "H", "code" : "hist", "aux" : "(     12)Power saving = on " }\r\n{ "id" : 63009, "ts" : "2025/08/19 12:24:14.325480", "cat" : "H", "code" : "hist", "aux" : "(=Stamp=)[2025/8/19 12:24:15](+299921531us)" }\r\n{ "id" : 62997, "ts" : "2025/08/19 12:19:14.403964", "cat" : "H", "code" : "hist", "aux" : "(     14)>online_tracking_finish " }\r\n{ "id" : 62996, "ts" : "2025/08/19 12:19:14.403953", "cat" : "H", "code" : "hist", "aux" : "(7142148)FinalizeTracking " }\r\n
 				...
 \r\n'})
```
</div>

[__SOURCE](8-file_manager/README.md)
# 8. file_manager

- 제어기의 파일 정보를 읽어오거나, 파일 이름 변경, 파일 전송 기능을 다룹니다.
- 디렉토리 존재여부를 확인하거나, 생성 및 삭제를 하는 기능 또한 다룹니다.

[__SOURCE](8-file_manager/1-get/README.md)
## 8.1 file_manager/get

- 제어기의 파일 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](8-file_manager/1-get/1-files.md)
#### 8.1.1 `files`

##### 설명

- `GET` : 제어기로부터 파일 내용을 응답 받습니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/files
```

##### query-parameter

query-parameter 를 반드시 입력해야합니다.

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 가져올 파일 이름

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- "_text" 를 키값으로 요청한 job 파일의 내용을 반환
	- e.g.
		<div style="width: fit-content;">

		```json
		{ "_text": "Hyundai Robot Job File; { version: 2.0, mech_type: "458(HA006B-01)", total_axis: 6, aux_axis: 0 }\nS1   move P,spd=60%,accu=0,tool=1  [0.000,90.000,0.000,0.000,0.000,0.000]\n     wait di1\n     end\n" }
		```
		</div>
</div>

##### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job   <- target
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
GET /file_manager/files?pathname=project/jobs/0001.job

response-body:
{
	Hyundai Robot Job File; { version: 2.0 ... }
	...
}
```
</div>

Python Script 예시


<div style="width: fit-content;">


```python
# test.py
import requests


def get_file_contents() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_contents())
```
```sh
$python test.py
(200, {'_text': 'Hyundai Robot Job File; { version: 2.0, mech_type: "458(HA006B-01)", total_axis: 6, aux_axis: 0 }\nS1   move P,spd=60%,accu=0,tool=1  [0.000,90.000,0.000,0.000,0.000,0.000]\n     wait di1\n     end\n'})
```  

</div>

[__SOURCE](8-file_manager/1-get/2-file_info.md)
#### 8.1.2 `file_info`

##### 설명

- `GET` : 파일 경로를 기반으로 해당 파일에 대한 정보를 반환합니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/file_info
```

##### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

</div>

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - [파일 정보](../../99-schema/file_info.md)
   - 	e.g.
		<div style="width: fit-content;">

		```json
		{"mday": 11, "fname": "${cont_model:lower}_proj.json", "month": 8, "is_dir": False, "min": 51, "size": 144513, "nfiles": 0, "year": 2025, "readonly": False, "sec": 38, "nfolders": 0, "hour": 14, "wday": 1}
		```
		</div>
   - 파일이 없을 시 `404 Not Found`

##### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job <- target 
    |-- lads
    |-- log
    |-- vars
    |-- ...
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
GET /file_manager/file_info?pathname=project/jobs/0001.job

response-body:
{
    "mday": 10,
    "sec": 52,
    "fname": "0001.job",
    "wday": 5,
    "size": 40,
    "year": 2023,
    "hour": 8,
    "readonly": false,
    "month": 11,
    "is_dir": false,
    "min": 35
}
```
</div>


<div style="width: fit-content;">

Python Script 예시

```python
# test.py
import requests


def get_file_info() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/file_info"
    query_parameter = {"pathname": "project/${cont_model:lower}_proj.json"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_info())
```
```sh
$python test.py
(200, {'mday': 11, 'fname': '${cont_model:lower}_proj.json', 'month': 8, 'is_dir': False, 'min': 51, 'size': 144513, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 38, 'nfolders': 0, 'hour': 14, 'wday': 1})
```

</div>

[__SOURCE](8-file_manager/1-get/3-file_list.md)
#### 8.1.3 `file_list`

##### 설명

- `GET` : 파일 및 디렉토리 리스트를 반환합니다.

##### path-parameter


<div style="width: fit-content;">

```python
GET /file_manager/file_list
```

##### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```  
</div>


<div style="width: fit-content;">

|key|description|
|:---|:---|
|`path`|확인하려는 대상 폴더 경로|
|`incl_file`|리스트 출력 시 파일 포함 여부|
|`incl_dir`|리스트 출력 시 디렉토리 포함 여부|

</div>

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 파일 리스트를 반환
   - 	e.g.
		<div style="width: fit-content;">

		```json
		{"mday": 11, "fname": "${cont_model:lower}_proj.json", "month": 8, "is_dir": False, "min": 51, "size": 144513, "nfiles": 0, "year": 2025, "readonly": False, "sec": 38, "nfolders": 0, "hour": 14, "wday": 1}
		```
		</div>
   - 파일이 없을 시 `404 Not Found`


##### 사용 예

<div style="width: fit-content;">

```text
${cont_model}
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
GET /file_manager/file_list?path=project&incl_file=true&incl_dir=true

response-body:
[
    {
        "mday": 20,
        "sec": 24,
        "fname": "jobs",
        "wday": 1,
        "size": 8192,
        "year": 2023,
        "hour": 18,
        "readonly": false,
        "month": 11,
        "is_dir": true,
        "min": 12
    },
    {
        "mday": 31,
        "sec": 40,
        "fname": "${cont_model:lower}_proj.json",
        "wday": 2,
        "size": 130551,
        "year": 2023,
        "hour": 7,
        "readonly": false,
        "month": 10,
        "is_dir": false,
        "min": 57
    },
           ...
]
```

</div>

<div style="width: fit-content;">

Python Script 예시

```python
import requests


def print_file_list() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/file_list"
    query_parameter = {"incl_file": "true", "incl_dir": "true", "path": "project/jobs"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(print_file_list())
```
```sh
$python final_test.py
(200, [{'mday': 18, 'fname': '0002.job', 'month': 7, 'is_dir': False, 'min': 8, 'size': 543, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 44, 'nfolders': 0, 'hour': 14, 'wday': 5}, {'mday': 18, 'fname': '0003.job', 'month': 7, 'is_dir': False, 'min': 8, 'size': 1043, 
                                ...
, {'mday': 19, 'fname': '0001.job', 'month': 8, 'is_dir': False, 'min': 42, 'size': 198, 'nfiles': 0, 'year': 2025, 'readonly': False, 'sec': 6, 'nfolders': 0, 'hour': 7, 'wday': 2}])

```
</div>

[__SOURCE](8-file_manager/1-get/4-file_exist.md)
#### 8.1.4 `file_exist`

##### 설명

- `GET` : 타겟 파일의 존재 여부를 반환합니다.

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/file_exist
```

##### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 파일 존재 여부에 대한 bool 값 (True/False) 반환

##### 사용 예

<div style="width: fit-content;">

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```  

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def get_file_contents() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response


print(get_file_contents())
```
```sh
$python test.py
True
```

</div>

[__SOURCE](8-file_manager/2-post/README.md)
## 8.2 file_manager/post

- 제어기의 파일 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.

[__SOURCE](8-file_manager/2-post/1-rename_file.md)
#### 8.2.1 `rename_file`

<div style="width: fit-content;">

##### 설명

- `POST` : 타겟 파일의 파일 이름을 변경합니다.

##### path-parameter

```python
POST /file_manager/rename_file
```

##### request-body

```json
{
    "pathname_from" : "project/jobs/0001.job",
    "pathname_to"   : "project/jobs/4321.job"
}
```


- `pathname_from` : 변경 전 파일 경로
- `pathname_to` : 변경 후 파일 경로

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
     - 변경하려는 타겟 파일이 존재하지 않음
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 변경하려는 파일 경로와 변경되었을 때의 파일 경로를 응답
	 <div style="width: fit-content;">

		```json
		{"pathname_from": "project/jobs/0001.job", "pathname_to": "project/jobs/0882.job"}
		```
	</div>


##### 사용 예

<div style="width: fit-content;">

```python
request url:
POST /file_manager/rename_file

request-body: 
{
    "pathname_from" : "project/jobs/0001.job",
    "pathname_to"   : "project/jobs/4321.job"
}
```

```text
${cont_model}
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</div>

Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests

def rename_file() -> requests.Response:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = { "pathname_from" : "project/jobs/0001.job",
                        "pathname_to"   : "project/jobs/4321.job" }

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

try:
    ret = rename_file()
    print(ret.status_code, ret.json())
except:
    print(rename_file())
```
```sh
$python test.py
(200, {'pathname_from': 'project/jobs/0001.job', 'pathname_to': 'project/jobs/4321.job'})
```

</div>

[__SOURCE](8-file_manager/2-post/2-mkdir.md)
#### 8.2.2 `mkdir`



##### 설명

- `POST` : 타겟 경로에 디렉토리를 생성합니다.  

##### path-parameter

<div style="width: fit-content;">

```python
GET /file_manager/mkdir
```


##### request-body

<div style="width: fit-content;">

- 생성하려는 디렉토리 타겟 위치
	```json
	{ "path" : "project/jobs/special" }
	```

</div>

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
     - 변경하려는 타겟 파일이 존재하지 않음
   - 403 : Forbidden
   - 404 : Not Found
   - 500 : Internal Server Error
     - 타겟 위치에 디렉토리 이름이 중복되는 경우

2) response-body
   - 생성하려는 디렉토리 타겟 위치
		<div style="width: fit-content;">

		```json
		{ "path" : "project/jobs/special" }
		```
		</div>

##### 사용 예
<div style="width: fit-content;">

```python
request url:
GET /file_manager/mkdir

request-body:
{
    "path" : "project/jobs/special"
}
```

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- ${cont_model:lower}_proj.json
```
</div>


Python Script 예시

<div style="width: fit-content;">

```python
# test.py
import requests


def post_mkdir() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/mkdir"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"path": "project/jobs/special"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


try:
    ret = post_mkdir()
    print(ret.status_code, ret.json())
except:
    print(post_mkdir())
```
```sh
$python test.py
200 {'path': 'project/jobs/special'}
```
</div>

[__SOURCE](8-file_manager/2-post/3-files.md)
#### 8.2.3 `files`

##### 설명

- `POST` : 타겟 경로에 파일을 전송합니다.

##### path-parameter


<div style="width: fit-content;">

```python
POST /file_manager/files/{target_filepath}
```

##### path-variable

- `target_filepath` : 확장자를 포함한 타겟 파일 경로

##### request-body

- binary 형식의 파일
- `Content-Type` 은 `application/octet-stream` 이어야합니다.

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body

	<div style="width: fit-content;">

	```json
	{"_text": ""})
	```
	</div>

##### 사용 예

```text
${cont_model}
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- ${cont_model:lower}_proj.json
```

```python
request url:
POST /file_manager/files/project/jobs/test.job
```

</div>

Python Script 예시

```python
# test.py
import requests


def post_file_transfer() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    path_value = "/project/jobs/3344.job"  # target

    target_file = base_url + path_parameter + path_value
    source_file = "D:\\temp\\test.job"  # source (path for WindowOS)

    with open(source_file, "rb") as file:
        response = requests.post(
            url=target_file,
            data=file,
            headers={"Content-Type": "application/octet-stream"},
        )

    return response


print(post_file_transfer())
```
```sh
$python test.py
(200, {'_text': ''})
```

[__SOURCE](8-file_manager/3-delete/README.md)
## 8.3 file_manager/delete

- 제어기의 파일 정보에 대한 DELETE 요청을 보냅니다.
[__SOURCE](8-file_manager/3-delete/1-files.md)
#### 8.3.1 `files`

<div style="width: fit-content;">

##### 설명

- `DELETE` : 타겟 파일 또는 디렉토리를 삭제합니다.

##### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

##### response
1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
   - 없음. status code 만 반환
   - 삭제할 대상의 파일이 없어도 통신상에 문제가 없으면 상태코드 200 응답

##### 사용 예

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```

```text
${cont_model}
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python Script 예시

```python
# test.py
import requests


def delete_file() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/file_manager/files"
    target_file = "/project/jobs/0001.job"

    response = requests.delete(url=base_url + path_parameter + target_file)

    return response


ret = delete_file()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)
```
```sh
$python test.py
<Response [200]>
```
</div>

[__SOURCE](9-task/README.md)
# 9.task

- 태스크와 관련된 내용들을 다룹니다.
- 특정 태스크나 전체 태스크에 대해서 리셋을 할 수 있습니다.
- 현재 태스크의 지역 또는 전역 변수에 대해서 값을 읽어오거나 새로운 변수를 선언할 수 있습니다.
- 태스크 실행 중 특정 작업 흐름(ex. wait)에 대해서 특정 조치(ex. release)를 취할 수 있습니다.
[__SOURCE](9-task/1-get/README.md)
## 9.1 task/get

- 태스크와 관련된 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](9-task/2-post/README.md)
## 9.2 task/post

- 태스크와 관련된 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](9-task/2-post/1-cur_prog_cnt.md)
#### 9.2.1 `task/cur_prog_cnt`

<div style="width: fit-content;">

##### 설명

- `POST` : 태스크의 현재 프로그램 카운터를 설정합니다.

##### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

##### request-body

- [cur_prog_cnt 요청 파라미터](../.././99-schema/cur_prog_cnt.md)
- 원격모드에서 동작하는 api로, 외부선택 옵션(ext_sel: 1)을 선택해야합니다.

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 허용되지 않는 요청을 한 경우
     - `err_code` (<0) 반환. 하기 에러코드 참조
   - 404 : Not Found

2) response-body
   - [cur_prog_cnt 응답 파라미터](../.././99-schema/cur_prog_cnt.md)

3) error code

	<div style="width: fit-content;">

   	- -1114208 : 원격모드가 아닌 경우
   	- -1442080 : 프로그램 재생 중 적용 불가
   	- -1245280 : 유효하지 않은 프로그램 카운터

   		> api 로 프로그램을 start/stop 한 뒤 cur_prog_cnt 를 호출 하는 경우  
   		> '유효하지 않은 프로그램 카운터' 에러가 발생할 수 있습니다.  
   		> set_cur_pc_idx api 로 현재 커서 위치를 상단(idx: 1)으로 옮기고 호출하면 정상 동작합니다.

	</div>

##### 사용 예

```python
request url:
POST /project/context/tasks[0]/cur_prog_cnt

request-body:
{
    "pno":1,
    "sno":-1,
    "fno":-1,
    "ext_sel":1
}
```

Python Script 예시

```python
import requests


def post_cur_prog_cnt() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://192.168.1.150:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/cur_prog_cnt"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {"pno": 1, "sno": 0, "fno": 0, "ext_sel": 1}

    response = requests.request(
        "POST", base_url + path_parameter, headers=headers, json=body
    )

    return response


ret = post_cur_prog_cnt()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$python python test.py
(200, {'_type': 'JObject', 'sno_new': 0, 'ofs_moved': 0, 'fno_new': 0, 'ln_new': 0})
```
</div>

[__SOURCE](9-task/2-post/2-reset.md)
<link rel="stylesheet" href="../../_assets/style.css">

#### 9.2.2 `task/reset`

<div style="width: fit-content;">


{% hint style="warning" %}

R코드 0 호출 시 프로그램 카운터가 초기화되어 로봇 오작동의 원인이 될 수 있습니다.<br>
에러 초기화 용도로는 R코드 1을 사용하십시오.<br>
이를 무시하고 무분별한 R코드 0 호출로 발생한 문제에 대해 당사는 책임지지 않습니다.

{% endhint %}

##### 설명

- `POST`: 스텝 카운터를 초기화하여 STEP0으로 이동합니다.
- [R코드 1](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/ko-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) 또는 [R코드 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/ko-tp630/8-r-code/1-use-r-code?cont_model=${cont_model})를 활용합니다.  <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;">
    R코드 1, 0 이외의 코드는 예정된 동작이 아닙니다.
</span>
- R코드 1을 진행한 이후에 프로그램 카운터 조작이 필요한 경우는 명시적으로 [cur_prog_cnt](./1-cur_prog_cnt.md), [set_cur_pc_idx](./6-set_cur_pc_idx.md) api 를 활용하십시오.


##### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

##### request-body

```json
{"code": 1}
```

##### response

1) status code
	- 200 : OK
	- 400 : Bad Request
		- request body 가 유효성 검사에서 실패한 경우
	- 403 : Forbidden
	  - 허용되지 않는 요청을 한 경우
	  - `err_code` (<0) 반환. 하기 에러코드 참조
	- 404 : Not Found

2) response-body
   - code: 요청한 rcode 번호가 반환
		<div style="width: fit-content;">

		```json
		{"code": 1, ... })
		```
		</div>

##### 사용 예

```python
request url:
POST /project/service/r_code/execute

request-body:
{
    "code":1
}
```

Python Script

```python
# test.py
import requests


def post_rcode() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response


print(post_rcode())
```
```sh
$python test.py
(200, {'code': 1, 'description': '', 'params': [], 'subcode': 0})
```

</div>

[__SOURCE](9-task/2-post/3-assign_var_expr.md)
#### 9.2.3 `assign_var_expr`

<div style="width: fit-content;">

##### 설명

- `POST` : 태스크 구문의 변수를 재지정합니다.

##### path-parameter

```python
POST /project/context/tasks[{task index}]/assign_var_expr
```

##### request-body

- `name` : 변수명
- `expr` : 변수에 대입할 수식
- `save` : 저장 유무 (true/false). 변수 파일에 해당 데이터를 저장하기 위함입니다.
- `scope` : 해당 변수의 유효 스코프 설정
	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

##### response

1) status code
	- 200 : OK
	- 400 : Bad Request
	- 403 : Forbidden
	- 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>



##### 사용 예

현재 태스크에 지역 변수 a 가 선언된 상태인 경우

```python
request url:
POST /project/context/tasks[0]/assign_var_expr

request-body
{
    "name" : "a",
    "scope": "local",
    "expr" : "465 + 312",
    "save" : "true"
}
```


Python Script 예시

```python
# test.py
import requests


def post_read_var(var: str, scope=None) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/solve_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"expr": f"{var}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


def assign_var_expr(var: str, scope=None, expression: str = "") -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/assign_var_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"name": f"{var}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret1 = post_read_var("a", "local")
ret2 = assign_var_expr("a", "local", "465 + 312")
ret3 = post_read_var("a", "local")

try:
    print((ret1.status_code, ret1.json()))
    print((ret2.status_code, ret2.json()))
    print((ret3.status_code, ret3.json()))
except:
    print(ret1)
    print(ret2)
    print(ret3)
```
```sh
$python test.py
(200, 0)
(200, {'_type': 'JObject'})
(200, 777)
```

</div>

[__SOURCE](9-task/2-post/4-assign_var_json.md)
#### 9.2.4 `assign_var_json`

<div style="width: fit-content;">

##### 설명

- `POST` : 태스크 구문의 변수를 재지정합니다.

##### path-parameter

```python
POST /project/context/tasks[{task index}]/assign_var_json
```

##### request-body

- `name` : 변수명
- `json` : 변수에 대입할 json 형태의 문자열
- `save` : 저장 유무 (true/false). 변수 파일에 해당 데이터를 저장하기 위함입니다.
- `scope` : 해당 변수의 유효 스코프 설정
	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|


	```json
	{
		"name" : "a",
		"scope": "local",
		"json" : "{\"test\": 10}",
		"save" : "true"
	}
	```

##### response

1) status code
	- 200 : OK
	- 400 : Bad Request
	- 403 : Forbidden
	- 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject", ${request-body 에서 요청한 body의 json값}}
	```
	</div>

	e.g. "json" 으로 {"test":10} 을 요청한 경우
	<div style="width: fit-content;">

	```json
	{"_type": "JObject", "test": 10}
	```
	</div>


##### 사용 예


현재 태스크에 지역 변수 a 가 선언된 상태일 경우

```python
request url:
POST /project/context/tasks[0]/assign_var_json

request-body
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```

Python Script 예시

```python
# test.py
import requests


def post_read_var(var_name: str, scope=None) -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/solve_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.json()


def assign_var_json(var_name: str, scope=None, var_json: str = "") -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/assign_var_json"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "name": f"{var_name}",
        "scope": f"{scope}",
        "json": f"{var_json}",
        "save": "true",
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"before: {post_read_var('a', 'local')}")
print(f"""response: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py
before: 777
response: 200
after: {'_type': 'JObject', 'test': 10}
```

</div>

[__SOURCE](9-task/2-post/5-release_wait.md)
#### 9.2.5 `release_wait`

<div style="width: fit-content;">

##### 설명

- `POST` : WAIT 을 실행중인 태스크에 대해서 wait 상태를 강제로 해제합니다.
- **<u>필요 조건</u>** : `[F2: 시스템] - 1: 사용자 환경` 진입 후 `wait(di/wi) 강제 해제` 항목 `[유효]` 선택

##### path-parameter

```python
POST /project/context/tasks[{task index}]/release_wait
```

##### request-body

```json
{}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
     - 상기 필요 조건 불충족
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>

3) error code
   - -1442069 : 사용자 환경 설정 오류. 상기 필요 조건을 확인하십시오.


##### 사용 예

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

Python Script 예시

```python
import requests


def post_release_wait() -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/release_wait"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


ret = post_release_wait()
try:
    print((ret.status_code, ret.json()))
except:
    print(ret)

```
```sh
$python test.py
(200, {'_type': 'JObject'})
```

</div>

[__SOURCE](9-task/2-post/6-set_cur_pc_idx.md)
#### 9.2.6 `set_cur_pc_idx`

<div style="width: fit-content;">

##### 설명

- `POST` : 현재 커서를 index 라인(>=0)에 위치 시키는 함수

##### path-parameter

```python
POST /project/context/tasks[{task index}]/set_cur_pc_idx
```

##### request-body
-
	<div style="width: fit-content;">

	```json
	{ "idx": 1 }
	```
	</div>

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	{"_type": "JObject"}
	```
	</div>



##### error code

- -38501 : 재생 중인 task 가 있을 때는 적용이 되지 않습니다.

##### 사용 예

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
  "idx": 2
}
```


Python Script

```python
# test.py
import requests


def set_cur_pc_idx() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/set_cur_pc_idx"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"idx": 1}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(set_cur_pc_idx())
```
```sh
$python test.py
(200, {'_type': 'JObject'})
```
</div>

[__SOURCE](9-task/2-post/7-solve_expr.md)
#### 9.2.7 `solve_expr`

<div style="width: fit-content;">

##### 설명

- `POST` : 표현식(expression)을 풀어서 나오는 결과 값을 태스크의 지역 또는 전역 변수에 설정합니다.

##### path-parameter

```python
POST /project/context/tasks[{task index}]/solve_expr
```

##### request-body
- `expr` : 풀려고 하는 수식(expression)을 입력합니다
- `scope` : `expr` 에 대한 스코프를 설정합니다.

	|`local`|`global`|`미설정`|
	|:---|:---|:---|
	|지역 변수|전역 변수|전체 스코프|

	```json
	{
		"expr" : "a",
		"scope" : "local"
	}
	```
##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	<div style="width: fit-content;">

	```json
	13 // 현재 지정된 scope 안의 expr 값을 읽어옵니다.
	```
	</div>

##### 사용 예

<blockquote>

```python
# 1. 현재 Task 에서 선언된 "지역" 변수 a 값 읽어오기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr"  : "a",
    "scope" : "local"
}

response-body:
13
```

</blockquote>

<blockquote>

```python
# 2. 현재 Task 에서 선언된 "전역" 변수 a 값 읽어오기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr"  : "a",
    "scope" : "global"
}

response-body:
10
```

</blockquote>

<blockquote>

```python
# 3. 지역 변수 a 의 값에 대해서 -234 를 더하기
request url:
GET /project/context/tasks[0]/solve_expr

request-body:
{
    "expr": "a + (-234)"
}

response-body:
1000
```

</blockquote>

Python Script 예시
- 로봇 제어기의 태스크 영역에 지역 및 전역 변수 a 값이 설정된 상태로 하기 코드 실행

```python
# test.py
import requests


def post_read_var(var_name: str, scope=None) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/solve_expr"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


print(post_read_var("a", "local"))
print(post_read_var("a", "global"))
```
```sh
$python test.py
(200, 1234)
(200, 0)
```
</div>

[__SOURCE](9-task/2-post/8-execute_move.md)
<script id="page-config" type="application/json">
{
	"permittedStrs": ["Hi6"]
}
</script>

#### 9.2.8 `execute_move`

<div style="width: fit-content;">

##### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : 지정한 포즈로 이동합니다.

{% hint style="warning" %}
HRSpace 사용 시 주의<br>
VRC_Hi6 버전 v60.30-10 ~ v60.32-06에서 execute_move 원격 제한 오류 발생<br>
→ v60.30-09 이하 또는 v60.32-07 이상 사용 권장 (실제 Hi6 제어기 영향 없음)
{% endhint %}

##### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### request-body
- `stmt` : 요청 바디의 키 값으로, 구문(statment)을 뜻합니다.
- move 문 작성법과 관련된 내용은 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/ko/5-moving-robot/4-move?cont_model=${cont_model:lower})을 참조 바랍니다.
	<div style="width: fit-content;">

	```json
	{
		"stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
	}
	```
	</div>
1. status code
   - 200 : OK
   - 400 : Bad Request
    - request body 가 유효성 검사에서 실패
   - 403 : Forbidden
    - 원격모드가 아닌 상태로 API 요청(v60.30-07 부터 적용)
   - 404 : Not Found

2. response-body
	- v60.30 이하 정상 응답
		<div style="width: fit-content;">

		```json
		{ "err_code" : 0 }
		```
		</div>
	- v60.32 이상 정상 응답

		<div style="width: fit-content;">

		```json
		{ "_type" : "JObject" }
		```
		</div>

3. error code
   - -38500 : 원격 모드가 아닌 상태로 해당 api 요청
   - -1442071 : MOTOR OFF 에서 api 요청
   - -1442080 : 프로그램 자동 운전 중에 api 요청
   - -1376272 : api 요청 수행 중 로봇 언어 문법 오류 발생

Python Script 예시
- 모터온이 된 상태에서, 현재 로봇 축에 맞는 pose 명령문 입력

```python
# test.py
import requests
import time


def post_execute_move(in_pose: str) -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response


poses = ["[-10, 90, -10, 0, 0, 0]", "[-5, 90, 5, 0, 0, 0]", "[0, 90, 0, 0, 0, 0]"]

for idx, pose in enumerate(poses):
    res = post_execute_move(pose)
    print((res.status_code, res.json()))

    if idx < len(poses) - 1:
        time.sleep(1.5)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
``````

</div>

[__SOURCE](10-console/README.md)
# 10. console

- ${cont_model}s 제어기 S/W 의 CLI 명령어를 사용할 수 있습니다.
- 로봇언어로 할 수 있는 다양한 동작을 수행할 수 있습니다.

[__SOURCE](10-console/1-get/README.md)
## 10.1 console/get

- 로봇 명령문 실행과 관련된 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.
[__SOURCE](10-console/2-post/README.md)
## 10.2 console/post

- 로봇 명령문 실행과 관련된 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.
[__SOURCE](10-console/2-post/1-execute_cmd.md)
<div style="width: fit-content;">

#### 10.2.1 `execute_cmd`


##### 설명

- 지원 버전 : `60.28-00` &uparrow;
- `POST` : ${cont_model} 제어기의 콘솔 명령어를 실행합니다.    
- [CLI 로봇 언어 명령어 형식](../.././99-schema/robotlang.md)에 따른 명령을 수행할 수 있습니다.  

##### path-parameter

```python
POST /console/execute_cmd
```

##### request-body

```json
{
    "cmd_line" : "rl.reinit"
}
```

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
    	- request body 가 유효성 검사에서 실패한 경우
   - 403 : Forbidden
     - 허용되지 않거나 서비스 되지 않는 API 에 대해서 요청을 한 경우
   - 404 : Not Found

2) response body
	<div style="width: fit-content;">

	```json
	{ "_type" : "JObject" }
	```
	</div>

3) error code

   - 1: 로봇 언어 명령어 규칙을 벗어난 경우


##### 사용 예

</blockquote>

Python Script 예시
- `모터온` 이후 `원격모드` 상태에서 하기 명령어 수행 가능
- 현재 로봇 축 수에 맞춰서 move 문 입력 시 수행 가능

```python
# test.py
import time
import requests


cmds = [
    "rl.stop",   # 외부정지
    "rl.reinit", # 재시작
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
    "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
    "rl.i end",
    "rl.start",  # 재생
]

def post_execute_cmd(cmd: str) -> int:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.1:8888"  # hrspace
    path_parameter = "/console/execute_cmd"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"cmd_line": cmd}

    res = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return res


for cmd in cmds:
    ret = post_execute_cmd(cmd)
    print((ret.status_code, ret.json()))
    time.sleep(0.1)
```
```sh
$python test.py
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
(200, {'_type': 'JObject'})
```

</div>

[__SOURCE](11-etc/README.md)
# 11. etc

- 시스템 버전, 이벤트 로그, 클럭 등을 다루고 있습니다.
[__SOURCE](11-etc/1-clock/README.md)
## 11.1 clock

- 제어기의 시스템 시간을 읽고 설정할 수 있습니다.

[__SOURCE](11-etc/1-clock/1-get/README.md)
#### 11.1.1 clock/get

- 제어기 시스템 시간 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.

[__SOURCE](11-etc/1-clock/1-get/1-date_time.md)
#### 11.1.1.1 `date_time`

<div style="width: fit-content;">

##### 설명

- `GET` : 설정된 시스템 시간을 가져옵니다.

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response body
   - [시스템 시간 정보](../../../99-schema/date_time.md)
		<div style="width: fit-content;">

		```json
		{"_type": "JObject", "year": 2025, "min": 43, "sec": 39, "hour": 15, "wday": 2, "mon": 8, "day": 19}
		```
		</div>


##### 사용 예

<blockquote>

```python
request url:
GET /clock/date_time

response-body:
{
    "_type": "JObject",
    "year": 2025,
    "mon": 11,
    "day": 20,
    "min": 40,
    "hour": 19,
    "sec": 54
}
```
</blockquote>

Python Script 예시

```python
# test.py
import requests
import time


def get_system_time() -> requests.Response:
    base_url = f"http://192.168.1.150:8888"
    # base_url = f"http://127.0.0.1:8888"  # hrspace
    path_parameter = "/clock/date_time"
    res = requests.get(url=base_url + path_parameter)

    return res


for idx in range(5):
    res = get_system_time()
    print((res.status_code, res.json()))
    time.sleep(1)
```
```sh
$python test.py
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 39, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 40, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 41, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 42, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
(200, {'_type': 'JObject', 'year': 2025, 'min': 43, 'sec': 43, 'hour': 15, 'wday': 2, 'mon': 8, 'day': 19})
```
</div>

[__SOURCE](11-etc/1-clock/2-put/README.md)
#### 11.1.2 clock/put

- 제어기 시스템 시간 대한 PUT 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.

[__SOURCE](11-etc/1-clock/2-put/1-date_time.md)
#### 11.1.2.1 `date_time`

<div style = "width: max-content">  

##### 설명

- `PUT` : 시스템 시간을 변경합니다.
- 요청 후 `[F1: 서비스] - 9: TP 응용 프로그램 종료`를 통해 TP 를 재부팅하면 ui에 적용됩니다.

##### request-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response body
	<div style="width: fit-content;">

	```json
	{}
	```
	</div>

##### 사용 예

```python
request url:
PUT /clock/date_time

request-body:
{
    "year": 2025,
    "mon": 10,
    "day": 30,
    "hour": 18,
    "min": 30,
    "sec": 0
}
```

Python Script 예시

```python
# test.py
import requests


def put_system_time() -> requests.Response:
    base_url = "http://192.168.1.150:8888"
    # base_url = "http://127.0.0.18888"  # hrspace
    path_parameter = "/clock/date_time"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"year": 2025, "mon": 8, "day": 19, "hour": 16, "min": 50, "sec": 0}

    response = requests.put(url=base_url + path_parameter, headers=head, json=body)

    return response


print(put_system_time())
```

```sh
$python test.py
(200, {})
```
</div>

[__SOURCE](99-schema/README.md)
# 12. 스키마 (schema)

이 챕터는 Open API에서 사용되는 각종 열거자(enumeration)와 구조체(structure)의 참조자료(reference)를 담고 있습니다.


[__SOURCE](99-schema/crdsys.md)
### crdsys

#### 설명

좌표계 (coordinate system)를 지정하는 열거자 (enumeration) 입니다.  

<div style="width: fit-content;">  

|value|description|
|:---:|:---|
|`-1`|`다음` 좌표계|
|`0`|`베이스` 좌표계|
|`1`|`로봇` 좌표계|
|`2`|`축` 좌표계|
|`3`|`엔코더` 좌표계|
|`4`|`사용자` 좌표계|

</div>

[__SOURCE](99-schema/cur_prog_cnt.md)
### cur_prog_cnt

#### 설명
태스크의 현재 프로그램 카운터를 설정합니다.

<div style="width: fit-content;">  

#### request body
|key|type|description|
|:---|:---|:---|
|`pno`|int|프로그램 번호 (-1이면 현재 번호 유지)|
|`sno`|int|스텝 번호 (-1이면 현재 번호 유지)|
|`fno`|int|펑션 번호 (-1이면 현재 번호 유지)|
|`ext_sel`|int|`0` : 내부선택(원격모드에선 금지됨) <br> `1` : 외부선택(원격모드에서만 허용됨)|

</div>

<div style="width: fit-content;">  

#### response body
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|새로 이동한 스텝 번호|
|`fno_new`|int|새로 이동한 펑션 번호|
|`ln_new`|int|새로 이동한 라인번호 (프로그램 헤더가 0, 첫 명령문이 1)|

</div>

[__SOURCE](99-schema/date_time.md)
### date_time

#### 설명

<div style="width: fit-content;">  

시스템 시간 관련 정보를 나타냅니다.
|value|type|description|
|:---:|:---|:---|
|"year"|`int`|현재 시스템의 년도|
|"mon"|`int`|현재 시스템의 월|
|"day"|`int`|현재 시스템의 일|
|"hour"|`int`|현재 시스템의 시|
|"min"|`int`|현재 시스템의 분|
|"sec"|`int`|현재 시스템의 초|

</div>

[__SOURCE](99-schema/file_info.md)
### file_info

#### 설명

파일 정보 요청 시 반환되는 파라미터 입니다.

<div style="width: fit-content;">  

|key|type|description|
|:---:|:---|:---|
|fname|`str`|파일 이름|
|size|`int`|파일 크기(B, Byte)|
|year|`int`| 파일이 수정된 `년` |
|month|`int`| 파일이 수정된 `월` |
|mday|`int`| 파일이 수정된 `일` |
|wday|`int`| 파일이 수정된 `요일` (0:일, 1:월, 2:화, ...) |
|hour|`int`| 파일이 수정된 `시` |
|min|`int`| 파일이 수정된 `분` |
|sec|`int`| 파일이 수정된 `초` |
|is_dir|`bool`| 현재 파일이 디렉토리인지 확인 |
|readonly|`bool`| 읽기 전용 파일 여부 확인 |

</div>

[__SOURCE](99-schema/jobs_info.md)
### jobs_info

#### 설명

<div style="width: fit-content;">  

job 파일 정보 파라미터 입니다.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|job 파일명|
|job_commnet|`str`|주석|
|n_step|`int`|스텝 개수|
|n_total_ax|`int`|총 축 수|
|n_aux_ax|`int`|부가축 수|

</div>

[__SOURCE](99-schema/mechinfo.md)
### mechinfo

#### 설명

메커니즘 정보(mechanism info)입니다.
어떤 메커니즘들이 사용되는 지를 bit-field로 지정합니다.  

- bit 0 : M0
- bit 1 : M1
- bit 2 : M2
- bit 3 : M3
- bit 4 : M4
- bit 5 : M5
- bit 6 : M6
- bit 7 : M7

#### 사용 예

<div style="width: fit-content;">  

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 메커니즘 M0, M1, M4를 지정합니다.
```

</div>

[__SOURCE](99-schema/op_cnd.md)
### op_cnd

#### 설명
op_cnd (operation condition) : 로봇의 조건설정 값입니다.  
TP 에서 `조건설정` 버튼을 눌렀을 때 해당 값들을 확인할 수 있습니다.

<br>

<div style="width: fit-content;">  

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1사이클 <br> `2` : 반복|자동운전 동작 사이클 모드|
|step_goback_max_spd|`10` ~ `250` (mm/sec)|스텝 전/후진 시 최고속|
|step_go_func_ex|`0` : 무효 <br> `1` : 유효 <br> `2` : I ON (=DI신호)|스텝 전진 시 펑션 실행|
|func_reexe_on_trace| `0` : 무효 <br> `1` : 유효 |스텝 후진 후, 전진 시 펑션 재실행|
|path_recov_confirm|`0` : 무효 <br> `1` : 유효|스텝 전/후진 시 경로복구|
|playback_spd_rate|`1` ~ `100` (%)|자동운전 속도비율|
|robot_lock|`0` : 무효 <br> `1` : 유효 |로봇 Lock|
|intp_base|`0` : 로봇툴 <br> `1` : 정치툴|보간 기준|
|ucrd_num|`0` ~ `20`|사용자 좌표계 지정|
|plc_mode|`0` : Off -> Stop <br> `1` : Stop -> Remote Stop <br> `2` : Remote Stop -> Remote Stop <br> `3` : Remote Run -> Remote Stop <br> `4` : Run -> Off|PLC 동작 모드|

</div>

<br>

#### 예 (example)

<div style="width: fit-content;">  

```python
{
    "_type": "CondGrp",
    "playback_mode": 2,
    "step_goback_max_spd": 130,
    "step_go_func_ex": 0,
    "func_reexe_on_trace": 2,
    "path_recov_confirm": 0,
    "playback_spd_rate": 80,
    "robot_lock": 1,
    "intp_base": 1,
    "ucrd_num": 10,
    "plc_mode": 4
}
```

</div>

[__SOURCE](99-schema/pose.md)
### Pose

#### 설명

포즈(pose) 데이터입니다.

<div style="width: fit-content;">  

|key|description|
|:---|:---|
|x|X위치 (mm)|
|y|Y위치 (mm)|
|z|Z위치 (mm)|
|rx|RX각도 (deg.)|
|ry|RY각도 (deg.)|
|rz|RZ각도 (deg.)|
|j1~j16|1~16축 값(mm or deg.)|
|crd|[좌표계](./crdsys.md)|
|mechinfo|[메커니즘정보](./mechinfo.md)|
|nsync|센서동기 값의 개수 (0~2)|
|sync|센서동기 값 (문자열). e.g. `"sync(220.5,195.3)"`|

</div>

[__SOURCE](99-schema/tool_data.md)
### tool_data

#### 설명

로봇의 툴 데이터입니다.

<div style="width: fit-content;">  

|key|description|
|:---:|:---|
|`x`|X위치 (mm)|
|`y`|Y위치 (mm)|
|`z`|Z위치 (mm)|
|`rx`|RX각도 (deg.)|
|`ry`|RY각도 (deg.)|
|`rz`|RZ각도 (deg.)|
|`mass`|중량 (kg.)|
|`cx`|무게중심 X위치 (mm)|
|`cy`|무게중심 X위치 (mm)|
|`cz`|무게중심 X위치 (mm)|
|`ixx`|이너셔(inertial) X (kgm2)|
|`iyy`|이너셔(inertial) Y (kgm2)|
|`izz`|이너셔(inertial) Z (kgm2)|
|`mass_esti`|부하추정 중량 (kg.)|

</div>

[__SOURCE](99-schema/robotlang.md)
### CLI 로봇 언어 명령어

#### 설명

${cont_model} 제어기 콘솔에서 실행 가능한 로봇언어의 명령어 리스트입니다.

<div style="width: fit-content;">  

|option|description|example|
|:---|:---|:---|
|`reinit`| 로봇언어 재시작 명령을 수행합니다. |rl.reinit|
|`i`|job 파일에 로봇언어 명령문을 삽입(insert)합니다.|rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|`start`|`모터 온` 상태이고 `원격모드` 일때 해당 옵션 수행 시 로봇언어가 실행됩니다.|rl.start|
|`stop`|현재 로봇언어가 실행 중일 때, `외부정지` 진행됩니다.|rl.stop|
|`exit`|현재 실행 중인 로봇언어를 종료합니다.|rl.exit|

</div>
