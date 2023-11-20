# 1.2.1 예제 코드 - C#

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
