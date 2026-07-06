
[__SOURCE](README.md)
# ${cont_model} 控制器功能手册 - 开放 API

<div style="max-width: fit-content;">

{% hint style="warning" %}

我们对因使用未在 ${cont_model} 开放 API 手册中正式提及的 API 而引起的任何损坏或问题不承担任何责任。

{% endhint %}

</div>

<div style="max-width: fit-content;">

{% hint style="warning" %}

来自外部设备、高级控制系统或网络传输的信号不在制造商的直接控制范围内。  
因此，制造商对因这些信号引起的任何操作失败、故障或事故不承担任何责任，所有相关责任仅由用户承担。

{% endhint %}

</div>
[__SOURCE](0-about-this-manual/README.md)
# 关于手册
[__SOURCE](0-about-this-manual/precautions.md)
# 注意事项

{% include file="zh/precautions.md" %}
[__SOURCE](0-about-this-manual/safety-notice.md)
# 安全警告

{% include file="zh/safety-notice.md" %}
[__SOURCE](0-intro/README.md)
# 0. 介绍

您可以在下面查看与 ${cont_model} Open API 相关的基本信息。

[0.1 关于 ${cont_model} Open API](./1-concept/README.md) <br>
[0.2 必要的先前知识](./2-prerequisite/README.md) <br>
[0.3 示例代码](./3-sample-code/README.md) <br>
[0.4 无需编码的简单 API 调用](./4-api-test/README.md)<br>
[0.5 开始前的注意事项](./5-caution/README.md)
[__SOURCE](0-intro/1-concept/README.md)
## 0.1 关于 ${cont_model} 开放 API

在本文件中，HD 现代机器人发布了一个 API，供应用开发人员轻松监控和远程控制机器人控制器（以下简称 ${cont_model}）。<br>
这使得开发人员能够读取和写入 ${cont_model} 数据，而无需深入理解用于 ${cont_model} 开发的源代码。<br>
下面的图像将帮助您更好地理解开放 API 的角色。

<img src="../../_assets/05_open_api_flow.png" style="max-height: 22vh;">

上图中标记为橙色的部分显示了开放 API 的角色。

|箭头标志|描述|
|:---|:---|
|`实线`|这意味着 `开发者` (`客户端`) 使用四种方法中的一种（GET、POST、PUT、DELETE）向 `${cont_model}` (`服务器`) `请求` 信息。|
|`虚线`|这意味着 `接收` `请求` 的 `控制器` `发送回` 适当的 `响应`，格式为 json 或文本。|

通过这种方式，开发人员可以使用文档中的开放 API 远程控制或监控通过 ${cont_model} 和基于 http 和 REST API 的以太网连接的台式机、笔记本电脑、平板电脑等。


<br><br>


#### 在开始之前请务必检查！

* 当前文档是基于 ${cont_model} 开放 API 架构版本 `5` 编写的。您可以通过 [API](../../2-version/1-get/1-api_ver.md) 查看。

* 当前文档是基于 ${cont_model} 开放 API 架构版本 ` (5)` 编写的。您可以通过 [API](../../1-version/1-get/1-api_ver.md) 查看它。


{% hint style="warning" %}

除非另有说明，本文件中描述的 API 从 `${cont_model} V60.24-00` 开始支持。

请注意，本文件中未指定的 URL 和属性可能会在相同 API 版本中不经通知而更改。

{% endhint %}
[__SOURCE](0-intro/2-prerequisite/README.md)
## 0.2 先决知识

为了使用 Open API，您必须首先了解如何使用 ${cont_model} 控制器。  
请参考下面的手册或在 HD 現代机器人联合培训中心接受培训。

- [${cont_model} 机器人控制器操作手册](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/zh-tp630/README?cont_model=${cont_model})

<br>

Open API 是一种基于 HTTP 的 REST API。各种开发语言提供用于调用 REST API（也称为 RESTful API）的库，  
许多开发者利用它们来开发程序。除非您是一位经验丰富的开发者，否则，  
您必须熟悉基本概念，即如何进行基于 Web 的服务调用和响应，如 [0.1 关于 ${cont_model} Open API](../1-concept/README.md) 中提到的。

在这方面，请参考以下要点。

* 如果您对下面的简单 API 相关解释不熟悉或在应用方面没有广泛的开发经验，请先学习，然后使用该文档。
* 如果您需要学习，请学习如何通过 REST API 调用编写客户端功能。

<br>

{% hint style="warning" %}

我们不接受关于如何编写传统 REST API 客户端的咨询。

我们不对因使用 ${cont_model} Open API 手册中未正式提及的 API 而导致的任何损害或问题承担责任。

{% endhint %}

---- 

#### 0.2.1 什么是 API？

`API`（应用程序编程接口）是用于构建和集成应用程序软件的 `一组定义和协议` （[ref](https://www.redhat.com/zh/topics/api/what-are-application-programming-interfaces)）。  
这就是用户以特定方式发送的 `请求`，以及提供者的软件对此做出的 `响应`。  
这使您能够与您不知道如何具体开发的产品或服务进行通信，并简化应用程序开发，从而节省时间和金钱。

<br>

#### 0.2.2 什么是 REST API？

`REST`（表现层状态转移）是一种对 API 行为施加条件的 `软件架构`。  
`REST API` 指的是遵循 REST 体系结构风格的 API。也称为 RESTful API （[ref](https://aws.amazon.com/what-is/restful-api/)）。  
通过 HTTP 请求进行通信，它执行标准的数据库功能（CRUD），如在资源内创建、读取、更新和删除记录。

开发者通常使用四种常见的超文本传输协议（HTTP）方法实现 RESTful API （[ref](https://aws.amazon.com/what-is/restful-api/#seo-faq-pairs#what-restful-api-client-contain)）。

- `GET` : 客户端使用 GET 访问位于服务器指定 URL 的资源。它们可以缓存 GET 请求，并在 RESTful API 请求中发送参数，以指示服务器在发送数据之前进行过滤。
- `POST` : 客户端使用 POST 将数据发送到服务器。它们在请求中包含数据表示。多次发送相同的 POST 请求会导致同一资源被多次创建。
- `PUT` : 客户端使用 PUT 更新服务器上的现有资源。与 POST 不同，在 RESTful Web 服务中多次发送相同的 PUT 请求会得到相同的结果。
- `DELETE` : 客户端使用 DELETE 请求删除资源。DELETE 请求可以改变服务器状态。然而，如果用户没有适当的身份验证，请求将失败。
[__SOURCE](0-intro/3-sample-code/README.md)
## 0.3 示例代码

各种开发语言提供用于调用 REST APIs 的库。  
要了解如何使用它，您可以轻松搜索并参考每种开发语言的技术文档。

- 在本文档中，我们将仅使用 C# 和 python 解释对 GET 和 POST 方法的调用。

- 假设您正在向 IP 地址 192.168.1.150 的 ${cont_model} 控制器发出请求。
[__SOURCE](0-intro/3-sample-code/1-csharp.md)
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
[__SOURCE](0-intro/3-sample-code/2-python.md)
#### 0.3.2 示例代码 - python

示例代码主要描述 `a. 同步请求`。

||同步|异步|
|:---|:---|:---|
|阻塞|`a. 同步请求`||
|非阻塞||`b. 异步请求`|

这两种方法之间的差异可能对 TPs 和控制器产生严重后果，如：
1. 由于 UI 线程中频繁的同步函数调用，UI 可能无法流畅运行并可能冻结（`挂起问题`）。
2. 如果由于服务器（控制器）端的问题未收到响应，应用程序 UI 可能冻结（`挂起问题`）。

因此，在开发实际应用程序时，请以异步方式编写代码。  
- 请注意，在 ${cont_model} 开放 API 描述中编写的 python 脚本示例是同步编写的，以便于理解。

<br>

##### a. 同步请求
同步是一种阻塞状态的请求方法，在完成一个请求并收到响应之前，无法执行其他任务。  
在 Python 中用于 `同步` HTTP 请求的广泛使用的库是 `requests`。  
如果没有 `requests` 库，可以通过 Python 包管理器进行安装。

```sh
$pip install requests
```

- 请记住，如果在通信时未收到响应或者需要很长时间才能收到响应，发生挂起问题的可能性可能非常高。

```python
# sync.py - 同步，获取和设置用户 IO 输出值
import requests
import time

url='http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) 设置 fb2.do3 值
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
start_time = time.time()
resp = requests.post(url + path, headers=head, json=req_body)
end_time = time.time()
print('[post]', hex(val), '到 fb2.do3', f"耗时: {end_time - start_time} 秒")

# (GET) 获取 fb2.do3 值
total_start_time = time.time()
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), '来自 fb2.do3', f"耗时: {end_time - start_time} 秒")
total_end_time = time.time()
print(f"总请求时间 : {total_end_time - total_start_time} 秒")
```
```bash
$python sync.py
[post] 0x79 到 fb2.do3 耗时: 0.004312038421630859 秒
[get] 0x79 来自 fb2.do3 耗时: 0.05764031410217285 秒
[get] 0x79 来自 fb2.do3 耗时: 0.06277251243591309 秒
[get] 0x79 来自 fb2.do3 耗时: 0.0634009838104248 秒
[get] 0x79 来自 fb2.do3 耗时: 0.06106710433959961 秒
[get] 0x79 来自 fb2.do3 耗时: 0.04711771011352539 秒
总请求时间 : 0.292741060256958 秒
```
[__SOURCE](0-intro/4-api-test/README.md)
## 0.4 简单的 API 调用，无需编码

如果您在开发客户端应用程序时使用 Open API，像 [之前的示例代码](../3-sample-code/README.md)，您可以轻松地调用 API 而无需编码。  
通过此调用过程，您可以检查请求是否正常工作，以及返回了什么数据作为响应。  
有几种方法可以实现这一点。本节介绍两种代表性的方式。

<br>

#### 0.4.1 使用 `postman`

`postman` 是全球广泛使用的 API 测试平台。  
Postman 的 `workspace` 功能支持项目级的 API 测试和历史跟踪，并配备特定语言的代码片段和直观的用户界面。  
简单的使用说明可以在 [1.4.1 在 Postman 中请求 POST](../4-api-test/1-postman.md) 中找到。

<br>

#### 0.4.2 使用 `Web Browser`

简单的 `get` 请求可以通过网页浏览器轻松快速地完成。  
此外，您可以使用网页浏览器的扩展直接调用 `get` 请求和其他 API 请求并查看结果。  
您可以在 [1.4.2 从网页浏览器调用 API](../4-api-test/2-web-browser.md) 中查看简单的使用说明。
[__SOURCE](0-intro/4-api-test/1-postman.md)
#### 0.4.1 在 Postman 中请求 POST

在此页面上，使用 `postman` 调用 REST API 的 `POST` 请求并检查结果。  
此外，简单的 UI 配置帮助您了解如何使用它。

<br>

##### a. 主要 UI 组成

您可以通过下图查看主要 UI 组成。

<img src="../../_assets/01_postman_desc.png" style="max-height: 55vh;">

<blockquote>

(1) 您可以通过 ` (+)` 按钮简单地创建一个请求。 </br>
(2) 这是输入 `request` 信息的空间。 </br>
(3) 这是检查 `response` 信息的空间。 </br>
(4) 这是一个检查通过应用 `request` URL 自动生成的每种语言的 `Code snippet` 的空间。 </br>

</blockquote>

<br>

##### b. 测试 POST 请求

1. `Request Header`  
	- 在 Headers 标签下输入 `Key` 和 `力控制变量 (Value)`。  
	- 关于 `Content-Type` ([ref](https://blog.postman.com/what-are-http-headers/#Content-type))
	<br><img src="../../_assets/02_postman_headers.png" style="max-height: 14vh;">

<br>

2. `Request Body`  
	- 将 API 方法选择为 `POST` 并输入 URL。  
	- 点击 `Body` 标签并输入您要请求的 `body-parameter`。 ([9.2.1 `task/cur_prog_cnt` - request body](../../8-task/2-post/1-cur_prog_cnt.md))
	- 点击 `发送`  
		<img src="../../_assets/03_postman_post.png" style="max-height: 30vh;">

<br>

3. `Response` 和 `Code snippet`
	- 如果请求正常完成，`request` 的 `HTTP Status` 将响应 `200 OK`，如下所示。([HTTP Status](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status))
	- 您也可以检查应用于 URL 的每种语言的 `Code snippet`。  
		<img src="../../_assets/04_postman_post_result_check.png" style="max-height: 52vh;">  
		<blockquote>

		`(1) 响应体` : 来自 `post` 请求的响应 ([9.2.1 `task/cur_prog_cnt` - response body](../../8-task/2-post/1-cur_prog_cnt.md))</br>
		`(2) Python 代码片段` : python 中 `post` 请求的代码。  
抱歉，我无法处理这个请求。
[__SOURCE](0-intro/4-api-test/2-web-browser.md)
#### 0.4.2 从网络浏览器调用 API  

###### a. 发起简单的 `GET` 请求

`get` 请求可以通过网络浏览器更简单、快速地检查。顺序如下：
1. 打开网络浏览器
2. 在地址栏中输入 `get` 请求的服务器端 URL。
	- 服务器端 URL 以 `http://<${cont_model} 控制器的 IP 地址>:<http 通信端口>` 开头，然后是提取所需信息的路径和查询。
	- 例如） ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
3. 打开该 URL 的页面并输出如下响应。
	```json
	{
		"_type" : "JObject",
		"val" : -99
	}
	```

<br>

###### b. 使用 `extension` 调用 API
如果您使用 Chrome 或 Edge 浏览器，可以通过 Chrome 扩展测试其他 API，而不仅仅是 `get` 请求。  
以下扩展程序是全球许多开发者使用的 API 测试工具。
- Chrome 扩展程序 : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)  

通过此程序，您可以像 `postman` 一样轻松调用各种 API。

<img src="../../_assets/06_Talend_api_tester.png" style="max-height: 80vh;">

<blockquote>

`(1) 请求/场景` : 您可以设置是测试对一个 API 的调用，还是创建多个 API 的场景并依次测试。<br>
`(2) 请求` : 输入您的请求。  
`(3) 响应` : 您可以检查对您请求的响应。  
`(4) 历史` : 打印请求历史。   
`(5) 侧边历史选项卡` : 此选项卡允许您检查比 `(4)` 中的请求历史列表更多的历史，这可以打开和关闭。

</blockquote>
[__SOURCE](0-intro/5-caution/README.md)
## 0.5 注意事项

{% hint style="warning" %}

本节概述了可能导致机器人控制器严重错误的关键预防措施。

在使用 API 之前，请确保您完全理解这些事项。

{% endhint %}


0.5.1. [保持活动状态 vs 关闭连接](./1-http-connection.md)
[__SOURCE](0-intro/5-caution/1-http-connection.md)
#### 0.5.1. Keep-Alive vs Close connection

{% hint style="warning" %}

对于机器人控制器，使用 `关闭 (close)` 连接类型的重复 API 请求可能导致 CPU 负载过高，从而可能导致机器人意外停止。

如果您的应用程序涉及频繁的 API 调用，请遵循以下说明并使用 **Keep-Alive** 连接方法来实现。

{% endhint %}

<br>

###### 1-1. Comparing Two HTTP Connection Methods

<div style="max-width: fit-content">

| | Close | Keep-Alive |
|--| ----- | ----- |
|Recommended HTTP Version| HTTP/1.0 | HTTP/1.1 |
|Characteristics| 多个连接 | 持久连接 |

<img src="../../_assets/07_http_connection.png" style="max-height: 37vh;">

</div>

- `关闭 (close)` 连接类型为每个请求和响应建立和终止连接。<br>
  这个过程导致延迟和资源使用的增加，给服务器和客户端带来了沉重的负担。

- ${cont_model} 使用 HTTP/1.1，默认情况下使用 Keep-Alive 连接，除非明确覆盖。

- 请参考下面的示例代码，确保频繁调用的 API 使用 Keep-Alive，而不是 close 方法来实现。

<br>

###### 1-2. Example Code

- 在 `关闭 (close)` 和 `keep-alive` 连接之间切换很简单，只需修改请求头即可。

- Close connection
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
- Keep-Alive
  <div style="max-width:fit-content">

	```python
	import requests
	import time

	BASE_URL = "http://192.168.10.150:8888"
	URI = "/project/robot/po_cur"
	URL = BASE_URL + URI

	# 默认连接是 Keep-alive
	response = requests.get(URL)
	```
	</div>
- Packet Capture Comparison - Connection Header info <br>
	<img src="../../_assets/08_packet_compare.png" style="max-width: 80vw;"><br>
	左) Keep-Alive, 右) Close

<br><br>

References
  1) [HTTP/1.1 persistent connection](https://datatracker.ietf.org/doc/html/rfc2616#section-8)
[__SOURCE](1-version/README.md)
# 1. `version`

- 检查当前的 API 版本或机器人控制器系统版本。
[__SOURCE](1-version/1-get/README.md)
## 1.1 `version/get`

- 发送 GET 请求以获取有关当前 API 版本或机器人控制系统版本的信息。  
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](1-version/1-get/1-api_ver.md)
#### 1.1.1 `api_ver`

##### Description

在极少数情况下，您的 API 的模式版本可能会更改与控制器或其数据结构的通信方式。  
这可能会导致客户端程序出现问题，因此需要通过相应的功能进行确认。  
如果每个 API 功能的模式版本发生变化，将在描述页面上通过单独的标注进行通知。  

- `GET` : 获取开放 API 版本号

##### path-parameter

```python
GET /api_ver
```

##### response-body

- 开放 API 版本号
- 初始 ${cont_model} 开放 API 是基于 `version 5` 编写的文档。

##### Example

```python
request url:
GET /api_ver

response-body:
5
```

Python Script Example

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
```
[__SOURCE](1-version/1-get/2-sysver.md)
#### 1.1.2 `sysver`

##### 描述

- `GET` : 获取机器人控制器系统的软件版本。

##### 路径参数

```python
GET /versions/sysver
```

##### 响应主体

modules : 模块版本信息数组
  - 模块版本信息 :
    - `名称 (name)` : 模块名称
		|module name|description|
		|---:|:---|
		|com|机器人控制器|
		|tp|教学挂件|
    - `ver` : 版本号
    - `build-date` : 构建日期
    - `build-time` : 构建时间
    - `commit-id` : 源代码的提交 ID

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](2-project/README.md)
# 2. `project`

- 读取条件设置、项目信息和作业文件信息。
- 您可以重新加载更新的作业文件或删除特定的作业文件。
[__SOURCE](2-project/1-get/README.md)
## 2.1 `project/get`

- 发送 GET 请求以获取条件设置、项目信息和作业文件信息。
- 通过为每个 API 设置正确的路径参数和查询参数接收响应。
[__SOURCE](2-project/1-get/1-rgen.md)
#### 2.1.1 `rgen`

##### Description

- `GET` : 在控制器中获取远程一般信息。

##### path-parameter

```python
GET /project/rgen
```

##### response-body

###### 1) Mode
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : 手动 <br> `1` : 手动, 系统设置 <br>`3` : 自动, 1周期 <br> `4` : 自动, 继续 (循环)|`int`|手动/自动模式|
|`enable_state`|`0` Byte(`LSB`) : 电机开启 (0: 开 / 1: 关 / 2: 忙)<br> `1` Byte : TP 启用 (死区) 开关 (0: 关 / 1: 开)<br>`2` Byte : 机器锁 (0: 关 / 1: 开)<br>`3` Byte : 枪锁 (0: 关 / 1: 开)<br>`4` Byte : 枪 (0: 关 / 1: 开)|`int`||
|`is_playback`|`0` : 暂停 <br>`1` : 播放|`int`||
|`is_remote_mode`|`0`: 错误 <br> `1`: 正确|`int`|是否为远程模式|
|`is_ext_start`|`0`: 错误 <br> `1`: 正确|`int`|是否为外部启动|
|`is_ext_prog_sel`|`0`: 错误 <br> `1`: 正确|`int`|是否选择外部程序|

<br>

###### 2) current program counter
在手动模式或自动模式下，教导挂件 JOB 面板上的条形光标所在位置。这是当前正在执行的语句或编辑的目标位置。
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|当前程序编号|
|`cur_step_no`|`int`|当前步骤编号|
|`cur_func_no`|`int`|当前功能编号|

<br>

###### 3) moving program counter
这是机器人在回放期间移动的目标步骤。
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|移动程序编号|
|`mov_step_no`|`int`|移动步骤编号|
|`mov_func_no`|`int`|移动功能编号|

<br>

###### 4) Speed
|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|手动模式 jog 速度级别 (1~8)|
|`manual_spd_max`|`int`|手动模式最大速度 (mm/sec)|
|`auto_spd`|`int`|自动模式回放速度 (%)|
|`jog_inch_status`|`int`|jog 细微移动状态 (0:关/ 1:开)|
|`step_execute_unit_status`|`int`|StepFWD 执行单元 (运行到)<br>0: 命令 <br>1: 步骤<br>2: 结束 |
|`cont_path`|`int`|连续运动模式 (0~2)|

<br>

##### Example
Python 脚本示例

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
[__SOURCE](2-project/1-get/2-jobs_info.md)
#### 2.1.2 `jobs_info`

##### 描述

- `GET` : 获取有关作业程序的信息。

##### path-parameter

```python
GET /project/jobs_info
```

##### response-body

- [作业文件信息](../../99-schema/jobs_info.md)

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](2-project/2-post/README.md)
## 2.1 `project/post`

- 发送一个 POST 请求以获取条件设置、项目信息和作业文件信息。
- 您必须为每个 API 编写正确的请求体。
[__SOURCE](2-project/2-post/1-reload_updated_jobs.md)
#### 2.2.1 `reload_updated_jobs`

##### 描述

- `POST` : 发送请求以更新工作文件。
- 在通过 FTP 将作业文件传输到控制器时，必须通过相应的 API 发起重载请求，以使传输的作业文件在内存中反映。

##### 路径参数

```python
POST /project/reload_updated_jobs
```

##### 请求体

```json
{}
```

##### 描述

```python
请求 URL:
POST /project/reload_updated_jobs

请求体: {}
```

Python 脚本示例

- 请参考 [here](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200) 以获取响应的 HTTP 状态码。
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
[__SOURCE](2-project/2-post/2-jobs-delete_job.md)
#### 2.2.2 `delete_job`

##### 描述

- `POST` : 发送请求以删除工作文件。

##### path-parameter

```python
POST /project/jobs/delete_job
```

##### request-body

```json
{
    "fname": "0001.job"
}
```

##### 示例

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
    "fname": "0001.job"
}
```

Python 脚本示例

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
```
[__SOURCE](3-control/README.md)
# 3. `control`

- 应用控制器的设置并处理输入/输出值。
- 它涉及系统输入/输出、数字输入/输出、条件设置和用户坐标系统的信息。
[__SOURCE](3-control/1-get/README.md)
## 3.1 `control/get`

- 发送 GET 请求以获取控制器设置信息和输入/输出值。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](3-control/1-get/1-op_cnd.md)
#### 3.1.1 `op_cnd`

##### 描述

- `GET` : 获取操作条件设置值。

##### 路径参数

```python
GET /project/control/op_cnd
```

##### 响应体

- [条件设置参数](../../99-schema/op_cnd.md)

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

Python 脚本示例

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
```
[__SOURCE](3-control/1-get/2-ucss-ucs_nos.md)
#### 3.1.2 `ucss/ucs_nos`

##### Description

- `GET` : 获取当前使用的用户坐标系列表。
- 打印通过 `[F2: 系统] - 2: 控制参数 - 6: 坐标系注册 ([F2: system] - 2: Control parameter - 6: Coordinate registration)` 注册的用户坐标系列表。

##### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

##### Example

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python Script Example

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
```
[__SOURCE](3-control/2-post/README.md)
## 3.2 `control/post`

- 发送用于控制器设置信息和输入/输出值的POST请求。
- 您必须为每个API编写正确的请求体。
[__SOURCE](3-control/3-put/README.md)
## 3.3 `control/put`

- 发送用于控制器的设置信息和输入/输出值的 PUT 请求。
- 您必须为每个 API 编写正确的请求主体。
[__SOURCE](3-control/3-put/1-op_cnd.md)
#### 3.3.1 `op_cnd`

##### Description

- `PUT` : 更改机器人的状态设置值。
- 如果在 TP 中打开 `condition setting window(cond.set)` 并请求相应的方法，  
您必须关闭并重新打开窗口，以使值反映出来。

##### path-parameter

```python
PUT /project/control/op_cnd
```

##### request-body

- [Condition Setting parameter](../../99-schema/op_cnd.md)


##### Example

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

Python Script Example

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
```
[__SOURCE](4-robot/README.md)
# 4. `机器人 (robot)`

- 您可以检查机器人和工具数据的远程控制和监控。
- 它涵盖电机开/关、机器人姿态、工具、Jog 坐标系等。
[__SOURCE](4-robot/1-get/README.md)
## 4.1 `robot/get`

- 发送 GET 请求以获取机器人和工具数据。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](4-robot/1-get/1-motor_on_state.md)
#### 4.1.1 `motor_on_state`

##### Description

`motor_on_state`

- `GET` : 获取电机开启状态。

##### path-parameter

```python
GET /project/robot/motor_on_state
```

##### response-body

- val :
  - `0` : 开启
  - `1` : 关闭
  - `2` : 繁忙（转换状态）

##### Example
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
    "_type" : "JObject",
    "val" : 1
}
```

Python Script Example

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
```
[__SOURCE](4-robot/1-get/2-po_cur.md)
#### 4.1.2 `po_cur`

##### Description

- `GET` : 获取机器人当前所处的姿态。

##### path-parameter

```python
GET /project/robot/po_cur
```

##### query-parameter

- `task_no` : 任务编号 (0~7)。
  - unspecified : 应用为任务 0。
  - &gt;=0 : 如果未指定 mechinfo，则应用任务的当前 mechinfo。
- `crd` :  
  - unspecified : 获取所有 tcp、轴和编码器。
  - <0 : 遵循当前记录的坐标系统。
  - &gt;=0 : [坐标系统](../../99-schema/crdsys.md)
- `ucrd_no` : 用户坐标系统编号 (仅在 crd 为用户时指定)。
- `mechinfo` : [机制信息](../../99-schema/mechinfo.md)

##### response-body

- [姿态信息](../../99-schema/pose.md)


##### Example

示例系统包含 6 个机器人轴 (j1~j6) + 1 个驱动轴 (j7) + 2 个定位轴 (j8, j9)。

- 仅获取机器人的基坐标

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

- 获取所有轴的轴坐标

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

- 获取定位器 2 轴的轴坐标 (即机制 M2)

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

Python 脚本示例

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
```
[__SOURCE](4-robot/1-get/3-cur_tool_data.md)
#### 4.1.3 `cur_tool_data`

##### 描述

- `GET` : 获取机器人的当前工具数据。

##### path-parameter

```python
GET /project/robot/cur_tool_data
```

##### response-body

- val : [工具数据](../../99-schema/tool_data.md)

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](4-robot/1-get/4-tools.md)
#### 4.1.4 `tools`

##### Description

- `GET` : 获取机器人所有工具信息。仅获取 T0 到 T31 范围内存在的工具。

##### path-parameter

```python
GET /project/robot/tools
```

##### response-body

- t_0 : [工具数据](../../99-schema/tool_data.md)
- t_1 : 工具数据
- t_2 : 工具数据  
...
- t_31 : 工具数据

##### Example

仅存在工具 0 和工具 31 的系统示例。

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

Python 脚本示例

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
```
[__SOURCE](4-robot/1-get/5-tools_t.md)
#### 4.1.5 `tools/t_{number}`

##### 描述

- `GET` : 这是一个接收特定工具设置信息的函数。

##### path-parameter

```python
GET /project/robot/tools/t_{number}
```

##### response-body

- [工具数据](../../99-schema/tool_data.md)

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](4-robot/1-get/6-emergency_stop.md)
#### 4.1.6 `emergency_stop`

##### 描述

- `GET` : 获取关于紧急停止按钮被按下的状态的信息。  
- 当通过 API 请求紧急停止时，控制器在收到 API 请求的瞬间返回值 1。   

##### path-parameter

```python
GET /project/robot/emergency_stop
```

##### response-body

- 0: 紧急按钮释放
- 1: 紧急按钮被按下 

##### 示例

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "val": 0,
}
```

Python 脚本示例

```python
# test.py
import requests

def get_emergency_stop() -> Optional[dict]:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = requests.get(url=base_url + path_parameter, headers=head)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error in get_emg_state: {e}")
        return None

print(f"{get_emergency_stop()}")
```
```sh
$python test.py
{'_type': 'JObject', 'val': 0}
```
[__SOURCE](4-robot/1-get/7-joint_traject_buf_avail.md)
#### 4.1.7 `joint_traject_buf_avail`

##### 描述
- 支持版本 : `60.32-00` &uparrow;
- `GET` : 返回轨迹缓冲区的可用大小。
- 在连续请求轨迹时，您必须使用此函数以确保每个轨迹请求的大小不超过可用缓冲区空间。

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

##### response-body

- val: 可用缓冲槽的数量（最大：2048）

##### 状态码
  - 200 : 请求成功
  - 403 : 请求失败
    - 调用不支持的 API 时返回

##### 示例

```python
request url:
GET /project/robot/trajectory/joint_traject_buf_avail

response-body:
{
    "val": 2048,
}
```
</div>

Python 脚本示例

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
        print(f"[错误] {e}")
        return None


if __name__ == "__main__":
    base_url = "http://192.168.1.150:8888"

    with requests.Session() as session:
        ret = get_jt_buff_avail_num(base_url, session)
        print(ret)
```
```sh
$python test.py
{'val': 2048}
```
</div>
[__SOURCE](4-robot/1-get/8-joint_states.md)
#### 4.1.8 `joint_states`

##### 描述
- 支持的版本: `70.00-00` ↑
- `GET`: 检索机器人的当前关节状态。
- 返回每个关节的**关节角度（位置, °）、速度和扭矩（努力）**信息。  
  您可以查询所有轴，或选择性查询指定范围的轴。

##### path-parameter

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

##### query-parameter

* * 如果未指定参数，则查询所有关节。
* jno_start (可选)

  * 从哪个关节索引开始查询（从1开始计数）
* jno_n (可选)

  * 要查询的关节数量

##### response

1. 状态代码

   * 200 : OK
   * 400 : 错误请求

     * 查询参数验证失败
   * 403 : 禁止
   * 404 : 未找到

2. 响应体

   * position : 关节角度数组（度）
   * velocity : 关节速度数组
   * effort : 关节扭矩数组（Nm）

        <div style="width: fit-content;">

     ```json
     {
     	"position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
     	"velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     	"effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
     }
     ```

        </div>

##### 使用示例

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

Python脚本示例

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
[__SOURCE](4-robot/2-post/README.md)
## 4.2 `robot/post`

- 发送用于机器人和工具数据的POST请求。
- 您必须为每个API编写正确的请求体。
[__SOURCE](4-robot/2-post/1-motor-on.md)
#### 4.2.1 `motor_on`

##### Description

- `POST` : 执行电机开启。
- `motor_off` API 已被弃用，并从 `v60.30-00` 开始不再支持。

##### path-parameter

```python
POST /project/robot/motor_on
```

##### request-body

```json
{}
```

##### response

1. status code

- 200 : OK
- 400 : 错误请求
  - 请求体未通过验证
- 403 : 禁止
  - 在非远程模式下尝试了 API 请求（自 v60.30-09 起生效）。
- 404 : 未找到


2. response-body

```json
{
    "_type": "JObject"
}
```

3. error code

- -38500 : 由于系统不在远程模式，API 请求被拒绝

##### Example

```python
POST /project/robot/motor_on

request-body:
{}
```

Python Script Example

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
```
```sh
$python test.py
Motor-ON  response: 200
```
[__SOURCE](4-robot/2-post/2-start-stop.md)
#### 4.2.2 `start / stop`

##### 描述

- `POST` : 执行机器人启动和机器人停止。

##### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

##### request-body

```json
{}
```

##### response-body

1. 状态码

- 200 : OK
- 400 : 错误请求
   - 请求体验证失败。
- 403 : 禁止
    - 在非远程模式下尝试了 ` (start)` 请求 (自 v60.30-07 起生效)。
- 404 : 未找到

2. 响应体

```json
{
    "_type": "JObject"
}
```
3. 错误码

- -38500: API 请求被拒绝，因为控制器不在远程模式

##### 示例

```python
POST /project/robot/start or /project/robot/stop

request-body:
{}
```

Python 脚本示例

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # 需要自动模式和电机开启设置
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
```
[__SOURCE](4-robot/2-post/3-tool_no.md)
#### 4.2.3 `tool_no`

##### 描述

- `POST` : 设置当前工具编号。

##### path-parameter

```python
POST /project/robot/tool_no
```

##### request-body

- `val` : 工具编号
  - `robot tools` : `0` ~ `31`
  - `stationary tool` : `0` ~ `3`

##### response-body

```json
{
    "_type": "JObject"
}
```

##### 示例

```json
POST /project/robot/tool_no

request-body
{
  "val": 1
}
```

Python 脚本示例

```python
import requests

def post_tool_no(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/tool_no'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_tool_no(1)}")
```
```sh
$python test.py
response: 200
```
[__SOURCE](4-robot/2-post/4-crd_sys.md)
#### 4.2.4 `crd_sys`

##### 描述

- `POST` : 设置当前的关节坐标系统。

##### path-parameter

```python
POST /project/robot/crd_sys
```

##### request-body

- [坐标系统](../../99-schema/crdsys.md)

##### response-body

```json
{
  "_type": "JObject",
  "cur_crd": 1,
  "ucrd_no": 1
}
```


##### 示例

```json
POST /project/robot/crd_sys

request-body
{
  "val": 1
}
```

Python 脚本示例

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
```
[__SOURCE](4-robot/2-post/5-emergency_stop.md)
#### 4.2.5 `emergency_stop`

- <b style="color:orange"> 对于版本在 ***<u>60.30-00</u>*** 之前，请参阅 ***<u>[emergency_stop_test](./6-emergency_stop_test.md)</u>***，而不是 emergency_stop。 </b>  

##### 描述

- 支持版本 : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  
- 应用与按下紧急停止按钮相同的减速曲线。  
- 由于网络延迟或请求处理时间，API 可能响应慢于物理按钮。  

##### 路径参数

```python
POST /project/robot/emergency_stop
```

##### 请求主体
```python 
{}
```

##### 状态码

- 200 : 请求成功  
- 400 : 请求失败（紧急停止序列执行失败）    

##### 示例

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

Python 脚本示例

```python
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {post_emergency_stop()}")
```
```sh
$python test.py
response: 200
```
[__SOURCE](4-robot/2-post/6-emergency_stop_test.md)
#### 4.2.6 `emergency_stop_test`

- <b style="color:orange"> 此 API 在版本 60.28-00 之前作为 `emergency_stop` API 使用。 </b>  

##### Description

- Supported version : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  

##### path-parameter


<div style="max-width:fit-content">


```python
POST /project/robot/emergency_stop_test
```

</div>

##### request-body

  <div style="max-width:fit-content">

-  |key|type|contents|validation|
	|---|---|---|---|
	|`step_no`| int | 紧急停止的目标步骤编号，在当前作业的总步骤编号内 | 1 ~ 999 |
	|`stop_at`| double | 设置停止时的指定位置的百分比 | 1 ~ 100 |
	|`stop_at_corner`| int | 0: 正常停止, 1: 转角停止 | 0 或 1 |
	|`category`| int | 0: 立即停止, 1: 减速停止, 2: 暂停 | 0 或 1 或 2 |

- `0: 立即停止`  
  &rightarrow; 与机器人回放时控制器关闭时相同。电机在停止后关闭。  

    {% hint style="warning" %}
    规格更改

    - V60.29-08 ~ V60.30-10: 仅能在目标步骤调用立即停止 API。
    - V60.32-00 及以后: 可在任何步骤调用立即停止 API。

    {% endhint %}

- `1: 减速停止`  
	&rightarrow;  像是按下紧急停止按钮一样。电机在停止后关闭。   
- `2: 暂停`  
	&rightarrow;  暂时停止机器人运动。电机在停止后不会关闭。  

</div>

##### status code

- 200 : 请求成功    
- 400 : 请求失败     
	- 请求体验证失败    
- 403 : 请求失败    
	- 请求了未提供服务的 API  


##### Usage Example  

<div style="max-width:fit-content">

```emergency_stop_test
POST /project/robot/emergency_stop_test

request-body
{
  "step_no": 1,
  "stop_at": 50,
  "stop_at_corner": 0,
  "category": 1,
}
```

Python Script Example

```python
import requests


def emergency_stop_test() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop_test"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "step_no": 2,
        "stop_at": 20,
        "stop_at_corner": 0,
        "category": 1,
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {emergency_stop_test()}")
```
```sh
$python test.py
response: 200
```

</div>
[__SOURCE](4-robot/2-post/7-joint_traject_init.md)
#### 4.2.7 `joint_traject_init`

##### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : 初始化轨迹缓冲区。
- 在请求新的轨迹之前，用户必须清除之前存储的轨迹，尤其是在机器人停止时。
- ex)
  - request traj1 → 在运动过程中发生错误 → 必须使用 `joint_traject_init` 清除缓冲区 → request traj2 <br>
  : 如果错误发生时的轨迹数据仍保留在缓冲区中，则在未清除缓冲区的情况下请求 traj2 可能会导致另一个错误。
- 如果在通过 [joint_traject_insert_points](./8-joint_traject_insert_points.md) API 执行轨迹时调用此 API，缓冲区将立即更新。
  - 从缓冲区中删除之前存储的轨迹点可能导致机器人停止并触发错误。 请谨慎使用。


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


##### status code

- 200 : 请求成功
- 403 : 请求失败
  - 当调用不支持的 API 时返回
  - `err_code` (<0): 初始化失败

##### Example

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}
```

Python 脚本示例
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
        print(f"[INFO] 初始化成功: status={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] 初始化轨迹缓冲区失败: {e}")
        return None


def main():
    base_url = "http://192.168.1.150:8888"
    with requests.Session() as session:
        response = post_init_trajectories(base_url, session)


if __name__ == "__main__":
    main()
```
```sh
$python test.py
[INFO] 初始化成功: status=200
```
</div>
[__SOURCE](4-robot/2-post/8-joint_traject_insert_points.md)
#### 4.2.8 `joint_traject_insert_points`

##### Description

- Supported version : `60.32-00` &uparrow;
- `POST` : 发送由多个点组成的轨迹到机器人控制器。
  - 多个关节轨迹点存储在控制器的内部缓冲区，并反映在机器人的运动中。

---

##### Caution

1. 此 API 仅在程序处于 <u>运行状态</u> 时功能正常。
   - 例如) 此 API 只有在程序以自动模式播放时才有效。
   - 如果未满足此条件而提出请求，系统将返回错误。  
	 "[\[E01554\] Not executable state for external command move](https://hr-alarms.web.app/#/${cont_model}/zh/E01554)"

2. 可以一次 POST 的最大轨迹点数是 **<u>2048</u>**。
   - 用于存储轨迹点的缓冲区最大大小为 **<u>2048</u>**。

3. 请求的轨迹点在反映在运动之前不会被丢弃，机器人将继续移动，直到到达相应的位置。
   - 缓冲区中的轨迹在运动执行之前保持不变，除非通过 [joint_traject_init](./7-joint_traject_init.md) api 明确清除。

4. 根据轨迹，可能会发生 "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/${cont_model}/zh/E159)" 错误。如果发生此错误，机器人将停止。

5. 此 API 处理由 **<u>两个或更多点</u>** 组成的轨迹。

6. 使用额外轴时，请注意 **<u>轴坐标值的单位</u>**。

---

##### path-parameter

<div style="width: fit-content;">

```joint_traject_insert_points
POST /project/robot/trajectory/joint_traject_insert_points
```
</div>

##### request-body

<div style="width: fit-content;">

- 	|               Key |       Type      | Description                          | Remarks                                           |
	| ----------------: | :-----------: | --------------------------- | -------------------------------------------- |
	|     `joint_names` | array(string) | 轨迹的关节名称列表          | 例如，对于一个 6 轴机器人: "j1" 到 "j6"， **顺序必须精确** |
	|          `points` |     object({})    | 要执行的轨迹点列表      | 	键: "point_n"，n 从 1 开始。 **至少需要 2 个点**   |
	|       `positions` | array(double) | 每个关节的目标位置，以弧度表示，<br>对于 **额外轴，请注意坐标单位**)| 位置必须根据当前关节数指定。 |
	| `time_from_start` |     number    | 点的起始时间（单位：秒） | 必须是 **<u>0.0</u>** 或 **<u>更大</u>**，并且大于上一个点。 |


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

##### status code

- 200 : 请求成功
- 403 : 请求失败
  - 当调用不支持的 API 时返回

##### error code (response 403)

<div style="width: fit-content;">

- 	| error code     | Error constant name     | Description                                           |
	| ---------- | --------------------------- | ----------------------------------------------------- |
	| `-2`       | `ERR_MISSING_JOINT_NAMES`   | 如果缺少 joint_names 字段 |
	| `-3`       | `ERR_INVALID_JOINT_NAMES`   | 如果 joint_name 格式无效（例如，"x1"），请求的关节数量与<br>机器人的当前关节数量不匹配，或关节名称顺序错误。<br>（例如，["j1", "j3", "j2", ..., "j6"]） |
	| `-4`       | `ERR_MISSING_POINTS`        | 如果缺少 points 字段 |
	| `-5`       | `ERR_INVALID_POINTS`        | 如果 points 的值不是一个对象（即不是 Python 字典），例如整数或字符串 |
	| `-6`       | `ERR_TOO_FEW_POINTS`        | 如果轨迹点数少于 2 |
	| `-7`       | `ERR_TOO_MANY_POINTS`       | 如果请求的轨迹点数超过允许的 2048 |
	| `-8`       | `ERR_POINTS_EXCEED_BUFFER`  | 如果请求的轨迹点数超过当前可用缓冲区空间 |
	| `-9`      | `ERR_INVALID_POINT_OBJECT`  | 如果 point_n 的值不是一个对象（即不是 Python 字典，例如整数或字符串） |
	| `-10`      | `ERR_MISSING_POSITIONS`     | 如果缺少 positions 字段 |
	| `-11`      | `ERR_INVALID_POSITIONS`     | 如果 positions 不是数组，包含非数字值，或其长度与关节数量不匹配 |
	| `-12`      | `ERR_MISSING_TIME`          | 如果缺少 time_from_start 字段        |
	| `-13`      | `ERR_INVALID_TIME`          | 如果 time_from_start 不是数字，小于 0，或在机器人运动时小于前一个值 |

</div>

##### Example

**Ex1. 当机器人处于静止状态时请求轨迹**

<img src="../../_assets/09_online_trajectory_insert_points_single.png" style="max-height: 280px;">

1) 当在机器人停止后请求轨迹时，使用 [joint_traject_init](./7-joint_traject_init.md) api 清除包含先前轨迹的缓冲区。
2) 在请求轨迹之前，检查程序是否在运行，并确保有可用的缓冲区。
3) 请求由 **至少两个点** 组成的轨迹。
   - 将 `起始点的位置信息`（point_1）设置为机器人的 **当前位置**。
   - 将 `起始点的 time_from_start`（point_1）设置为 **0.0**。
   - 后续点应配置以使 `positions` 和 `time_from_start` 值可从前一个点到达，然后再发布。
4) 如果由于错误导致机器人停止，请通过 joint_traject_init 初始化后重新启动，然后按步骤 1 到 3 进行操作。

<br>

**Ex2. 请求具有不连续运动的轨迹（轨迹之间包含停顿时间）**

<img src="../../_assets/10_online_trajectory_insert_points_two.png" style="max-height: 240px;">

1) 必须按照示例 1 中规定的条件发送 traj1 和 traj2。
2) 请注意以下事项：
   - traj2 中的 P1 的位置必须等于 traj1 中的 Pn 的位置。
   - traj2 中的 P1 的 time_from_start 必须为 0.0。

<br>

**Ex3. 请求具有连续运动的轨迹**

<img src="../../_assets/11_online_trajectory_insert_points_continuous.png" style="max-height: 350px;">

1) 根据示例 1 中规定的条件发送 traj1。
2) 当机器人朝 Pn-1 的位置移动时，必须发送 traj2，并注意以下条件。
   - traj1 的 Pn 和 traj2 的 P1 必须配置以使机器人能够平滑和连续地在它们之间移动。
     - traj2 中 P1 的 time_from_start 必须是一个累计值，且 Δ (> 0) 大于 traj1 中最后一个点 Pn 的 time_from_start。
     - traj2 中 P1 的位置必须在时间间隔 Δ 内可以从 traj1 的 Pn 到达。
   - 如果连续请求无法平滑跟随的轨迹，则可能会发生 "[\[E159\] axis speed limit value exceeded](https://hr-alarms.web.app/#/${cont_model}/zh/E159)" 错误。

<div style="width: fit-content;">

<br>

##### Python Script Example

- 将机器人移动到其默认姿势（基于 6 轴配置，[0, 90, 0, 0, 0, 0]）
- 创建并 `播放` 下面的 0001.job 以进入程序播放状态。
- 0001.job
	```job
	Hyundai Robot Job File; { version: 1.6, mech_type: "-1()", total_axis: -1, aux_axis: -1 }
	  > wait di1
		end
	```
- 运行测试脚本（示例 3：请求两个连续运动的轨迹）

	```
	条件1)
	`traj_2` 中 `point_1` 的 `time_from_start` 必须是一个累计值，且 Δ (> 0) 大于 `traj_1` 中 `point_2` 的值。

	条件2)
	`traj_2` 中 `point_1` 的 `positions` 必须在时间间隔 Δ 内可以从 `traj_1` 中的 `point_2` 到达。

	```

	```python
	import requests
	import time
	import math

	session = requests.Session()


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
			print("程序未在运行中！")
			return None

		n_jt_buff_avail = get_jt_buff_avail_num(base_url)
		if n_jt_buff_avail <= 0:
			print("当前关节轨迹缓冲区已满。")
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

			print(ret, ret.json())

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
		base_url = f"http://192.168.1.150:8888"

		while True:
			# 在从静止状态请求轨迹时初始化缓冲区
			post_init_trajectories(base_url)

			# 连续发布轨迹
			ret = post_trajectories(base_url, trajectories_go)
			time.sleep(1)
			ret = post_trajectories(base_url, trajectories_back)
			time.sleep(8)

	```

- ```sh
		$python test.py
		[0] elapsed_ms: 6.122 ms. available jt buff: 2047/2048
		<Response [200]> {'_type': 'JObject'}
		[1] elapsed_ms: 3.997 ms. available jt buff: 2046/2048
		<Response [200]> {'_type': 'JObject'}
		...
	```


</div>
[__SOURCE](4-robot/2-post/9-joint_traject_insert_point.md)
#### 4.2.9 `joint_traject_insert_point`

##### Description
- Supported version: `70.00-00` ↑
- `POST`: **顺序附加下一个关节目标点**以执行关节轨迹。
- 通过重复调用此 API，可以构建连续的关节轨迹。

---

##### Notes

Operating Condition: 程序必须正在运行
* 只有在控制器程序运行时才能调用 API。
* 正常示例: 在自动模式下执行 `wait di1` 语句
* 结果错误: [E01554](https://hr-alarms.web.app/#/${cont_model}/ko/E01554) (外部命令操作准备状态错误)

Physical Condition: 遵守速度和扭矩限制
* 超过系统允许的最大速度和扭矩的命令将导致错误。
* 基本错误: [E159](https://hr-alarms.web.app/#/${cont_model}/ko/E159) (轴速度限制超出错误)

由过扭矩命令触发的级联警报
* 减速器过扭矩: [E249](https://hr-alarms.web.app/#/${cont_model}/ko/E249) · [E6402](https://hr-alarms.web.app/#/${cont_model}/ko/E6402) · [E6403](https://hr-alarms.web.app/#/${cont_model}/ko/E6403)
* 减速器过电流: [W153](https://hr-alarms.web.app/#/${cont_model}/ko/W153) · [W181](https://hr-alarms.web.app/#/${cont_model}/ko/W181) · [W182](https://hr-alarms.web.app/#/${cont_model}/ko/W153)
* 位置偏差超出: [E2630](https://hr-alarms.web.app/#/${cont_model}/ko/E2630) · [E2636](https://hr-alarms.web.app/#/${cont_model}/ko/E2636) · [E2638](https://hr-alarms.web.app/#/${cont_model}/ko/E2638)

注意: 显示的实际警报可能会因轴配置、有效载荷和操作条件而异。

---

##### path-parameter

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
````</div>

---

##### request-body

<div style="width: fit-content;">

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

  * 添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始计算的累计时间
* look_ahead_time

  * 轨迹执行的提前时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态码

   * 200 : OK
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### Usage Example

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

---

##### Python Script Example

###### Prerequisites

1. 将机器人移动到参考姿态。
   (示例 - 对于一个六轴机器人: (

</div>

---

##### request-body

<div style="width: fit-content;">

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

  * 添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始计算的累计时间
* look_ahead_time

  * 轨迹执行的提前时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态码

   * 200 : OK
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### Usage Example

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

---

##### Python Script Example

###### Prerequisites

1. 将机器人移动到参考姿态。
   (示例 - 对于一个六轴机器人: )`[0, 90, 0, 0, -90, 0]`)
2. 插入语句 ()
2. 插入语句 )`wait di1` 到任务中。
3. 切换到自动模式并开始程序播放。
4. 在该状态下运行下面的测试代码。

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
[__SOURCE](5-io_plc/README.md)
# 5. I/O PLC

- 读取或设置内置 PLC 的输入/输出值。
[__SOURCE](5-io_plc/1-get/README.md)
## 5.1 `io_plc/get`

- 发送一个获取内置 PLC 输入/输出值的 GET 请求。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](5-io_plc/1-get/1-relay-value.md)
#### 5.1.1 `get relay values`

##### Description

- `GET` : 获取整个对象类型的继电器值。

##### path-parameter

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

##### path-variable

[relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model}) (小写字母)

* (`{obj_type}{obj_idx}_` 必须为 `di`, `do`, ` (x)`, and ` (y)` 指定。剩余的 `relay_type` 不指定。)

- `obj_type` : 对象类型
  - `fb`
  - `fn`

- `obj_idx` : 对象索引 (fb: 0~9, fn: 0~63)

- `relay_type` : `di`, `do`, ` (x)`, ` (y)`, ` (m)`, ` (s)`, ` (r)`, ` (k)`

##### query-parameter

- `st` : 起始字节索引 (默认: 0)
- `len` : 字数 (默认: 8)

##### Example

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

Python Script Example

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
```
[__SOURCE](5-io_plc/1-get/2-ios-dio.md)
#### 5.1.2 `ios/dio/{dio_val}`

##### Description

- `GET` : 获取用户 IO 值。
- 请参阅 [sio api](./3-ios-sio.md) 以获取系统输入/输出值。

##### path-parameter

<div style="max-width: fit-content;">

```python
GET /project/control/ios/dio/{dio_val}
```

</div>

##### path-variable

- `dio_val` :
  - `di_val` : 获取输入（di）值。
  - `do_val` : 获取输出（do）值。

##### query-parameter

- `类型 (type)` : IO 值的类型
  - di 或 do : bit
  - dib 或 dob : signed-byte
  - diw 或 dow : signed-word (2byte)
  - dil 或 dol : signed-dword (4yte)
  - dif 或 dof : float
- `blk_no` : 块编号 (0~9)
- `sig_no` : 信号索引 (0~)

##### response

1) status code
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) response-body
	- 在成功响应时返回一个有符号的十进制值
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : -99}
		```

		</div>


##### Example

<div style="max-width: fit-content;">

- 获取 fb2.dob3 值。 (结果 : 0b11001000 = 0xc8 = -56)

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```

Python Script Example

```python
# test.py
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
# (当 fb0.do18 = 1, fb0.do20 = 1 / fb0.di14 = 1)
$python test.py
do value: 00101000
di value: 00000010
```

</div>
[__SOURCE](5-io_plc/1-get/3-ios-sio.md)
#### 5.1.3 `ios/sio/{sio_val}` 

##### Description

- `GET` : 获取系统 IO 值。

##### path-parameter

```python
GET /project/control/ios/sio/{sio_val}
```

##### path-variable

- `sio_val` :
  - `si_val` : 获取输入(si) 值。
  - `so_val` : 获取输出(so) 值。

##### query-parameter

- `类型 (type)` : IO 值的类型
  - si 或 so : bit
  - sib 或 sob : signed-byte
  - siw 或 sow : signed-word (2byte)
  - sil 或 sol : signed-dword (4yte)
  - sif 或 sof : float
- `sig_no` : 信号索引 (0~)


##### Example

- 获取 sib1 值。 (结果 : 0b00000010 = 0x02 = 2)

```python
request url:
GET /project/control/ios/sio/si_val?type=sib&sig_no=1

response-body:
{
    "_type" : "JObject",
    "val" : 2,
}
```

Python Script Example

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
```
[__SOURCE](5-io_plc/2-post/README.md)
## 5.2 `io_plc/post`

- 发送来自内置 PLC 的输入/输出值的 POST 请求。
- 您必须为每个 API 编写正确的请求主体。
[__SOURCE](5-io_plc/2-post/1-set_relay_value.md)
#### 5.2.1 `设置继电器值`

##### Description

- `POST` : 设置继电器值。

##### path-parameter

```python
POST /project/plc/set_relay_value
```

##### request-parameter

- `名称 (name)` : 输入您要设置的继电器名称，按照 [relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model})。
- `值 (value)` : 请注意上面的符号中的 'data-type'，并输入您要设置的值。
```json
{
    "name": "fb3.dof14",
    "value": "2.718"
}
```

##### Example

```json
request url:
POST /project/plc/set_relay_value

request-body:
{
    "name": "fb1.do0",
    "value": "1"
}
```

Python Script Example

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
```
[__SOURCE](5-io_plc/2-post/2-ios-dio.md)
#### 5.2.2 `ios/dio/{do_val}`

##### 描述

- `POST` : 更改数字输出。

##### path-parameter

```python
POST /project/control/ios/dio/do_val
```

##### request-body

```json
{
    "type": "do",
    "blk_no": 1,
    "sig_no": 1,
    "val": 1
}
```


##### query-parameter

- `类型 (type)` : io值类型
  - do : 位
  - dob : 有符号字节
  - dow : 有符号字 (2byte)
  - dol : 有符号双字 (4yte)
  - dof : 浮点数
- `blk_no` : 块编号 (0~9)
- `sig_no` : 信号索引 (0~)
- `val` : 你想要更改的设置值


##### 示例

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

Python 脚本示例

- 请参阅 [here](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200) 以获取响应 HTTP 状态码。
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
```
[__SOURCE](6-log_manager/README.md)
# 6.1 事件日志

- 输出在控制器中记录的错误、警告、执行历史等。
[__SOURCE](6-log_manager/1-get/README.md)
## 6.1 `log_manager/get`

- 发送 GET 请求以获取在控制器中记录的错误、警告和执行历史。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](6-log_manager/1-get/1-search.md)
#### 6.1.1 `搜索 (search)`

##### Description

- `GET` : 使用指定的过滤条件查看事件日志。

##### path-parameter

```python
GET /logManager/search
```

##### query-parameter

- `n_item` : 请求的事件数量 (默认=100)
- `cat_p` : 请求类别过滤 (category positive). 通过用逗号 (,) 组合代表每种类型的字母来指定它们。 (cat_p=E,W,N)
  - `E` : 错误
  - `W` : 警告
  - `N` : 通知
  - ` (S)` : 启动/停止
  - `O` : 用户操作
  - `I` : I/O，继电器值
  - ` (P)` : 周期状态
  - ` (H)` : 历史
  - `C按钮 (C)` : 控制台输出
  - ` (M)` : 杂项
- `id_min` : 最小 ID 过滤。 (可选)
  - 每个事件都有一个唯一的事件 ID (eid)。 (0~)  
    如果你通过将之前接收到的事件的最大 ID 加 1 并将其指定在 `id_min` 中请求历史记录，你可以仅获取新发生的历史，排除已接收的事件。
  - 但是，当控制器中的事件 ID 达到最大值 (0xffffffffffffffff) 时，它将从 0 开始重新生成。  
    过滤会考虑到这些情况正确地应用。  
    例如，如果 id_min 为 0xfffffffffffffffa，事件 ID 为 0、1 和 2 的事件仍会被包含在响应中。
- `id_max` : 最大 ID 过滤。 (可选)
- `ts_min` : 最小时间戳过滤。 (可选)
  - 年/月/日期 时:分:秒.毫秒格式。 例如 2023/11/20 18:50:30.955
- `ts_max` : 最大时间戳过滤。 (可选)
  - 年/月/日期 时:分:秒.毫秒格式。 例如 2023/11/20 18:50:30.955

##### response-body

- ` (id)` : 事件 ID
- `ts` : 时间戳
- `cat` : 事件类别
- `代码 (code)` : 事件代码号码
- `aux` : 事件辅助信息。最多 280 个字符。
  - 在发生错误、警告和启动/停止时，会包含快照信息。

```json
{ "id" : 19964, "ts" : "2023/11/20 15:53:11.275", "cat" : "E", "code" : "11,0,0", "aux" : "{ 'pc' : '20/3/1', 'j1' : 18.525, 'j2' : 105.000, 'j3' : -2.577, 'j4' : -14.432, 'j5' : -0.776, 'j6' : 0.314, 'sin' : '00 01 00 00 00 00 00 00', 'sout' : '05 08 06 00 00 00 00 01', 'din' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0', 'dout' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0' }" }
{ "id" : 18314, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(    976)节能 = 开 " }
{ "id" : 18313, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(=时间戳=)[2023/11/20 15:05:33](+299996445微秒) " }
{ "id" : 18312, "ts" : "2023/11/20 15:05:33.787", "cat" : "N", "code" : "5", "aux" : "{ 'pc' : '20/3/1' }" }
{ "id" : 18267, "ts" : "2023/11/20 15:00:33.791", "cat" : "H", "code" : "hist", "aux" : "(   2001)    .end ;(P20/S3/F1) " }
{ "id" : 18266, "ts" : "2023/11/20 15:00:33.789", "cat" : "H", "code" : "hist", "aux" : "( 738785)S3  .move P,spd=500mm/sec,accu=4,tool=0 " }

##### Example

<blockquote>

```python
request url:
GET /logManager/search?cat_p=O&id_max=24258&id_min=24253

response-body:
{
    { "id" : 24258, "ts" : "2023/11/28 16:53:31.239", "cat" : "O", "code" : "K.Click", "aux" : "右" }
    { "id" : 24257, "ts" : "2023/11/28 16:53:30.462", "cat" : "O", "code" : "K.Down", "aux" : "SHIFT" }
    { "id" : 24256, "ts" : "2023/11/28 16:53:23.450", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24255, "ts" : "2023/11/28 16:53:23.045", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
    { "id" : 24254, "ts" : "2023/11/28 16:53:13.695", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24253, "ts" : "2023/11/28 16:53:13.202", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
}
```

</blockquote>

Python Script Example

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
```
[__SOURCE](7-file_manager/README.md)
# 7. `file_manager`

- 这涵盖了从控制器读取文件信息、修改文件名和传输文件等功能。
- 还包括检查目录是否存在以及创建和删除目录的功能。
[__SOURCE](7-file_manager/1-get/README.md)
## 7.1 `file_manager/get`

- 发送一个 GET 请求以获取控制器的文件信息。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](7-file_manager/1-get/1-files.md)
#### 7.1.1 `文件 (files)`

##### Description

- `GET` : 从控制器返回文件内容。

##### path-parameter

```python
GET /file_manager/files
```

##### query-parameter

query-parameter 必须输入。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 要获取的文件名

##### status code

- 200 : 请求成功
  - 返回文件内容
- 403 : 请求失败
  - 当文件不存在时返回错误状态码

##### Example

<blockquote>

```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job   <- 目标
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

</blockquote>

Python Script Example

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
```
[__SOURCE](7-file_manager/1-get/2-file_info.md)
#### 7.1.2 `file_info`

##### 描述

- `GET` : 根据文件路径获取该文件的信息。

##### path-parameter

```python
GET /file_manager/file_info
```

##### query-parameter

query-parameter 必须填写。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### response-body

- [文件信息](../../99-schema/file_info)
- 如果文件不存在，`404 Not Found`

##### 示例

<blockquote>

```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job <- 目标 
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

</blockquote>

Python 脚本示例

```python
# test.py
import requests

def get_file_info() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/file_manager/file_info"
    query_parameter  = {"pathname": "project/${cont_model:lower}_proj.json"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(get_file_info())
```
```sh
$python test.py
{'mday': 31, 'sec': 40, 'fname': '${cont_model:lower}_proj.json', 'wday': 2, 'size': 130551, 'year': 2023, 'hour': 7, 'readonly': False, 'month': 10, 'is_dir': False, 'min': 57}
```
[__SOURCE](7-file_manager/1-get/3-file_list.md)
#### 7.1.3 `file_list`

##### Description

- `GET` : 获取文件和目录的列表。

##### path-parameter

```python
GET /file_manager/file_list
```

##### query-parameter

query-parameter 必须输入。  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|description|
|:---|:---|
|`路径 (path)`|您想要检查的目标路径|
|`incl_file`|输出列表时是否包含文件|
|`incl_dir`|输出列表时是否包含目录|


##### status code

- 200 : 请求成功
  - 返回 [file information](../../99-schema/file_info) `list`
- 403 : 请求失败
  - 没有文件存在


##### Example

<blockquote>

```
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

</blockquote>

Python Script Example

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
```
[__SOURCE](7-file_manager/1-get/4-file_exist.md)
#### 7.1.4 `file_exist`

##### 描述

- `GET` : 获取目标文件的存在性。

##### path-parameter

```python
GET /file_manager/file_exist
```

##### query-parameter

query-parameter 必须输入。

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### response-body

- `true` (文件存在)
- `false` (没有文件存在)

##### 状态码

- 200 : 请求成功
  - 返回 [file information](../../99-schema/file_info) `list`
- 404 : 请求失败
  - 不允许的 path-parameter


##### 示例

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```
```
${cont_model}
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
```

</blockquote>

Python 脚本示例

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
```
[__SOURCE](7-file_manager/2-post/README.md)
## 7.2 `file_manager/post`

- 发送控制器的文件信息的 POST 请求。
- 您必须为每个 API 编写正确的请求主体。
[__SOURCE](7-file_manager/2-post/1-rename_file.md)
#### 7.2.1 `rename_file`

##### Description

- `POST` : 更改目标文件的文件名。

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
- `pathname_from` : 更改前的文件路径
- `pathname_to` : 更改后的文件路径

##### status code

- 200 : 请求成功
  - 工作正常
- 400 : 请求失败
  - 找不到要重命名的文件


##### Example

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
${cont_model}
`-- project
    `-- jobs
        `-- 0001.job   ->   4321.job
```

</blockquote>

Python Script Example

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
```
[__SOURCE](7-file_manager/2-post/2-mkdir.md)
#### 7.2.2 `mkdir`

##### Description

- `POST` : 在目标路径中创建目录。

##### path-parameter

```python
GET /file_manager/mkdir
```

##### request-body

|key|value|description|
|:---|:---|:---|
|`路径 (path)`|`str`|创建目录的位置|

##### response-body

- { `路径 (path)`: ${target path} }

##### status code

- 200 : 请求成功
  - 在目标位置完成目录创建
- 400 : 请求失败
  - 当目标位置的目录名称重复时

##### Example

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
${cont_model}
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- ${cont_model:lower}_proj.json
```


</blockquote>

Python Script Example

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
```
[__SOURCE](7-file_manager/2-post/3-files.md)
#### 7.2.3 `文件 (files)`

##### Description

- `POST` : 将文件传输到目标路径。

##### path-parameter

```python
POST /file_manager/files/{target_filepath}
```

##### path-variable

- `target_filepath` : 包含扩展名的目标文件路径。

##### request-body

- `Content-Type` 必须为 `application/octet-stream`。

##### status code

- 200 : 请求成功
  - 传输完成

##### Example

<blockquote>

```
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

</blockquote>

Python Script Example

```python
# test.py
import requests

def post_file_transfer() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/file_manager/files'
    path_value      = '/project/jobs/test.job' #### target

    target_file     = base_url + path_parameter + path_value
    source_file     = 'D:\\temp\\test.job' #### source (path for WindowOS)

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
```
[__SOURCE](7-file_manager/3-delete/README.md)
## 7.3 `file_manager/delete`

- 从控制器发送删除文件信息的请求。
[__SOURCE](7-file_manager/3-delete/1-files.md)
#### 7.3.1 `文件 (files)`

##### 描述

- `DELETE` : 删除目标文件或目录。

##### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

##### 状态码

- 200 : 请求成功
  - 目标删除完成

##### 示例

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```
```
${cont_model}
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python 脚本示例

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
```
[__SOURCE](8-task/README.md)
# 8. `任务 (task)`

- 它涵盖与任务相关的内容。
- 您可以重置特定任务或所有任务。
- 您可以从当前任务的本地或全局变量读取值或声明新变量。
- 在任务执行期间，可以针对特定工作流程（例如，等待）采取特定行动（例如，释放）。
[__SOURCE](8-task/1-get/README.md)
## 8.1 `task/get`

- 发送与任务相关的信息的 GET 请求。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](8-task/2-post/README.md)
## 8.2 `task/post`

- 发送与任务相关的信息的 POST 请求。
- 您必须为每个 API 编写正确的请求体。
[__SOURCE](8-task/2-post/1-cur_prog_cnt.md)
#### 8.2.1 `task/cur_prog_cnt`

##### Description

- `POST` : 设置任务的当前程序计数器。

##### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

##### request-body

- [cur_prog_cnt request parameter](../../99-schema/cur_prog_cnt.md)

##### response-body

- [cur_prog_cnt response parameter](../../99-schema/cur_prog_cnt.md)

##### Example

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

Python Script Example

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
```
[__SOURCE](8-task/2-post/2-reset.md)
#### 8.2.2 `task/reset`

##### Description

<div style="width: fit-content;">

{% hint style="warning" %}

调用 R-code 0 会初始化程序计数器，这可能导致机器人故障。<br>
请使用 R-code 1 进行错误重置。<br>
我们对因不加选择地调用 R-code 0 而导致的任何问题不承担责任，忽视此警告。

{% endhint %}

##### Description

- `POST`: 初始化步进计数器并移动到 STEP0。
- 利用 [R-code 1](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) 或 [R-code 0](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}).  <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;">
    R-code 1 和 0 以外的代码不是预期的操作。
</span>
- 如果在执行 R-code 1 后需要操作程序计数器，请明确使用 [cur_prog_cnt](./1-cur_prog_cnt.md) 和 [set_cur_pc_idx](./6-set_cur_pc_idx.md) APIs。

##### path-parameter

```python
# reset all the tasks
POST /project/service/r_code/execute
```

##### request-body

```json
{"code": 0}
```

##### response

1) status code
	- 200 : OK
	- 400 : Bad Request
		- 当请求体验证失败时
	- 403 : Forbidden
        - 当进行未经授权的请求时
        - 返回 `err_code` (<0)。请参阅下面的错误代码
	- 404 : Not Found

2) response-body
   - code: 返回请求的 rcode 编号
        <div style="width: fit-content;">

		```json
		{"code": 1, ... })
		```

		</div>


##### Example

```python
request url:
POST /project/service/r_code/execute

request-body:
{
    "code":0
}
```

Python Script

```python
import requests


def post_rcode_0() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/service/r_code/execute"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"code": 0}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)
    return response.status_code


print(f"response: {post_rcode_0()}")
```
```sh
$python test.py
response: 200
```
[__SOURCE](8-task/2-post/3-assign_var_expr.md)
#### 8.2.3 `assign_var_expr`

##### Description

- `POST` : 在当前任务语句中重新分配变量。

##### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

##### request-body

- `名称 (name)` : 变量名
- `expr` : 要替代到变量中的表达式
- `保存 (save)` : 是否保存（true/false）。这是为了保存变量文件中的数据。
- `scope` : 设置变量的有效作用域
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|局部变量|全局变量|完整作用域（局部和全局自动设置）|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

##### Example

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

当上述作业文件被执行，并在任务中声明了一个局部变量 ` (a)`

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

Python脚本示例

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
```
[__SOURCE](8-task/2-post/4-assign_var_json.md)
#### 8.2.4 `assign_var_json`

##### 描述

- `POST` : 重新分配当前任务语句中的变量。  

##### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

##### request-body

- `名称 (name)` : 变量名称
- `json` : 要替换为变量的 json 格式 `string`。
- `保存 (save)` : 保存内容 (true/false)。也就是直到你将该数据保存到你的活动文件中。
- `scope` : 设置变量的有效范围
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|局部变量|全局变量|完整范围 (局部和全局会自动设置)|


```json
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```

##### 示例

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

当上述作业文件被执行并且在任务中声明一个局部变量 ` (a)`

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

Python 脚本示例

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
```
[__SOURCE](8-task/2-post/5-release_wait.md)
#### 8.2.5 `release_wait`

##### 描述

- `POST` : release 语法
- 要求：在输入 `[2: system] - 1: 用户环境 ([2: system] - 1: User environment)` 后，点击 `[Enable]` 以进行 `wait(di/wi) release`

##### 路径参数

```python
POST /project/context/tasks[0]/release_wait
```

##### 请求体

```json
{}
```

##### 状态码

- 200 : 请求成功
- 403 : 请求失败
  - 未满足上述要求

##### 错误代码
- -1442069 : 用户环境配置错误。请确保满足所有前提要求

##### 示例

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python 脚本示例

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
```
[__SOURCE](8-task/2-post/6-set_cur_pc_idx.md)
#### 8.2.6 `set_cur_pc_idx`

##### 说明

- `POST` : 将当前光标定位在索引行的功能

##### path-parameter

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

##### request-body
```json
{
    "idx": 1
}
```

##### 示例

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

Python 脚本示例

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
response 200 # 光标位置已在 TP 上更改
```
[__SOURCE](8-task/2-post/7-solve_expr.md)
#### 8.2.7 `solve_expr`

##### Description

- `POST` : 解决表达式并将结果值设置为任务的本地或全局变量。

##### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

##### request-body
- `expr` : 输入您想要求解的表达式
- `scope` : 设置 `expr` 的作用域。

	|`local`|`global`|`not set`|
	|:---|:---|:---|
	|本地变量|全局变量|完整作用域（本地和全局自动设置）|

```json
{
    "expr" : "a",
    "scope" : "local"
}
```

##### response-body

```json
13 // 在当前指定作用域内读取 expr 值。
```

##### Example

<blockquote>

```python
# 1. 读取当前任务中声明的"local"变量 a 的值
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
# 2. 读取当前任务中声明的"global"变量 a 的值
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
# 3. 将 -234 加到本地变量 a 的值
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

Python Script Example
- 执行以下代码时，任务区域的本地和全局变量 a 值已设置在机器人控制器中。

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
```
[__SOURCE](8-task/2-post/8-execute_move.md)
#### 8.2.8 `execute_move`

##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : 移动到指定姿态。

{% hint style="warning" %}
HRSpace 用户专用<br>
execute_move 可能因 VRC_${cont_model} v60.30-10 到 v60.32-06 的远程模式验证错误而失败<br>
→ 使用 v60.30-09 或更早版本，或 v60.32-07 或更高版本（物理 ${cont_model:upper} 控制器不受影响）
{% endhint %}

##### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### request-body
- `stmt` : 请求体中的关键值，指代语句。
- 有关如何编写移动语句的详细信息，请参见 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/zh/5-moving-robot/4-move?cont_model=${cont_model})。

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

##### response

1. 状态代码
- 200 : OK
- 400 : 错误请求
    - 请求体未通过验证。
- 403 : 禁止
    - 在未处于远程模式下尝试 API 请求（自 v60.30-07 起生效）。
- 404 : 未找到

2. 响应体

- v60.30 或更早版本的正常响应

```json
{ "err_code" : 0 }
```

- v60.32 或更高版本的正常响应

```json
{ "_type" : "JObject" }
```

3. 错误代码

- -38500 : 在未处于远程模式下尝试 API 请求
- -1442071 : 在电机关闭时尝试 API 请求
- -1442080 : 在自动程序执行期间尝试 API 请求
- -1376272 : 处理 API 请求时出现机器人语言语法错误

Python 脚本示例
- 当电机开启并与当前机器人轴匹配时输入姿态命令。

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
```
[__SOURCE](9-console/README.md)
# 9. `console`

- 您可以使用 ${cont_model} 控制器软件的 CLI 命令。  
- 可以使用机器人语言执行各种操作。
[__SOURCE](9-console/1-get/README.md)
## 9.1 `console/get`

- 发送与执行机器人命令相关的信息的GET请求。  
- 每个API的确切路径参数和查询参数必须设置，以接收响应。  
[__SOURCE](9-console/2-post/README.md)
## 9.2 `console/post`

- 发送与执行机器人命令相关的信息的POST请求。  
- 每个API的确切请求体必须写明。
[__SOURCE](9-console/2-post/1-execute_cmd.md)
#### 9.2.1 `execute_cmd`


##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : 执行 ${cont_model} 控制器的控制台命令。  
- 您可以执行 [CLI 机器人语言命令](../.././99-schema/robotlang.md)。  

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

##### status code

- 200: 请求成功  
	- 需要应用 [CLI 机器人语言命令](../.././99-schema/robotlang.md) 规则  
	- 如果命令违反机器人语言规则，则会返回 ecode 1，如下所示。
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400: 请求失败
	- 请求体验证失败
- 403/4: 请求失败
	- 请求的 API 未提供服务

##### Example

</blockquote>

Python 脚本示例
- 命令可以在 ` (motor on)` 和 `remote mode` 状态下执行。  
- 当移动命令与当前机器人轴匹配时，可以执行。  

```python
# test.py
import time
import requests


class ExecuteCmds:
    request_to = {
        "com": [
            "rl.stop",  # 外部停止
            "rl.reinit",  # 重启
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i end",
            "rl.start",  # 播放
        ],
    }


def post_execute_cmd() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/console/execute_cmd"
    head = {"Content-Type": "application/json; charset=utf-8"}

    execute_cmds = ExecuteCmds.request_to["com"]

    response: int = None
    for cmd in execute_cmds:
        data = {"cmd_line": cmd}
        response = requests.post(url=base_url + path_parameter, headers=head, json=data)
        print(f"response: {response}")
        time.sleep(0.1)

    return 200


print(f"response: {post_execute_cmd()}")
```
```sh
$python test.py 
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: 200
```
[__SOURCE](10-etc/README.md)
# 10. `etc`

- 它涵盖系统版本、事件日志、时钟等。
[__SOURCE](10-etc/1-clock/README.md)
# 10.1 `clock`

- 您可以读取和设置控制器的系统时间。
[__SOURCE](10-etc/1-clock/1-get/README.md)
#### 10.1.1 `clock/get`

- 发送获取控制器系统时间的 GET 请求。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](10-etc/1-clock/1-get/1-date_time.md)
#### 10.1.1.1 `date_time`

##### 描述

- `GET` : 获取设置的系统时间。

##### response-body

- [date time](../../../99-schema/date_time.md)

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](10-etc/1-clock/2-put/README.md)
#### 10.1.2 `clock/put`

- 发送PUT请求到控制器系统时间。
- 你必须为每个API写正确的请求体。
[__SOURCE](10-etc/1-clock/2-put/1-date_time.md)
#### 10.1.2.1 `date_time`

##### 描述

- `PUT` : 更改系统时间。

##### request-body

- [date time](../../../99-schema/date_time.md)

##### 示例

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

Python 脚本示例

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
```
[__SOURCE](99-schema/README.md)
# 11. 结构

本章包含对 Open API 中使用的各种枚举和结构的引用。
[__SOURCE](99-schema/crdsys.md)
### `crdsys`

#### 描述

这是一个枚举，用于指定坐标系统。
|value|description|
|:---:|:---|
|`-1`|`下一个 (next)` 坐标系统|
|`0`|`基座 (base)` 坐标系统|
|`1`|`机器人 (robot)` 坐标系统|
|`2`|`轴 (axis)` 坐标系统|
|`3`|`编码器 (encoder)` 坐标系统|
|`4`|`用户 (user)` 坐标系统|
[__SOURCE](99-schema/cur_prog_cnt.md)
### `cur_prog_cnt`

#### Description
设置任务的当前程序计数器。

#### request body
|key|type|description|
|:---|:---|:---|
|`pno`|int|程序编号（如果是-1，则保持当前编号）|
|`sno`|int|步骤编号（如果是-1，则保持当前编号）|
|`fno`|int|功能编号（如果是-1，则保持当前编号）|
|`ext_sel`|int|`0` : 内部选择（在远程模式下禁止） <br> `1` : 外部选择（仅在远程模式下允许）|

#### response body
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|新移动的步骤编号|
|`fno_new`|int|新移动的功能编号|
|`ln_new`|int|新移动的行编号（程序头为0，第一条语句为1）|
[__SOURCE](99-schema/date_time.md)
### `date_time`

#### 描述

指示系统时间相关的信息。
|value|type|description|
|:---:|:---|:---|
|"year"|`int`|当前系统的年份|
|"mon"|`int`|当前系统的月份|
|"day"|`int`|当前系统的日期|
|"hour"|`int`|当前系统的小时|
|"min"|`int`|当前系统的分钟|
|"sec"|`int`|当前系统的秒数|
[__SOURCE](99-schema/file_info.md)
### `file_info`

#### 描述

此参数在请求文件信息时返回。

|key|type|description|
|:---:|:---|:---|
|fname|`str`|文件名|
|size|`int`|文件大小(B, Byte)|
|year|`int`|文件修改的 `年份` |
|month|`int`|文件修改的 `月份` |
|mday|`int`|文件修改的 `日期` |
|wday|`int`|文件修改的 `星期几` (0: 周日, 1: 周一, 2: 周二, ...) |
|hour|`int`|文件修改的 `小时 (hour)` |
|min|`int`|文件修改的 `分钟` |
|sec|`int`|文件修改的 `秒` |
|is_dir|`bool`|检查当前文件是否为目录 |
|readonly|`bool`|检查文件是否为只读 |
[__SOURCE](99-schema/jobs_info.md)
### `jobs_info`

#### Description

这是一个作业文件信息参数。

|key|type|description|
|:---:|:---|:---|
|fname|`str`|作业文件名|
|job_comment|`str`|评论|
|n_step|`int`|步骤数|
|n_total_ax|`int`|轴的数量|
|n_aux_ax|`int`|附加轴的数量|
[__SOURCE](99-schema/mechinfo.md)
### `mechinfo`

#### Description

机制信息  
使用位字段庆祝使用哪些活动。

- bit 0 : M0
- bit 1 : M1
- bit 2 : M2
- bit 3 : M3
- bit 4 : M4
- bit 5 : M5
- bit 6 : M6
- bit 7 : M7

#### Example

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 指定机制 M0, M1 和 M4。
```
[__SOURCE](99-schema/op_cnd.md)
### `op_cnd`

#### Description
op_cnd (操作条件) : value of `条件设置 (Condition setting)`  
You can check the values when you press the `条件设置 (Condition setting)` button in TP.  

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1周期 <br> `2` : 重复|自动操作周期模式|
|step_goback_max_spd|` (10)` ~ `250` (mm/sec)|前进/后退时的最大速度|
|step_go_func_ex|`0` : 无效 <br> `1` : 有效 <br> `2` : I ON (=DI信号)|前进步骤时的功能执行|
|func_reexe_on_trace| `0` : 无效 <br> `1` : 有效 |后退后，再次执行向前移动时的功能|
|path_recov_confirm|`0` : 无效 <br> `1` : 有效|前进/后退时的路径恢复|
|playback_spd_rate|`1` ~ `100` (%)|自动操作速度比率|
|robot_lock|`0` : 无效 <br> `1` : 有效 |机器人锁定|
|intp_base|`0` : 机器人工具 <br> `1` : 定位工具|插补标准|
|ucrd_num|`0` ~ ` (20)`|指定用户坐标系|
|plc_mode|`0` : 关 -> 停止 <br> `1` : 停止 -> 远程停止 <br> `2` : 远程停止 -> 远程停止 <br> `3` : 远程运行 -> 远程停止 <br> `4` : 运行 -> 关|PLC操作模式|

<br>

#### Example

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
[__SOURCE](99-schema/pose.md)
### `姿势 (Pose)`

#### Description

姿势数据。

|key|description|
|:---|:---|
|x|X 位置 (mm)|
|y|Y 位置 (mm)|
|z|Z 位置 (mm)|
|rx|RX 角度 (deg.)|
|ry|RY 角度 (deg.)|
|rz|RZ 角度 (deg.)|
|j1~j16|1~16 轴值(mm 或 deg.)|
|crd|[坐标系统](./crdsys.md)|
|mechinfo|[机制信息](./mechinfo.md)|
|nsync|传感器同步值数量 (0~2)|
|sync|传感器同步值 (字符串). 例如 `"sync(220.5,195.3)"`|
[__SOURCE](99-schema/tool_data.md)
### `tool_data`

#### 描述

机器人的工具数据。

|key|description|
|:---:|:---|
|` (x)`|X 位置 (mm)|
|` (y)`|Y 位置 (mm)|
|` (z)`|Z 位置 (mm)|
|`rx`|RX 角度 (度)|
|`ry`|RY 角度 (度)|
|`rz`|RZ 角度 (度)|
|`mass`|重量 (kg)|
|`cx`|X 位置的重心 (mm)|
|`cy`|Y 位置的重心 (mm)|
|`cz`|Z 位置的重心 (mm)|
|`ixx`|惯性 X (kgm²)|
|`iyy`|惯性 Y (kgm²)|
|`izz`|惯性 Z (kgm²)|
|`mass_esti`|载荷估算重量 (kg)|
[__SOURCE](99-schema/robotlang.md)
### CLI Robot Language Commands

#### Description

这是可以从 ${cont_model} 控制器控制台执行的机器人语言命令列表。  

|option|description|example|
|:---|:---|:---|
|`reinit`| 执行机器人语言重启命令。 |rl.reinit|
|` (i)`| 将机器人语言命令插入到作业文件中。 |rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|` (start)`| 当`电机开启`且处于`远程模式`时执行机器人语言。|rl.start|
|` (stop)`| 当机器人语言正在运行时执行`外部停止`。|rl.stop|
|`exit`| 终止当前正在运行的机器人语言。|rl.exit|