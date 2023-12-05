### 1.3.1 Sample code - C#

This document uses `Newtonsoft.Json`, a library for JSON parsing.  
If it is not installed in your Visual Studio project, please install it using NuGet Package Manager.

* [Newtonsoft.Json License info](https://github.com/JamesNK/Newtonsoft.Json/blob/master/LICENSE.md)

1) Open `project` properties
2) `Manage NuGet Packages...`
3) Find `Json.NET (James Newton-King)` in `Online/nuget.org` and install it. 
   (If you receive a message that installation is not possible because the version of NuGet Package Manager is too low, select `TOOLS/Extensions and Updates...` from the main menu and update NuGet from Updates..)

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
request.Timeout = 5 * 1000; // 5 sec

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

You can check out the executable C# WinForms sample program containing the above source code through the Github link below.
> Lick : https://github.com/hyundai-robotics/OpenAPI