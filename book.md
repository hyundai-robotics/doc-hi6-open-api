# Hi6 Open API 설명서

{% hint style="warning" %}

본 제품 설명서에서 제공되는 정보는 현대로보틱스의 자산입니다.

현대로보틱스의 서면에 의한 동의 없이 전부 또는 일부를 무단 전재 및 재배포할 수 없으며, 제3자에게 제공되거나 다른 목적에 사용할 수 없습니다.


본 설명서는 사전 예고 없이 변경될 수 있습니다.


**Copyright ⓒ 2023 by HD Hyundai Robotics**



{% endhint %}

{% hint style="warning" %}

Hi6 Open API 설명서에 공식적으로 언급되지 않은 API 를 활용하여 발생하는 모든 피해 및 문제에 대해서는 책임을 지지않습니다.

{% endhint %}## 1.1 개요

Hi6 Open API 와 관련된 아래의 기본적인 내용들을 확인하실 수 있습니다.

[1.1 Hi6 Open API 개요](./1-concept/README.md) <br>
[1.2 필요한 사전 지식](./2-prerequisite/README.md) <br>
[1.3 Hi6 Open API 예제 코드](./3-sample-code/README.md) <br>
[1.4 코딩하지 않고 쉽게 API 호출 해보기](./4-api-test/README.md)### 1.1 Hi6 Open API 에 대하여

HD현대로보틱스는 어플리케이션 개발자들이 편리하게 로봇 제어기(이하, Hi6)를 모니터링하고 원격으로 제어하기 위한 API 를 해당 문서에서 공개합니다.<br>
이를 통해 개발자들은 Hi6 개발에 적용된 소스코드에 대한 깊은 이해 없이도 Hi6의 다양한 데이터를 읽고 쓸 수 있습니다.<br>
아래 그림을 통해서 Open API 역할을 보다 쉽게 이해할 수 있습니다.


<img src="../../_assets/05_open_api_flow.png" height="250vh">

위 그림에서 주황색으로 표시된 부분들은 Open API 의 역할을 보여주고 있습니다.  

|화살표|설명|
|:---|:---|
|`실선`|개발자(클라이언트)가 정해진 4가지 방법(GET, POST, PUT, DELETE)을 이용하여 Hi6(서버)에 정보를 `요청`하는 것을 의미|
|`점선`|요청을 받은 제어기가 그에 맞는 `응답`을 json 혹은 text 형식으로 반환하는 것을 의미|

이처럼 개발자는 해당 문서의 Open API 를 활용해서 Hi6 와 이더넷으로 연결된 본인의 데스크탑, 노트북, 태블릿 pc 등을 http 와 REST API 기반으로 원격 제어 또는 모니터링을 할 수 있게 됩니다.


<br><br>


### 시작하기 전에 꼭 확인하세요!

* 현재 문서는 초기 버전으로 Hi6 Open API 버전 5를 기준으로 작성되었습니다.

* 이후 지속적으로 버전 업데이트가 있을 수 있습니다. 버전이 업데이트 되는 경우, 해당 section 을 참고하시기 바랍니다.

* HTTP REST API 클라이언트 기능 개발에 익숙한 개발자의 경우, [`1.2 필요한 사전 지식`](../2-prerequisite/README.md)부터 [`1.4 코딩하지 않고 쉽게 API 호출 해보기`](../4-api-test/README.md) 까지 건너뛰어도 좋습니다.


{% hint style="warning" %}

본 문서에 설명된 API들은 별도의 지원버전 명기가 없으면 Hi6 V60.24-00부터 지원됩니다.

본 문서에 명시되지 않은 URL 및 속성은 동일 API 버전에서 예고없이 변경될 수 있으므로, 주의 바랍니다.

{% endhint %}## 1.2 필요한 사전 지식

Open API를 활용하기 위해서는 Hi6 제어기의 기본적인 사용법을 습득해야 합니다.<br>
아래 설명서를 참고하시거나 현대로보틱스 공동훈련센터의 교육을 수강하시기 바랍니다.

- [Hi6 로봇제어기 조작설명서](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/korean-tp630/README)
- [현대로보틱스 공동훈련센터](https://www.hyundai-robotics.com/customer/customer5intro.html)

<br>

Open API는 HTTP 프로토콜 기반의 REST API입니다.<br>
다양한 개발 언어들에서 REST API (일명 RESTful API) 호출을 위한 라이브러리를 제공하고 있으며 많은 개발자들이 이를 이용해 프로그램을 개발하고 있습니다.<br>
이러한 숙련된 개발자가 아니라면, [1.1 Hi6 Open API 에 대하여](.././1-concept/README.md)에서 언급한 웹 기반의 서비스 호출과 응답이 어떻게 이뤄지는지에 대한 기본적인 개념에는 익숙한 상태여야만 합니다.<br>

이와 관련하여 아래 사항들을 참고하시기 바랍니다.

* 아래의 간단한 API 관련 설명이 낯설거나 이를 응용한 개발 경험이 풍부한 숙련자가 아니면 먼저 학습을 한 후에 해당 문서를 활용하기 바랍니다. 
* 학습이 필요한 경우, REST API 호출을 통한 클라이언트 기능의 코딩 방법을 학습하시기 바랍니다.

<br>


{% hint style="warning" %}

당사는 통상적인 REST API 클라이언트 코딩 방법에 대한 문의는 받지 않습니다.

당사는 Hi6 Open API 설명서에 공식적으로 언급되지 않은 API 사용에 의해 발생하는 모든 피해 및 문제에 대해서는 책임을 지지않습니다.

{% endhint %}

---- 

### 1.2.1 API 란?

`API`(Application Programming Interface)란 어플리케이션 소프트웨어를 빌드하고 통합하기 위한 `정의 및 프로토콜 세트`입니다 ([참조](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)).  
사용자가 `특정한 방식으로 구성된 요청`을 보내면 제공자의 소프트웨어가 이에 `응답하는 방식`입니다.  
이를 통해 구현 방식을 알지 못하는 제품 또는 서비스와도 통신할 수 있으며 어플리케이션 개발을 간소화하여 시간과 비용을 절약할 수 있습니다.

<br>


### 1.2.2 REST API 란?

`REST`(Representational State Transfer)는 API 작동 방식에 대한 조건을 부과하는 `소프트웨어 아키텍처`입니다.<br>
`REST API`는 REST 아키텍처 스타일을 따르는 API 를 뜻합니다. RESTful API 라고도 합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)).<br>
HTTP 요청을 통해 통신함으로써 리소스 내에서 레코드의 작성(Create), 읽기(Read), 업데이트(Update) 및 삭제(Delete) 등의 표준 데이터베이스 기능(CRUD)을 수행합니다.<br>

개발자는 종종 4가지의 일반적인 Hypertext Transfer Protocol(HTTP) 메서드를 사용하여 RESTful API를 구현합니다 ([참조](https://aws.amazon.com/ko/what-is/restful-api/)).<br>

- `GET` : 클라이언트는 GET을 사용하여 서버의 지정된 URL에 있는 리소스에 액세스합니다. GET 요청을 캐싱하고 RESTful API 요청에 파라미터를 넣어 전송하여 전송 전에 데이터를 필터링하도록 서버에 지시할 수 있습니다.
- `POST` : 클라이언트는 POST를 사용하여 서버에 데이터를 전송합니다. 여기에는 요청과 함께 데이터 표현이 포함됩니다. 동일한 POST 요청을 여러 번 전송하면 동일한 리소스를 여러 번 생성하는 부작용이 있습니다.
- `PUT` : 클라이언트는 PUT을 사용하여 서버의 기존 리소스를 업데이트합니다. POST와 달리, RESTful 웹 서비스에서 동일한 PUT 요청을 여러 번 전송해도 결과는 동일합니다.
- `DELETE` : 클라이언트는 DELETE 요청을 사용하여 리소스를 제거합니다. DELETE 요청은 서버 상태를 변경할 수 있습니다. 하지만 사용자에게 적절한 인증이 없으면 요청은 실패합니다.## 1.3 예제 코드

다양한 개발 언어들은 REST API 호출을 위한 라이브러리를 제공하고 있습니다. 활용방법은 각 개발언어의 기술 문서들을 쉽게 검색하여 참고할 수 있습니다.

- 여기서는 C#과 python을 활용한 GET과 POST 메소드의 호출만 설명하도록 하겠습니다.

- IP 주소가 192.168.1.150인 Hi6 제어기에 대해 요청을 수행한다고 가정하겠습니다.
### 1.3.1 예제 코드 - C#

JSON parsing을 위한 라이브러리인 `Newtonsoft.Json`를 사용했습니다.
VisualStudio 프로젝트에 설치되어 있지 않다면, NuGet Package Manager로 설치하시기 바랍니다.

* [Newtonsoft.Json 라이선스 정보](https://github.com/JamesNK/Newtonsoft.Json/blob/master/LICENSE.md)

1) project 속성 열기
2) `Manage NuGet Packages...`
3) `Online/nuget.org`에서 `Json.NET (James Newton-King)`을 찾아 Install 수행.  
   (혹시, NuGet Package Manager의 버전이 낮아 설치가 안된다는 메시지가 나오면, 주 메뉴의 `TOOLS/Extensions and Updates...`를 선택 후 Updates에서 NuGet 업데이트를 수행하십시오.)

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

위 소스코드가 포함된 실행 가능한 C# WinForms 샘플 프로그램을 아래 Github 링크를 통해 확인하실 수 있습니다.
> 링크 : [https://github.com/hyundai-robotics/OpenAPI](https://github.com/hyundai-robotics/OpenAPI)### 1.3.2 예제 코드 - python

예제 코드는 크게 `a. 동기식 요청(blocking & 동기식)`방식과 `b. 비동기식 요청(non-blocking & 비동기식)` 두 가지 방식에 대해서 설명합니다.

||동기식|비동기식|
|:---|:---|:---|
|blocking|`a. 동기식 요청`||
|non-blocking||`b. 비동기식 요청`|

두 가지 방법의 차이점은 TP와 컨트롤러에 다음과 같은 심각한 결과를 초래할 수 있습니다.
1. UI 스레드에서 빈번한 동기 함수 호출로 인해 UI가 원활하게 실행되지 않고 정지될 수 있습니다(`Hanging 문제`).
2. 서버(컨트롤러) 측의 문제로 인해 응답을 받지 못하는 경우, 애플리케이션 UI가 정지될 수 있습니다(`Hanging 문제`).

따라서 실제 애플리케이션을 개발할 때에는 비동기식 요청 기반으로 작성하시기 바랍니다.
- Hi6 Open API 설명에 작성된 Python 스크립트 예시는 이해하기 쉽도록 동기적으로 작성되었으니 유의하시기 바랍니다.

<br><br>

### a. 동기식 요청
동기식은 하나의 요청이 끝나고 응답이 올 때까지 다른 task 의 실행이 불가능한 blocking 상태의 요청 방식 입니다.  
python 에서 `동기식` HTTP 요청을 위해 많이 사용되는 라이브러리는 `requests` 입니다.  
`requests` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다.   	
```sh
$pip install requests
```
- 통신시 응답을 받지 못하거나 응답을 받는데 시간이 오래 걸리는 경우에는 hanging 문제가 발생할 가능성이 매우 높으니 주의 바랍니다.

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
<br><br>  

### b. 비동기식 요청
동기식 요청의 문제점을 보완한 방식으로, 요청 시 콜백 함수를 동작시켜 해당 콜백 함수에서 요청 사항을 처리하여 도중에 다른 task 가 실행 가능해집니다.  
작업 완료 순서를 보장하지 않는다는 점이 동기식과 차이가 있지만, 모든 요청이 거의 동시에 시작되므로 전체적인 응답 시간이 짧아집니다.  
python 은 `asyncio` 라는 비동기 프로그래밍 구현 용 빌트인 라이브러리를 제공하고 있습니다. 이를 통해 CPU 작업과 I/O를 병렬로 처리하게 해줍니다.  
`비동기식` HTTP 요청을 위해 많이 사용되는 라이브러리는 `aiohttp` 입니다.  
`aiohttp` 라이브러리가 없는 경우, 파이썬 패키지 매니저를 통해 설치할 수 있습니다.

```sh
$pip install aiohttp
```

```python
# async.py - 비동기식, 사용자 IO 출력 값 얻기와 설정하기
import asyncio
import aiohttp
import time

url = 'http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3}

async def set_value(session):
    val = 0x60
    req_body = {'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val': val}
    start_time = time.time()
    async with session.post(url + path, headers=head, json=req_body) as resp:
        pass
    end_time = time.time()
    print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def get_value(session):
    start_time = time.time()
    async with session.get(url + path, headers=head, params=query) as resp:
        resp_body = await resp.json()
    end_time = time.time()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def main():
    async with aiohttp.ClientSession() as session:
        await set_value(session)
        tasks = [get_value(session) for _ in range(5)]
        total_start_time = time.time()
        await asyncio.gather(*tasks)
        total_end_time = time.time()
        print(f"total request time : {total_end_time - total_start_time} seconds")

asyncio.run(main())
```
```bash
$python async.py
[post] 0x60 to fb2.do3 Time taken: 0.0018951892852783203 seconds
[get] 0x60 from fb2.do3 Time taken: 0.044029951095581055 seconds
[get] 0x60 from fb2.do3 Time taken: 0.0583953857421875 seconds 
[get] 0x60 from fb2.do3 Time taken: 0.05900430679321289 seconds
[get] 0x60 from fb2.do3 Time taken: 0.05900430679321289 seconds
[get] 0x60 from fb2.do3 Time taken: 0.05900430679321289 seconds
total request time : 0.060544490814208984 seconds
```## 1.4 코딩하지 않고 쉽게 API 호출 해보기

[앞선 예제 코드](../../1-intro/3-sample-code/README.md)처럼 client 어플리케이션을 개발하면서 Open API 를 사용하는 경우, 코딩을 따로 하지 않고도 손쉽게 API를 호출해 볼 수 있습니다.  
이러한 호출 과정을 통해서 요청이 제대로 동작했는지, 응답으로 어떠한 데이터가 반환되는지 확인 가능 합니다.  
이를 위한 방법은 여러가지가 있습니다. 해당 섹션에서는 대표적인 2가지를 다루고 있습니다.

<br>

### 1) `postman` 활용하기

`postman` 은 세계적으로 많이 사용되는 API 테스팅 플랫폼 입니다.  
`workspace` 기능을 통해 프로젝트 단위의 API 테스트와 history 추적이 가능하고 언어별 Code snippet, 직관적 ui 를 갖추고 있습니다.  
[1.4.1 Postman 에서 POST 요청하기](./1-postman.md)에서 간단한 사용법을 확인할 수 있습니다.


<br>


### 2) `웹 브라우저` 활용하기

간단한 `get` 요청은 웹 브라우저를 통해 간편하고 신속하게 확인할 수 있습니다.  
추가로 웹 브라우저의 확장 프로그램을 활용하여 `get` 요청과 다른 API 요청들을 직접 호출하고 결과를 볼 수 있습니다.  
[1.4.2 웹 브라우저에서 API 호출하기](./2-web-browser.md)에서 간단한 사용법을 확인할 수 있습니다.## 1.4.1 `Postman` 에서 `POST` 요청하기

해당 페이지에서는 `postman` 을 활용해서 REST API 의 `POST` 요청을 호출하고 결과를 확인합니다.  
추가로 간단한 UI 구성을 통해 사용법을 파악합니다.

<br>

### a. 주요 UI 구성

아래 그림을 통해 주요 UI 구성을 확인할 수 있습니다. <br>

<img src="../../_assets/01_postman_desc.png" height="460vh">

<blockquote>

(1) `+` 버튼을 통해 request 요청을 간단하게 생성할 수 있습니다. </br>
(2) `request` 요청에 대한 정보들을 입력하는 공간 입니다. </br>
(3) `response` 에 대한 정보들을 확인하는 공간입니다. </br>
(4) `request` url 이 적용되어 자동으로 생성된 언어별 `Code snippet`을 확인하는 공간입니다. </br>

</blockquote>

<br>

### b. POST 요청 시험하기

1. `Request Header` 작성 
	- Headers 탭에 아래의 Key-Value를 입력합니다.
  	- Content-Type 관련 ([postman](https://blog.postman.com/what-are-http-headers/#Content-type) 참조)
	<br><img src="../../_assets/02_postman_headers.png" height="130vh">

<br>

2. `Request Body` 작성 
	- API method 를 `POST` 로 선택하고 URL을 입력합니다.
	- Body 탭 클릭 후 요청하려는 `body-parameter`를 입력합니다. ([9.2.1 `task/cur_prog_cnt` - request body](../.././9-task/2-post/1-cur_prog_cnt.md) 참조)
	- Send를 클릭합니다.  
		<img src="../../_assets/03_postman_post.png" height="280vh">

<br>

3. `Response` 확인 및 `Code snippet` 참조
	- `request` 요청이 정상적으로 완료되면 아래 그림과 같이 `HTTP Status` 가 `200 OK`로 응답합니다. ([HTTP Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 참조)
	- 해당 url 이 적용된 언어별 `Code snippet` 또한 확인 가능합니다.  
	<img src="../../_assets/04_postman_post_result_check.png" height="500vh">  

		<blockquote>

		`(1) Response body` : `post` 에 대한 응답 결과 ([9.2.1 `task/cur_prog_cnt` - response body](../.././9-task/2-post/1-cur_prog_cnt.md) 참조)</br>
		`(2) Request` 에 대한 python `Code snippet`

		</blockquote>## 1.4.2 웹 브라우저에서 API 호출하기

### a. 간단한 `GET` 요청하기

`get` 요청은 웹 브라우저를 통해 보다 간편하고 신속하게 확인할 수 있습니다. 순서는 다음과 같습니다.
1. 웹 브라우저 엽니다.
2. 주소 창에 `get` 요청의 서버 측 url 을 입력합니다.
	- 서버 측 url 은 `http://<Hi6 제어기의 ip 주소>:<http 통신 포트>`로 시작되며 추출하려는 정보에 맞는 경로와 쿼리를 이어 적습니다.
	- ex) ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
3. 해당 url 의 페이지가 열리고 아래와 같이 응답이 출력됩니다.
	```json
	{
		"_type" : "JObject",
		"val" : -99
	}
	```

<br>

### b. `확장 프로그램`으로 API 호출하기  
크롬 또는 엣지 브라우저를 사용하는 경우, 크롬 확장 프로그램을 통해 `get` 요청 이외의 api 들을 테스트할 수 있습니다.  
하기 확장 프로그램은 세계적으로 여러 개발자들이 사용하는 API 테스터 입니다.
- 크롬 확장 프로그램 : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)  

해당 프로그램을 통해 `postman` 처럼 다양한 API 들에 대해서 간편하게 호출을 해볼 수 있습니다.

<img src="../../_assets/06_Talend_api_tester.png" height="850vh">

<blockquote>

`(1) Requests/Senarios` : 하나의 API 에 대해서 호출을 테스트할지, 여러 API 들로 시나리오를 작성하여 순차적으로 테스트할 지 설정할 수 있습니다.<br>
`(2) Request` : 요청할 내용을 입력합니다.  
`(3) Response` : 요청에 대한 응답을 확인할 수 있습니다.  
`(4) History` : 요청 이력을 출력합니다.  
`(5) History 탭` : 열었다 닫았다 할 수 있는 `(4)`의 요청 이력 리스트보다 많은 양의 이력이 확인 가능한 탭입니다.

</blockquote>## 2. version

- 현재 api 의 버전 또는 로봇제어기의 시스템 버전을 확인합니다.## 2.1 version/get

- 현재 api 의 버전 또는 로봇제어기의 시스템 버전 관련 정보에 대하여 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 2.1.1 api_ver

### 설명

- GET : Open API version 번호를 얻습니다.

### path-parameter

```python
GET /api_ver
```

### response-body

- Open API version 번호
- 초기 Hi6 Open API 는 `version 5`를 기준으로 작성된 문서입니다. 

### 사용 예

```python
request url:
GET /api_ver

response-body:
5
```

Python Script 예시

```python
import requests

def get_api_ver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/api_ver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_api_ver())
```
```sh
$python test.py
5
```## 2.1.2 sysver

### 설명

- GET : 로봇제어기 시스템의 소프트웨어 버전을 얻습니다.

### path-parameter

```python
GET /versions/sysver
```

### response-body

modules : 모듈 버전 정보의 배열
  - 모듈 버전 정보 :
    - `name` : 모듈명
		|모듈명|설명|
		|---:|:---|
		|com|로봇 제어기|
		|tp|티칭 팬던트|
    - `ver` : 버전번호
    - `build-date` : 빌드 날짜
    - `build-time` : 빌드 시간
    - `commit-id` : 소스코드의 커밋 ID

### 사용 예

```python
request url:
GET /versions/sysver

response-body:
{
    "modules" : [
        {
            "build-date": ...
            "build-time": ...
                 ...
            "ver": ...
        }
    ] 
}
```

Python Script 예시

```python
import requests

def get_sysver() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/versions/sysver'
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(get_sysver())
```
```sh
$python test.py
{'modules': [{'build-date': 'Jan 00 2000', 'build-time': '00:00:00' ...
```# 3. project

- 조건설정, 프로젝트 정보, job 파일 정보들을 읽습니다.
- 업데이트된 job 파일들을 새로이 로드하거나 특정 job 파일들을 삭제할 수 있습니다.## 3.1 project/get

- 조건설정, 프로젝트 정보, job 파일 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 3.1.1 `rgen`

### 설명

`rgen` (remote general status)

- `GET` : 제어기에 설정된 일반적인 정보들을 읽습니다.

### path-parameter

```python
GET /project/rgen
```

### response-body

#### 1) 모드
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : 수동 <br> `1` : 수동, 시스템 설정 <br>`3` : 자동, 1-cycle <br> `4` : 자동, 연속 (cycle 반복)|`int`|수동/자동 모드|
|`enable_state`|`0번` 바이트(`LSB`) : 모터 ON (0: On / 1: Off / 2: Busy) <br> `1번` 바이트 : TP Enable (deadman) 스위치 (0: OFF / 1: ON)<br>`2번` 바이트 : 머신 Lock (0: OFF / 1: ON)<br>`3번` 바이트 : 건(gun) Lock (0: OFF / 1: ON)<br>`4번` 바이트 : 건(gun) (0: OFF / 1: ON)|`int`||
|`is_playback`|`0` : 정지 중 <br>`1` : 재생 중|`int`||
|`is_remote_mode`|`0`: False <br> `1`: True|`int`|원격(Remote) 모드 여부|
|`is_ext_start`|`0`: False <br> `1`: True|`int`|외부 기동 여부|
|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|외부 프로그램 선택 여부|

<br>

#### 2) current 프로그램 카운터
수동모드나 자동모드에서 티치펜던트 JOB 패널의 막대형 커서가 위치한 지점입니다. 현재 실행되고 있는 명령문, 혹은 편집의 대상 위치입니다.
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|current 프로그램 번호|
|`cur_step_no`|`int`|current 스텝 번호|
|`cur_func_no`|`int`|current 펑션 번호|

<br>

#### 3) moving 프로그램 카운터

재생 중 로봇이 이동하고 있는 목표 스텝입니다.
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|moving 프로그램 번호|
|`mov_step_no`|`int`|moving 스텝 번호|
|`mov_func_no`|`int`|moving 펑션 번호|

<br>

#### 4) 속도

|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|수동모드 조그 속도 레벨 (1~8)|
|`manual_spd_max`|`int`|수동모드 최대 속도 (mm/sec)|
|`auto_spd`|`int`|자동모드 재생 속도 (%)|
|`jog_inch_status`|`int`|조그 인칭 상태 (0:OFF/ 1:ON)|
|`step_execute_unit_status`|`int`|StepFWD의 실행단위 (run to)<br>0: Cmd (명령문)<br>1: Step (스텝)<br>2: End (end문까지)|
|`cont_path`|`int`|연속 모션 모드 (0~2)|

<br>

### 사용 예
Python Script 예시

```python
import requests

def get_is_remote_mode() -> bool:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/rgen'    
    
    response = requests.get(url = base_url + path_parameter).json()    

    print(f"is remote mode? {response['is_remote_mode']}")    
    
    return response['is_remote_mode']

get_is_remote_mode()
```
```sh
$python test.py
is remote mode? 0
```
## 3.1.2 `jobs_info`

### 설명

`jobs_info`

- `GET` : job 프로그램 관련 정보들을 받는 함수입니다.

### path-parameter

```python
GET /project/jobs_info
```

### response-body

- [job 파일 관련 정보](../../99-schema/jobs_info.md)
### 사용 예

<blockquote>

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
</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_jobs_info() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/jobs_info"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_jobs_info())
```
```sh
$python test.py
[{'_type': 'JObject', 'job_comment': '', 'fname': '0001.job', 'n_step': 0, 'n_aux_ax': 0, 'n_total_ax': 6}, 
{'_type': 'JObject', 'job_comment': '', 'fname': '0002.job', 'n_step': 9, 'n_aux_ax': -1, 'n_total_ax': -1}, 
{'_type': 'JObject', 'job_comment': '', 'fname': '0003.job', 'n_step': 0, 'n_aux_ax': -1, 'n_total_ax': -1}]
```## 3.1 project/post

- 조건설정, 프로젝트 정보, job 파일 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 3.2.1 `reload_updated_jobs`

### 설명

`reload_updated_jobs`

- `POST` : 작업 파일들을 갱신하는 요청을 보냅니다.
- FTP 로 job 파일을 제어기에 전송하는 경우, 해당 API 를 통해 reload 요청을 해야 전송된 job 파일이 메모리에 반영이 됩니다.

### path-parameter

```python
POST /project/reload_updated_jobs
```

### request-body

```json
{}
```

### 사용 예

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```

Python Script 예시

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.
```python
# test.py
import requests 

def post_reload_updated_jobs() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/reload_updated_jobs'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_reload_updated_jobs()}")
```
```sh
$python test.py
response: 200 
```
## 3.2.2 `delete_job`

### 설명

`delete_job`

- `POST` : 작업 파일을 제거하는 요청을 보냅니다.

### path-parameter

```python
POST /project/jobs/delete_job
```

### request-body

```json
{
  "fname": "0001.job"
}
```

### 사용 예

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
	"fname": "0001.job"
}
```

Python Script 예시

```python
# test.py
import requests 

def post_delete_job(file_name: str = "0001.job") -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/jobs/delete_job'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"fname": file_name}
 
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.status_code

print(f"response: {post_delete_job('0002.job')}")
```
```sh
$python test.py
response: 200 
```# 4. control

- 제어기(controller)의 설정값 적용 및 입출력 값을 처리합니다.
- 시스템 입출력, 디지털 입출력, 조건설정, 사용자 좌표계 관련 정보를 다룹니다.

<br>## 4.1 control/get

- 제어기의 설정 정보, 입출력 값에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 4.1.1 `op_cnd`

### 설명

`op_cnd` (operation condition)

- `GET` : 조건설정 값을 얻습니다.

### path-parameter

```python
GET /project/control/op_cnd
```

### response-body

- [조건설정 파라미터](../../99-schema/op_cnd.md)

<blockquote>

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
</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_operation_condition() -> dict:
    base_url       = "http://192.168.1.150:8888"
    path_parameter = "/project/control/op_cnd"

    response = requests.get(url=base_url + path_parameter).json()

    return response

print(get_operation_condition())
```
```sh
$python test.py
{'step_goback_max_spd': 130, 'playback_mode': 2, '_type': 'CondGrp', 'step_go_func_ex': 0, 'robot_lock': 1, 'playback_spd_rate': 80, 'intp_base': 1, 'ucrd_num': 19, 'path_recov_confirm': 0, 'func_reexe_on_trace': 2, 'plc_mode': 0}
```## 4.1.2 `ios/dio/{dio_val}`

### 설명

`dio` (digital input/output)

- `GET` : 사용자 IO 값을 얻습니다.

### path-parameter

```python
GET /project/control/ios/dio/{dio_val}
```

### path-variable

- `dio_val` :
  - `di_val` : 입력(di) 값을 얻습니다.
  - `do_val` : 출력(do) 값을 얻습니다.

### query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)

### 사용 예

- fb2.dob3 값 얻기. (결과값 : 0b11001000 = 0xc8 = -56)

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
	"_type" : "JObject",
    "val" : -56,
}
```

Python Script 예시

```python
# test.py
import requests

def get_dio_val() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/control/ios/dio/do_val'
    query_parameter = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3 }
    
    response = requests.get(url=base_url + path_parameter, params=query_parameter).json()

    return response

print(get_dio_val())
```
```sh
$python test.py
{'_type': 'JObject', 'val': -56}
```## 4.1.3 `ios/sio/{sio_val}`

### 설명

`sio` (system input/output)

- `GET` : 시스템 IO 값을 얻습니다.

### path-parameter

```python
GET /project/control/ios/sio/{sio_val}
```

### path-variable

- `sio_val` :
  - `si_val` : 입력(si) 값을 얻습니다.
  - `so_val` : 출력(so) 값을 얻습니다.

### query-parameter

- `type` : io 값의 타입
  - si or so : bit
  - sib or sob : signed-byte
  - siw or sow : signed-word (2byte)
  - sil or sol : signed-dword (4yte)
  - sif or sof : float
- `sig_no` : 신호 인덱스 (0~)


### 사용 예

- sib1 값 얻기. (결과값 : 0b00000010 = 0x02 = 2)

```python
request url:
GET /project/control/ios/sio/si_val?type=sib&sig_no=1

response-body:
{
	"_type" : "JObject",
    "val" : 2,
}
```

Python Script 예시

```python
# test.py
import requests

def get_sio_val() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/control/ios/sio/so_val'
    query_parameter = { 'type': 'sob', 'sig_no': 3 }
    
    response = requests.get(url = base_url + path_parameter, params = query_parameter).json()

    return response

print(get_sio_val())
```
```sh
$python test.py
{'_type': 'JObject', 'val': 0}
```## 4.1.4 `ucss/ucs_nos`

### 설명

`ucss/ucs_nos` (user coordinate system numbers)

- `GET` : 현재 사용 중인 사용자 좌표계들을 리스트로 얻습니다.
- `시스템 > 2: 제어 파라미터 > 6: 좌표계 등록` 을 통해 등록한 사용자 좌표계 리스트를 출력합니다.

### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

### 사용 예

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
{
	"_type" : "JObject",
    "val" : [1],
}
```

Python Script 예시

```python
# test.py
import requests

def get_ucs_nos():
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ucss/ucs_nos'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(f"{get_ucs_nos()}")
```
```sh
$python test.py
[1, 2, 3]
```## 4.2 control/post

- 제어기의 설정 정보, 입출력 값에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 4.2.1 `ios/dio/{do_val}`

### 설명

`do` (digital output)

- `POST` : 디지털 출력을 변경합니다.

### path-parameter

```python
POST /project/control/ios/dio/do_val
```

### request-body

```json
{
  "type": "do",
  "blk_no": 1,
  "sig_no": 1,
  "val": 1
}
```


### query-parameter

- `type` : io 값의 타입
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : 블럭 번호 (0~9)
- `sig_no` : 신호 인덱스 (0~)
- `val` : 변경하고자 하는 설정값


### 사용 예

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

Python Script 예시

- 응답되는 HTTP 상태 코드는 [이곳](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)을 참조해주십시오.
```python
# test.py
import requests 

def post_do_val() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ios/dio/do_val'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"type": "dob", "blk_no": 2, "sig_no": 3,"val": -99}

    response = requests.post(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {post_do_val()}")
```
```sh
$python test.py
response: 200 
```## 4.3 control/put

- 제어기의 설정 정보, 입출력 값에 대한 PUT 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 4.3.1 `op_cnd`

### 설명

`op_cnd` (operation condition)

- `PUT` : 로봇의 조건설정 값을 변경합니다.
- TP 에서 조건 설정 창을 열고 해당 메서드를 요청한 경우, 창을 닫았다 다시 열어야 값이 반영됩니다.

### path-parameter

```python
PUT /project/control/op_cnd
```

### request-body

- [조건설정 파라미터](../../99-schema/op_cnd.md)


### 사용 예

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}
```

Python Script 예시

```python
# test.py
import requests 

def put_op_cnd() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/op_cnd'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = { 
                          "playback_mode": 1,
                          "step_goback_max_spd": 130,
                          "ucrd_num": 2
                     }

    response = requests.put(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {put_op_cnd()}")
```
```sh
$python test.py
response: 200 
```# 5. robot

- 로봇과 툴 데이터에 대한 원격 제어와 모니터링을 확인할 수 있습니다.
- 모터 on/off, 로봇 자세, 툴, 조그 좌표계 등을 다루고 있습니다.
## 5.1 robot/get

- 로봇과 툴 데이터에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 5.1.1 `motor_on_state`

### 설명

`motor_on_state`

- `GET` : 모터 온 상태를 얻습니다.

### path-parameter

```python
GET /project/robot/motor_on_state
```

### response-body

- val :
  - `0` : on
  - `1` : busy (상태 전환 중)
  - `2` : off

### 사용 예
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
	"_type" : "JObject",
	"val" : 1
}
```

Python Script 예시

```python
# test.py
import requests

def get_motor_on_state() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on_state'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(f"Motor On status: {get_motor_on_state()['val']}")
```
```sh
$python test.py
Motor On status: 1
```## 5.1.2 `po_cur`

### 설명

`po_cur` (pose current)

- `GET` : 현재 로봇이 취하고 있는 pose(자세)를 얻습니다.

### path-parameter

```python
GET /project/robot/po_cur
```

### query-parameter

- `task_no` : task 번호 (0~7).
  - 미지정 : task 0으로 적용됨.
  - &gt;=0 : mechinfo 미지정 시, task의 현재 mechinfo가 적용됨.
- `crd` :  
  - 미지정 : tcp, axis, encoder를 모두 얻음.
  - <0 : 현재 기록 좌표계를 따름.
  - &gt;=0 : [좌표계](../../99-schema/crdsys.md)
- `ucrd_no` : 사용자 좌표계 번호 (crd가 user일 때만 지정함.)
- `mechinfo` : [메커니즘 정보](../../99-schema/mechinfo.md)

### response-body

- [포즈 정보](../../99-schema/pose.md)


### 사용 예

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

Python Script 예시

```python
# test.py
import requests

def get_base_coordinate() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/po_cur'
    query_parameter = {'crd': 0, 'mechinfo': 1}

    response = requests.get(url = base_url + path_parameter, params = query_parameter).json()

    return response

print(get_base_coordinate())
```
```sh
$python test.py
{'nsync': 0, '_type': 'Pose', 'rx': 0.0, 'x': 1067.366, 'ry': 73.248, 'y': -12.859, 'rz': -0.69, 'z': 1609.909, 'mechinfo': 1, 'crd': 'base', 'j1': 0.0, 'j2': 0.0, 'j3': 0.0, 'j4': 0.0, 'j5': 0.0, 'j6': 0.0}
```## 5.1.3 `cur_tool_data`

### 설명

`cur_tool_data`

- `GET` : 로봇의 현재 툴 데이터 얻기.

### path-parameter

```python
GET /project/robot/cur_tool_data
```

### response-body

- val : [툴 데이터](../../99-schema/tool_data.md)

### 사용 예

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

Python Script 예시

```python
# test.py
import requests

def get_cur_tool_data() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/cur_tool_data'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(get_cur_tool_data())
```
```sh
$python test.py
{'_type': 'Tool', 'x': 0.0, 'rx': 0.0, 'y': 0.0, 'ry': 0.0, 'z': 0.0, 'rz': 0.0, 'cy': 0.0, 'mass': 20.0, 'cx': 100.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'bias_2': 0.0, 'mass_esti': 20.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```## 5.1.4 `tools`

### 설명

`tools`

- `GET` : 로봇의 모든 툴 정보 얻기. T0~T31까지의 툴 중 존재하는 툴만 얻습니다.

### path-parameter

```python
GET /project/robot/tools
```

### response-body

- t_0 : [툴 데이터](../../99-schema/tool_data.md)
- t_1 : 툴 데이터
- t_2 : 툴 데이터  
...
- t_31 : 툴 데이터

### 사용 예

툴 0과 툴 31만 존재하는 시스템의 사례.

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

Python Script 예시

```python
# test.py
import requests

def get_tools_data() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/tools'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(get_tools_data())
```
```sh
$python test.py
{'_type': 'Tools', 't_31': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_0': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0, 'load_rate': {'_type': 'JObject', 'high_load_mode': -11, 'moment_rate': 0, 'inertia_rate': 0, 'mass_rate': 0}}, 't_1': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_15': {'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}}
```## 5.1.5 `tools/t_{number}`

### 설명

`tools/t_{number}`

- GET : 특정 툴의 설정값 정보를 받는 함수입니다.

### path-parameter

```python
GET /project/robot/tools/t_{number}
```

### response-body

- [툴 데이터](../../99-schema/tool_data.md)

### 사용 예

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
  "_type" : "Tool",
	"x" : 0.0,
	"y" : 0.0,
	"z" : 0.0,
	"rx" : 0.0,
	"ry" : 0.0,
	"rz" : 0.0,
	 ...
}
```

Python Script 예시

```python
# test.py
import requests

def get_tool1_data() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/robot/tools/t_1'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(get_tool1_data())
```
```sh
$python test.py
{'_type': 'Tool', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```## 5.2 robot/post

- 로봇과 툴 데이터에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 5.2.1 `motor_on / motor_off`

### 설명

- POST : 모터 ON과 모터 OFF를 수행합니다.

### path-parameter

```python
POST /project/robot/motor_on
POST /project/robot/motor_off
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### 사용 예

```python
POST /project/robot/motor_off

request-body:
{}
```

Python Script 예시

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

def post_motor_off() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_off'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
print(f"Motor-OFF response: {post_motor_off()}")
```
```sh
$python test.py
Motor-ON  response: 200
Motor-OFF response: 200
```## 5.2.2 `start / stop`

### 설명

- POST : 로봇 기동(start)과 로봇 정지(stop)를 수행합니다.

### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### 사용 예

```python
POST /project/robot/motor_off

request-body: 
{}
```

Python Script 예시

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # 자동모드 및 모터 온 설정 필요
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

def post_stop() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/stop'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Start response: {post_start()}")
print(f"Stop  response: {post_stop()}")
```
```sh
$python test.py
Start response: 200
Stop  response: 200
```## 5.2.3 `tool_no`

### 설명

- POST : 현재 툴 번호를 설정합니다.

### path-parameter

```python
POST /project/robot/tool_no
```

### request-body

- `val` : 툴 번호
  - `로봇 툴` : `0` ~ `31`
  - `정치 툴` : `0` ~ `3`

### response-body

```json
{
    "_type": "JObject"
}
```

### 사용 예

```json
POST /project/robot/tool_no

request-body
{
  "val": 1
}
```

Python Script 예시

```python
import requests

def post_tool_no(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/tool_no'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    # 자동모드 및 모터 온 설정 필요
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_tool_no(1)}")
```
```sh
$python test.py
response: 200
```## 5.2.4 `crd_sys`

### 설명

- POST : 현재 조그(jog) 좌표계를 설정합니다.

### path-parameter

```python
POST /project/robot/crd_sys
```

### request-body

- [좌표계](../../99-schema/crdsys.md)

### response-body

```json
{
  "_type": "JObject",
  "cur_crd": 1,
  "ucrd_no": 1
}
```


### 사용 예

```json
POST /project/robot/crd_sys

request-body
{
  "val": 1
}
```

Python Script 예시

```python
import requests

def post_crd_sys(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/crd_sys'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_crd_sys(1)}")
```
```sh
$python test.py
response: 200
```# 6. I/O PLC

- 내장 PLC(built-in plc)의 입출력 값을 읽어오거나 설정합니다.## 6.1 io_plc/get

- 내장 PLC(built-in plc)의 입출력 값에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 6.1.1 `relay values`

### 설명

- `GET` : relay 값을 객체.타입 전체에 대해 얻습니다.

### path-parameter

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

### path-variable

[릴레이명](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/korean/3-relay/2-relay-expression) (소문자 표기)

* (`di`, `do`, `x`, `y`에는 `{obj_type}{obj_idx}_`를 지정해야 합니다. 나머지 `relay_type`에는 지정하지 않습니다.)

- `obj_type` : 객체 타입 (`fb`, `fn`)

- `obj_idx` : 객체 인덱스 (`fb`: `0` ~ `9`, `fn`: `0` ~ `63`)

- `relay_type` : `di`, `do`, `x` , `y` , `m` , `s` , `r`, `k`

	

### query-parameter

- `st` : 시작 byte index (default: 0)
- `len` : dword 개수 (default: 8)


### 사용 예

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

Python Script 예제

```python
# test.py
import requests

def get_relay_value() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/m/val_s32'
    query_parameter = {"st": "32", "len": "4"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(f"{get_relay_value()}")
```
```sh
$python test.py
[0, 0, 0, 0]
```## 6.2 io_plc/post

- 내장 PLC(built-in plc)의 입출력 값에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 6.2.1 `set_relay_value`

### 설명
`set_relay_value`

- `POST` : relay 값 설정합니다.

### path-parameter

```python
POST /project/plc/set_relay_value
```

### request-parameter

- `name` : 설정하려는 릴레이명을 [표기법](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/korean/3-relay/2-relay-expression)에 맞춰 입력합니다.
- `value` : 상기 표기법의 `data-type` 에 유의하여 설정하려는 값을 입력합니다.
```json
{
	"name": "fb3.dof14",
	"value": "2.718"
}
```

### 사용 예

```json
request url:
POST /project/plc/set_relay_value

request-body:
{
	"name": "fb1.do0",
	"value": "1"
}
```

Python Script 예제

```python
# test.py
import requests

def get_relay_value() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/fb1_do/val_s32'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

def post_set_relay_value() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/plc/set_relay_value'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"name": "fb1.do0", "value": 1}
 
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.status_code

print(f"{get_relay_value()}")
print(f"response: {post_set_relay_value()}")
print(f"{get_relay_value()}")
```
```sh
$python test.py
[0, 0, 0, 0, 0, 0, 0, 0]
response: 200
[1, 0, 0, 0, 0, 0, 0, 0]
```# 7.1 event-log

- 제어기에 기록되는 에러, 경고, 실행이력 등을 출력합니다.## 7.1 log_manager/get

- 제어기에 기록되는 에러, 경고, 실행이력에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 7.1.1 search

### 설명

`search`

- `GET` : 지정한 필터 조건으로 이벤트 이력(event log)를 열람합니다.  

### path-parameter

```python
GET /logManager/search
```

### query-parameter

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

### response-body

- `id` : 이벤트 ID (event ID)
- `ts` : timestamp
- `cat` : 이벤트 범주 (event category)
- `code` : 이벤트 코드번호
- `aux` : 이벤트 보조정보 (event auxiliary info.). 최대 280자입니다.
  - 에러와 경고, 기동/정지의 경우에는 스냅샷(snapshot) 정보를 담습니다.

```json
{ "id" : 19964, "ts" : "2023/11/20 15:53:11.275", "cat" : "E", "code" : "11,0,0", "aux" : "{ 'pc' : '20/3/1', 'j1' : 18.525, 'j2' : 105.000, 'j3' : -2.577, 'j4' : -14.432, 'j5' : -0.776, 'j6' : 0.314, 'sin' : '00 01 00 00 00 00 00 00', 'sout' : '05 08 06 00 00 00 00 01', 'din' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0', 'dout' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0' }" }
{ "id" : 18314, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(    976)Power saving = on " }
{ "id" : 18313, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(=Stamp=)[2023/11/20 15:05:33](+299996445us) " }
{ "id" : 18312, "ts" : "2023/11/20 15:05:33.787", "cat" : "N", "code" : "5", "aux" : "{ 'pc' : '20/3/1' }" }
{ "id" : 18267, "ts" : "2023/11/20 15:00:33.791", "cat" : "H", "code" : "hist", "aux" : "(   2001)    .end ;(P20/S3/F1) " }
{ "id" : 18266, "ts" : "2023/11/20 15:00:33.789", "cat" : "H", "code" : "hist", "aux" : "( 738785)S3  .move P,spd=500mm/sec,accu=4,tool=0 " }
```

### 사용 예

<blockquote>

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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_log_search() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/logManager/search'
    query_parameter = { 
                        'cat_p':  "P,O", 
                        'id_max': "24256", 
                        'id_min': "24251" 
                      }
    
    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    return response.text

print(get_log_search())
```
```sh
$python test.py
{ "id" : 24256, "ts" : "2023/11/28 16:53:23.450", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
{ "id" : 24255, "ts" : "2023/11/28 16:53:23.045", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
{ "id" : 24254, "ts" : "2023/11/28 16:53:13.695", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
{ "id" : 24253, "ts" : "2023/11/28 16:53:13.202", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
{ "id" : 24252, "ts" : "2023/11/28 16:53:13.036", "cat" : "P", "code" : "fb7.dil", "aux" : "00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000" }
{ "id" : 24251, "ts" : "2023/11/28 16:53:13.036", "cat" : "P", "code" : "fb7.dol", "aux" : "00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000" }
```# 8. file_manager

- 제어기의 파일 정보를 읽어오거나, 파일 이름 변경, 파일 전송 기능을 다룹니다.
- 디렉토리 존재여부를 확인하거나, 생성 및 삭제를 하는 기능 또한 다룹니다.## 8.1 file_manager/get

- 제어기의 파일 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 8.1.1 `files`

### 설명

`files`

- `GET` : 제어기로부터 파일 내용을 응답 받습니다.

### path-parameter

```python
GET /file_manager/files
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 가져올 파일 이름

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|파일 내용 반환|
|`404 Not Found`| 파일 없을 때 에러 상태 코드 반환|


### 사용 예

<blockquote>

```text
hi6
`-- project
    |-- jobs
    |   `-- 0001.job   <- target
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- hi6_proj.json
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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def print_file_contents() -> None:
    base_url	    = "http://192.168.1.150:8888"
    path_parameter  = "/file_manager/files"
    query_parameter = {"pathname": "project/jobs/0001.job"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)
	
    print(f'response: {response.status_code}')
    print(response.text)

print_file_contents()
```
```sh
$python test.py
response: 200
Hyundai Robot Job File; { version: 2.0, mech_type: "576(HH020-03)", total_axis: 6, aux_axis: 0 }
     Pose P1 =po1 = Pose(10, 90, 0, 0, -30, 0, -1240.8)
     Pose P2
     Pose P3
     Pose P4
S1   move P,tg=po1,spd=100%,accu=0,tool=1
S2   move P,tg=po1,spd=100%,accu=0,tool=1
S3   move P,tg=po1,spd=100%,accu=0,tool=1
S4   move P,tg=po1,spd=100%,accu=0,tool=1
     end
```## 8.1.2 `file_info`

### 설명

`file_info`

- `GET` : 파일 경로를 기반으로 해당 파일에 대한 정보를 반환합니다.

### path-parameter

```python
GET /file_manager/file_info
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

### response-body

- [파일 정보](../../99-schema/file_info.md)
- 파일이 없을 시 `404 Not Found` 

### 사용 예

<blockquote>

```text
hi6
`-- project
    |-- jobs
    |   `-- 0001.job <- target 
    |-- lads
    |-- log
    |-- vars
    |-- ...
    `-- hi6_proj.json
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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def get_file_info() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/file_manager/file_info"
    query_parameter  = {"pathname": "project/hi6_proj.json"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(get_file_info())
```
```sh
$python test.py
{'mday': 31, 'sec': 40, 'fname': 'hi6_proj.json', 'wday': 2, 'size': 130551, 'year': 2023, 'hour': 7, 'readonly': False, 'month': 10, 'is_dir': False, 'min': 57}
```## 8.1.3 `file_list`

### 설명

`file_list`

- `GET` : 파일 및 디렉토리 리스트를 반환합니다.

### path-parameter

```python
GET /file_manager/file_list
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|description|
|:---|:---|
|`path`|확인하려는 대상 폴더 경로|
|`incl_file`|리스트 출력 시 파일 포함 여부|
|`incl_dir`|리스트 출력 시 디렉토리 포함 여부|


### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|[파일 정보](../../99-schema/file_info.md) `리스트`를 반환|
|`404 Not Found`| 파일 없을 때 반환|


### 사용 예

<blockquote>

```text
hi6
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
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
		"fname": "hi6_proj.json",
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
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def print_file_list() -> None:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/file_manager/file_list"
    query_parameter = {"incl_file": "true", "incl_dir": "true", "path": "project"}

    response = requests.get(url=base_url + path_parameter, params=query_parameter)

    for x in response.json()[:3]:
        print(x)

print_file_list()
```
```sh
$python final_test.py 
{'mday': 20, 'sec': 8, 'fname': 'jobs', 'wday': 1, 'size': 8192, 'year': 2023, 'hour': 21, 'readonly': False, 'month': 11, 'is_dir': True, 'min': 50}
{'mday': 1, 'sec': 50, 'fname': 'vars', 'wday': 3, 'size': 8192, 'year': 2023, 'hour': 12, 'readonly': False, 'month': 11, 'is_dir': True, 'min': 29}
{'mday': 17, 'sec': 10, 'fname': 'lads', 'wday': 4, 'size': 8192, 'year': 2023, 'hour': 13, 'readonly': False, 'month': 8, 'is_dir': True, 'min': 47}
```## 8.1.4 `file_exist`

### 설명

`file_exist`

- `GET` : 타겟 파일의 존재 여부를 반환합니다.

### path-parameter

```python
GET /file_manager/file_exist
```

### query-parameter

query-parameter 를 반드시 입력해야합니다.  

```text
?pathname=project/jobs/0001.job
```
- `pathname` : 타겟 파일 경로

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|`true` (파일 존재)|
|`200 OK`|`false` (파일 없음)|


### 사용 예

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```  

```text
hi6
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def is_file_exist() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/file_exist'
    query_parameter = {'pathname': 'project/jobs/0001.job'}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.text

print(is_file_exist())
```
```sh
$python test.py
true
```## 8.2 file_manager/post

- 제어기의 파일 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 8.2.1 `rename_file`

### 설명

`rename_file`

- `POST` : 타겟 파일의 파일 이름을 변경합니다.

### path-parameter

```python
POST /file_manager/rename_file
```

### request-body

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : 변경 전 파일 경로
- `pathname_to` : 변경 후 파일 경로

### response-body

|HTTP Status|description|
|:---|:---|
|`200`| 이름 변경 완료 |
|`400`| 변경하려는 타겟 파일이 존재하지 않음 |


### 사용 예

<blockquote>

```python
request url:
POST /file_manager/rename_file

request-body: 
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
```
hi6
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def rename_file():
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/rename_file'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = { "pathname_from" : "project/jobs/0001.job", 
                        "pathname_to"   : "project/jobs/4321.job" }

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {rename_file()}")
```
```sh
$python test.py
response: 200
```## 8.2.2 `mkdir`

### 설명

`mkdir`

- `POST` : 타겟 경로에 디렉토리를 생성합니다.

### path-parameter

```python
GET /file_manager/mkdir
```

### request-body

|key|value|description|
|:---|:---|:---|
|`path`|`str`|디렉토리를 생성할 위치|

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| 타겟 위치에 디렉토리 생성 완료 |
|`500 Internal Server Error`| 타겟 위치에 디렉토리 이름이 중복되는 경우 |


### 사용 예

<blockquote>

```python
request url:
GET /file_manager/mkdir

request-body: 
{
	"path" : "project/jobs/special"
}
```

```
hi6
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- hi6_proj.json
```


</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_mkdir() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/mkdir'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body            = {'path': "project/jobs/special7"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {post_mkdir()}")
```
```sh
$python test.py
response: 200
```## 8.2.3 `files`

### 설명

`files`

- `POST` : 타겟 경로에 파일을 전송합니다.

### path-parameter

```python
POST /file_manager/files/{target_filepath}
```

### path-variable

- `target_filepath` : 확장자를 포함한 타겟 파일 경로

### request-body

- binary 형식의 파일
- `Content-Type` 은 `application/octet-stream` 이어야합니다.

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| 전송 완료 |


### 사용 예

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- hi6_proj.json
```

```python
request url:
POST /file_manager/files/project/jobs/test.job
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_file_transfer() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    path_value      = '/project/jobs/test.job' # target

    target_file     = base_url + path_parameter + path_value
    source_file     = 'D:\\temp\\test.job' # source (path for WindowOS)

    with open(source_file, 'rb') as file:
        response = requests.post(url=target_file, 
                                 data=file, 
                                 headers={'Content-Type': 'application/octet-stream'})

    return response.status_code

print(f"response: {post_file_transfer()}")
```
```sh
$python test.py
response: 200
```## 8.3 file_manager/delete

- 제어기의 파일 정보에 대한 DELETE 요청을 보냅니다.## 8.3.1 `files`

### 설명

`files`

- `DELETE` : 타겟 파일 또는 디렉토리를 삭제합니다.

### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

### response-body
|HTTP Status|description|
|:---|:---|
|`200 OK`| 타겟 삭제 완료, 타겟이 없어도 200 반환됨 |


### 사용 예

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```  

```text
hi6
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python Script 예시

```python
# test.py
import requests

def delete_file() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    target_file     = '/project/jobs/test.job'

    response = requests.delete(url = base_url + path_parameter + target_file)

    return response.status_code

print(f"response: {delete_file()}")
```
```sh
$python test.py
response: 200
```# 9.task

- 태스크와 관련된 내용들을 다룹니다.
- 특정 태스크나 전체 태스크에 대해서 리셋을 할 수 있습니다.
- 현재 태스크의 지역 또는 전역 변수에 대해서 값을 읽어오거나 새로운 변수를 선언할 수 있습니다.
- 태스크 실행 중 특정 작업 흐름(ex. wait)에 대해서 특정 조치(ex. release)를 취할 수 있습니다.## 9.1 task/get

- 태스크와 관련된 정보에 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 9.2 task/post

- 태스크와 관련된 정보에 대한 POST 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 9.2.1 `task/cur_prog_cnt`

### 설명

`cur_prog_cnt` (current program counter)

- `POST` : 태스크의 현재 프로그램 카운터를 설정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

### request-body

- [cur_prog_cnt 요청 파라미터](../.././99-schema/cur_prog_cnt.md)

### response-body

- [cur_prog_cnt 응답 파라미터](../.././99-schema/cur_prog_cnt.md)

### 사용 예

```python
request url:
POST /project/context/tasks[0]/cur_prog_cnt

request-body:
{
    "pno":-1,
    "sno":-1,
    "fno":-1,
    "ext_sel":0
}
```

Python Script 예시

```python
import requests

def post_cur_prog_cnt() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/cur_prog_cnt'
    headers        = { 'Content-Type': 'application/json; charset=utf-8' }
    body           = {"pno":-1, "sno":-1, "fno":-1, "ext_sel":0 }

    response = requests.request("POST", base_url + path_parameter, headers=headers, json=body)

    return response.json()

print(post_cur_prog_cnt())
```
```sh
$python python test.py
{'_type': 'JObject', 'sno_new': 0, 'fno_new': 2, 'ln_new': 2, 'ofs_moved': 0}
```## 9.2.2 `task/reset`

### 설명

- `POST` : 태스크에 대해 리셋을 수행합니다. (R.. 0 ENTER 와 같은 동작)

### path-parameter

```python
# reset all the tasks
POST /project/context/tasks/reset 

# reset the selected task
POST /project/context/tasks[{task index}]/reset 
```

### request-body

```json
{}
```

### 사용 예

0번 태스크 리셋 하기.

```python
request url:
GET /project/context/tasks[0]/reset
```

Python Script

```python
import requests

def post_task_reset() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/reset'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_task_reset()}")
```
```sh
$python test.py
response: 200
```## 9.2.4 `assign_var_expr`

### 설명

`assign_var_expr`

- `POST` : 현재 태스크 구문의 변수를 재지정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

### request-body

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

### 사용 예

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

상기 job 파일을 수행하여 태스크 상 지역 변수 a 가 선언된 상태일 경우

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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

def assign_var_expr(var_name: str, scope = None, expression: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_expr"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"name": f"{var_name}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"before: {post_read_var('a', 'local')}")
print(f"response: {assign_var_expr('a', 'local', '465 + 312')}")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
before: 1234
response: 200
after: 777   
```## 9.2.5 `assign_var_json`

### 설명

`assign_var_json`

- `POST` : 현재 태스크 구문의 변수를 재지정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

### request-body

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

### 사용 예

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

상기 job 파일을 수행하여 태스크 상 지역 변수 a 가 선언된 상태일 경우

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

</blockquote>

Python Script 예시

```python
# test.py
import requests

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

def assign_var_json(var_name: str, scope = None, var_json: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_json"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {
                         "name" : f"{var_name}",
                         "scope": f"{scope}",
                         "json" : f"{var_json}",
                         "save" : "true"
                       }

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"before: {post_read_var('a', 'local')}")
print(f"""response: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"after: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
before: 1234
response: 200
after: {'_type': 'JObject', 'test': 10}
```## 9.2.6 `release_wait`

### 설명

`release_wait`

- `POST` : 구문 정지해제
- 필요 조건 : TP > 시스템 > 1: 사용자 환경 > `wait(di/wi) 강제 해제` > `유효` 선택

### path-parameter

```python
POST /project/context/tasks[0]/release_wait
```

### request-body

```json
{}
```

### response-body

- `200` : 정상 동작
- `403` : 상기 필요 조건 불충족

### 사용 예

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python Script 예시

```python
import requests

def post_release_wait() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/release_wait'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_release_wait()}")
```
```sh
$python test.py
response: 200
```## 9.2.3 `set_cur_pc_idx`

### 설명

`set_cur_pc_idx`

- `POST` : 현재 커서를 index 라인에 위치 시키는 함수

### path-parameter

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

### request-body
```json
{
  "idx": 1
}
```

### 사용 예

<blockquote>

```python
request url:
POST /project/context/tasks[0]/set_cur_pc_idx

request-body
{
  "idx": 2
}
```

</blockquote>

Python Script

```python
# test.py
import requests

def set_cur_pc_idx() -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/set_cur_pc_idx"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"idx": 1}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"response: {set_cur_pc_idx()}")
```
```sh
$python test.py 
response 200 # + TP 상 커서 위치 변경 됨
```## 9.2.7 `solve_expr`

### 설명

`solve_expr`

- `POST` : 표현식(expression)을 풀어서 나오는 결과 값을 태스크의 지역 또는 전역 변수에 설정합니다.

### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

### request-body
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

### response-body

```json
13 // 현재 지정된 scope 안의 expr 값을 읽어옵니다.
```

### 사용 예

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

def post_read_var(var_name: str, scope = None) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/solve_expr'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"expr": f"{var_name}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
 
    return response.json()

print(f"{post_read_var('a', 'local')}")
print(f"{post_read_var('a', 'global')}")
print(f"{post_read_var('a + (-234)')}")
```
```sh
$python test.py 
1234
10
1000
```# 10. etc

- 시스템 버전, 이벤트 로그, 클럭 등을 다루고 있습니다.# 10.1 clock

- 제어기의 시스템 시간을 읽고 설정할 수 있습니다.## 10.1.1 clock/get

- 제어기 시스템 시간 대한 GET 요청을 보냅니다.
- API 별로 정확한 path-parameter, query-parameter 를 설정하여 응답을 받습니다.## 10.1.1.1 `date_time`

### 설명

`date_time`

- `GET` : 설정된 시스템 시간을 가져옵니다.

### response-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

### 사용 예

<blockquote>

```python
request url:
GET /clock/date_time

response-body:
{
	"_type": "JObject",
	"year": 2023,
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

def get_system_time() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'
	
    response = requests.get(url = base_url + path_parameter).json()

    t = f'[{response["mon"]}/{response["day"]}] {response["hour"]}:{response["min"]}'

    return t

print(get_system_time())
```
```sh
$python test.py
[11/20] 19:55
```## 10.1.2 clock/put

- 제어기 시스템 시간 대한 PUT 요청을 보냅니다.
- API 별로 정확한 request-body 를 작성해야합니다.## 10.1.2.1 `date_time`

### 설명

`date_time`

- `PUT` : 시스템 시간을 변경합니다.

### request-body

- [시스템 시간 정보](../../../99-schema/date_time.md)

### 사용 예

<blockquote>

```python
request url:
PUT /clock/date_time

request-body:
{
  "year": 2023,
  "mon": 10,
  "day": 30,
  "hour": 18,
  "min": 30,
  "sec": 0
}
```
</blockquote>

Python Script 예시

```python
# test.py
import requests

def put_system_time() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body 			= {"year": 2023, "mon": 11, "day": 20, "hour": 21, "min": 2, "sec": 0}
	
    response = requests.put(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {put_system_time()}")
```
```sh
$python test.py
response: 200
```# 7. 스키마 (schema)

이 챕터는 Open API에서 사용되는 각종 열거자(enumeration)와 구조체(structure)의 참조자료(reference)를 담고 있습니다.

## crdsys

### 설명

좌표계 (coordinate system)를 지정하는 열거자 (enumeration) 입니다.
|value|description|
|:---:|:---|
|`-1`|`다음` 좌표계|
|`0`|`축` 좌표계|
|`1`|`직교` 좌표계(=`로봇` 좌표계)|
|`2`|`사용자` 좌표계|
|`3`|`툴` 좌표계|
## cur_prog_cnt

### 설명
태스크의 현재 프로그램 카운터를 설정합니다.

### request body
|key|type|description|
|:---|:---|:---|
|`pno`|int|프로그램 번호 (-1이면 현재 번호 유지)|
|`sno`|int|스텝 번호 (-1이면 현재 번호 유지)|
|`fno`|int|펑션 번호 (-1이면 현재 번호 유지)|
|`ext_sel`|int|`0` : 내부선택(원격모드에선 금지됨) <br> `1` : 외부선택(원격모드에서만 허용됨)|

### response body
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|새로 이동한 스텝 번호|
|`fno_new`|int|새로 이동한 펑션 번호|
|`ln_new`|int|새로 이동한 라인번호 (프로그램 헤더가 0, 첫 명령문이 1)|## date_time

### 설명

시스템 시간 관련 정보를 나타냅니다.
|value|type|description|
|:---:|:---|:---|
|"year"|`int`|현재 시스템의 년도|
|"mon"|`int`|현재 시스템의 월|
|"day"|`int`|현재 시스템의 일|
|"hour"|`int`|현재 시스템의 시|
|"min"|`int`|현재 시스템의 분|
|"sec"|`int`|현재 시스템의 초|
## file_info

### 설명

파일 정보 요청 시 반환되는 파라미터 입니다.

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
## jobs_info

### 설명

job 파일 정보 파라미터 입니다.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|job 파일명|
|job_commnet|`str`|주석|
|n_step|`int`|스텝 개수|
|n_total_ax|`int`|총 축 수|
|n_aux_ax|`int`|부가축 수|
## mechinfo

### 설명

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

### 사용 예

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 메커니즘 M0, M1, M4를 지정합니다.
```
## op_cnd

### 설명
op_cnd (operation condition) : 로봇의 조건설정 값입니다.  
TP 에서 `조건설정` 버튼을 눌렀을 때 해당 값들을 확인할 수 있습니다.

<br>

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

<br>

### 예 (example)

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
## Pose

### 설명

포즈(pose) 데이터입니다.

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