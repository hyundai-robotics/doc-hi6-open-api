# 1.2 예제 코드

다양한 개발 언어들은 REST API 호출을 위한 라이브러리를 제공하고 있습니다. 활용방법은 각 개발언어의 기술 문서들을 쉽게 검색하여 참고할 수 있습니다.

여기서는 C#과 python을 활용한 GET과 POST 메소드의 호출만 설명하도록 하겠습니다.

- IP 주소가 192.168.1.150인 Hi6 제어기에 대해 요청.

## C#
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
* json parser package 설치는 아래 링크 참조;  
[Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/)


## python
```python
# test_io_info.py - 사용자 IO 출력 값 얻기와 설정하기
import requests

uri='http://192.168.1.150:8888'

head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) fb2.do3 값 설정하기
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
print('[post]', hex(val), 'to fb2.do3')
resp = requests.post(uri + path, headers=head, json=req_body)

# (GET) fb2.do3 값 가져오기
resp = requests.get(uri+path, headers=head, params=query)
resp_body = resp.json()
print('[get]', hex(resp_body['val']), 'from fb2.do3')
```
```bash
$python test_io_info.py
[post] 0x79 to fb2.do3
[get] 0x79 from fb2.do3
```
