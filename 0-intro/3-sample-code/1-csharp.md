#### 0.3.1 示例代码 - C#

此文档使用 `Newtonsoft.Json`，这是一个用于 JSON 解析的库。  
如果它尚未安装在您的 Visual Studio 项目中，请使用 NuGet 包管理器进行安装。

* [Newtonsoft.Json 授权信息](https://github.com/JamesNK/Newtonsoft.Json/blob/master)

1) 打开 `project` 属性
2) `管理 NuGet 包...`
3) 在 `Online/nuget.org` 中找到 `Json.NET (James Newton-King)` 并安装它。  
   （如果您收到该消息，表示由于 NuGet 包管理器的版本过低而无法安装，请从主菜单中选择 `TOOLS/Extensions and Updates...` 并从更新中更新 NuGet。）

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
request.Timeout = 5 * 1000; // 5 秒

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

您可以通过以下 GitHub 链接查看包含上述源代码的可执行 C# WinForms 示例程序。  
> 链接 : [https://github.com/hyundai-robotics/OpenAPI](https://github.com/hyundai-robotics/OpenAPI)