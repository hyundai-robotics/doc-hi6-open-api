
[__SOURCE](README.md)
# ${cont_model} 控制器功能手册 - 开放 API

{% hint style="warning" %}

我们对因使用未在 ${cont_model} 开放 API 手册中正式提及的 API 而导致的任何损坏或问题不承担责任。

{% endhint %}
[__SOURCE](0-about-this-manual/README.md)
# 关于手册

[__SOURCE](0-about-this-manual/precautions.md)
# 注意事项

{% include file="zh/precautions.md" %}
[__SOURCE](0-about-this-manual/safety-notice.md)
# 安全注意事项

{% include file="zh/safety-notice.md" %}

[__SOURCE](0-intro/README.md)
# 0. 介绍

您可以在下面查看与 ${cont_model} Open API 相关的基本信息。

[0.1 关于 ${cont_model} Open API](./1-concept/README.md) <br>
[0.2 所需的先验知识](./2-prerequisite/README.md) <br>
[0.3 示例代码](./3-sample-code/README.md) <br>
[0.4 无需编码的简单 API 调用](./4-api-test/README.md)
[0.5 启动前的注意事项](./4-api-test/README.md)
[__SOURCE](0-intro/1-concept/README.md)
## 0.1 关于 ${cont_model} 开放 API

在此文档中，HD 现代机器人发布了一种 API，供应用程序开发者轻松监控和远程控制机器人控制器（以下称为 ${cont_model}）。<br>
这使开发者能够读写 ${cont_model} 数据，而无需深入理解 ${cont_model} 开发中使用的源代码。<br>
下面的图像将帮助您更好地理解开放 API 的作用。

<img src="../../_assets/05_open_api_flow.png" style="max-height: 22vh;">

上图中标记为橙色的部分显示了开放 API 的作用。

|箭头标志|描述|
|:---|:---|
|`实线`|这意味着 `开发者` (`客户端`) 使用四种方法中的一种（GET、POST、PUT、DELETE）向 `${cont_model}` (`服务器`) `请求` 信息。|
|`虚线`|这意味着 `接收` `请求` 的 `控制器` `发送回` 适当的 `响应`，格式为 json 或文本。|

通过这种方式，开发者可以使用文档中的开放 API 远程控制或监控通过 ${cont_model} 和以 http 和 REST API 为基础的以太网连接的桌面、笔记本电脑、平板电脑等。

<br><br>

#### 开始之前请确保检查！

* 当前文档是基于 ${cont_model} 开放 API 架构版本 ` (5)` 编写的。您可以通过 [API](../../2-version/1-get/1-api_ver.md) 查看它。

* 对于熟悉开发 HTTP REST API 客户端功能的开发者，可以跳过 [1.2 所需的先前知识](../2-prerequisite/README.md) 到 [1.4 无需编码的简单 API 调用](../4-api-test/README.md)。

{% hint style="warning" %}

除非另有说明，本文件中描述的 API 从 `${cont_model} V60.24-00` 开始支持。

请注意，本文件中未指定的 URL 和属性在同一 API 版本中可能会更改，恕不另行通知。

{% endhint %}
[__SOURCE](0-intro/2-prerequisite/README.md)
## 0.2 所需的先前知识

为了使用 Open API，您必须首先了解如何使用 ${cont_model} 控制器。  
请参考以下手册或在 HD 现代机器人联合培训中心接受培训。

- [${cont_model} 机器人控制器操作手册](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-operation/zh-tp630/README?cont_model=${cont_model})

<br>

Open API 是一种基于 HTTP 的 REST API。各种开发语言提供用于调用 REST API（即 RESTful API）的库，  
许多开发人员使用它们来开发程序。除非您是经验丰富的开发人员，  
否则您必须熟悉如何进行基于 Web 的服务调用和响应的基本概念，正如 [1.1 关于 ${cont_model} Open API](../1-concept/README.md) 中提到的那样。

在这方面，请参考以下要点。

* 如果您对以下简单的 API 相关说明不熟悉或不是在应用中具有广泛开发经验的专家，请先学习然后再使用该文档。
* 如果您需要学习，请学习如何通过 REST API 调用来编写客户端功能。

<br>


{% hint style="warning" %}

我们不接受有关如何编写传统 REST API 客户端的询问。

我们对因使用 ${cont_model} Open API 手册中未正式提及的 API 而导致的任何损害或问题不承担责任。

{% endhint %}

---- 

#### 0.2.1 什么是 API？

`API`（应用程序编程接口）是一套用于构建和集成应用程序软件的 `定义和协议` ([ref](https://www.redhat.com/zh/topics/api/what-are-application-programming-interfaces))。  
这就是用户发送以特定方式结构化的 `请求`，并且提供者的软件 `响应` 该请求的方式。  
这使您能够与您不知道如何具体开发的产品或服务进行通信，并简化应用程序开发，从而节省时间和金钱。

<br>


#### 0.2.2 什么是 REST API？

`REST`（表现层状态转移）是一种对 API 行为施加条件的 `软件架构`。  
`REST API` 指的是遵循 REST 架构风格的 API。也称为 RESTful API ([ref](https://aws.amazon.com/what-is/restful-api/))。  
通过 HTTP 请求进行通信，它执行标准数据库功能（CRUD），例如在资源内创建、读取、更新和删除记录。

开发人员通常使用四种常见的超文本传输协议（HTTP）方法来实现 RESTful API ([ref](https://aws.amazon.com/what-is/restful-api/#seo-faq-pairs#what-restful-api-client-contain)).
- `GET` : 客户端使用 GET 来访问位于服务器指定 URL 的资源。它们可以缓存 GET 请求，并在 RESTful API 请求中发送参数，以指示服务器在发送数据之前过滤数据。
- `POST` : 客户端使用 POST 来向服务器发送数据。它们包括请求中的数据表示。多次发送相同的 POST 请求会导致创建相同资源的副作用。
- `PUT` : 客户端使用 PUT 来更新服务器上的现有资源。与 POST 不同，在 RESTful Web 服务中多次发送相同的 PUT 请求会得到相同的结果。
- `DELETE` : 客户端使用 DELETE 请求来删除资源。DELETE 请求可以更改服务器状态。但是，如果用户没有适当的身份验证，请求将失败。

[__SOURCE](0-intro/3-sample-code/README.md)
## 0.3 示例代码

各种开发语言都提供用于调用 REST APIs 的库。  
要了解如何使用它，您可以轻松搜索并参考每种开发语言的技术文档。

- 在本文档中，我们将仅使用 C# 和 Python 解释对 GET 和 POST 方法的调用。

- 假设您向 IP 地址为 192.168.1.150 的 ${cont_model} 控制器发出请求。
[__SOURCE](0-intro/3-sample-code/1-csharp.md)
#### 0.3.1 示例代码 - C#

本文件使用 `Newtonsoft.Json`，这是一个用于 JSON 解析的库。  
如果您在 Visual Studio 项目中未安装，请使用 NuGet 包管理器进行安装。

* [Newtonsoft.Json 许可证信息](https://github.com/JamesNK/Newtonsoft.Json/blob/master/LICENSE.md)

1) 打开 `project` 属性  
2) `管理 NuGet 包...`  
3) 在 `Online/nuget.org` 中找到 `Json.NET (James Newton-King)` 并进行安装。  
   （如果您收到一条消息，说明由于 NuGet 包管理器的版本过低而无法安装，请从主菜单中选择 `TOOLS/Extensions and Updates...`，并从更新中更新 NuGet。）

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

您可以通过以下 Github 链接查看包含上述源代码的可执行 C# WinForms 示例程序。  
> 链接 : [https://github.com/hyundai-robotics/OpenAPI](https://github.com/hyundai-robotics/OpenAPI)
[__SOURCE](0-intro/3-sample-code/2-python.md)
#### 0.3.2 示例代码 - python

示例代码主要描述 `a. 同步请求`。


||同步|异步|
|:---|:---|:---|
|阻塞|`a. 同步请求`||
|非阻塞||`b. 异步请求`|

这两种方法之间的差异可能对TP和控制器产生严重后果，例如：
1. 由于UI线程中频繁调用同步函数，UI可能无法流畅运行并可能会冻结 (`挂起问题`)。
2. 如果由于服务器（控制器）端的问题未收到响应，则应用程序UI可能会冻结 (`挂起问题`)。

因此，在开发实际应用时，请以异步方式编写代码。  
- 请注意，${cont_model} Open API 描述中编写的python脚本示例是为了便于理解而同步编写的。  


<br>

##### a. 同步请求
同步是一种阻塞状态的请求方法，在一个请求完成并收到响应之前，无法执行其他任务。  
在Python中，`synchronous` HTTP请求的广泛使用库是 `requests`。
如果您没有 `requests` 库，可以通过Python包管理器进行安装。  

- 请记住，如果在通信时未收到响应或收到响应需要很长时间，可能出现挂起问题的可能性非常高。

```python
# sync.py - 同步，获取和设置用户IO输出值
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
print('[post]', hex(val), '设置到 fb2.do3', f"耗时: {end_time - start_time} 秒")

# (GET) 获取 fb2.do3 值
total_start_time = time.time()
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), '从 fb2.do3 获取', f"耗时: {end_time - start_time} 秒")
total_end_time = time.time()
print(f"总请求时间 : {total_end_time - total_start_time} 秒")
```
```bash
$python sync.py
[post] 0x79 到 fb2.do3 耗时: 0.004312038421630859 秒
[get] 0x79 从 fb2.do3 耗时: 0.05764031410217285 秒
[get] 0x79 从 fb2.do3 耗时: 0.06277251243591309 秒
[get] 0x79 从 fb2.do3 耗时: 0.0634009838104248 秒
[get] 0x79 从 fb2.do3 耗时: 0.06106710433959961 秒
[get] 0x79 从 fb2.do3 耗时: 0.04711771011352539 秒
总请求耗时 : 0.292741060256958 秒
```
[__SOURCE](0-intro/4-api-test/README.md)
## 0.4 简单的 API 调用，无需编码

如果您在开发客户端应用程序时使用开放 API，例如 [先前的示例代码](../3-sample-code/README.md)，您可以轻松地进行 API 调用，而无需编码。  
通过这个调用过程，您可以检查请求是否正常工作以及返回了什么数据。  
这有几种方法可以做到。 本节将介绍两个代表性的方式。

<br>

#### 0.4.1 使用 `postman`

`postman` 是全球广泛使用的 API 测试平台。  
Postman 的 `workspace` 功能能够进行项目级别的 API 测试和历史跟踪，并配备了特定语言的代码片段和直观的用户界面。  
简单的使用说明可以在 [1.4.1 在 Postman 中请求 POST](../4-api-test/1-postman.md) 中找到。

<br>

#### 0.4.2 使用 `Web 浏览器`

简单的 `get` 请求可以通过 Web 浏览器轻松快速地进行。  
此外，您可以使用 Web 浏览器的扩展直接调用 `get` 请求和其他 API 请求，并查看结果。  
您可以在 [1.4.2 从 Web 浏览器调用 API](../4-api-test/2-web-browser.md) 中查看简单的使用说明。
[__SOURCE](0-intro/4-api-test/1-postman.md)
#### 0.4.1 在 Postman 中请求 POST

在此页面上，使用 `postman` 调用 REST API 的 `POST` 请求并检查结果。  
此外，简单的 UI 配置帮助您理解如何使用它。

<br>

##### a. 主 UI 结构

您可以通过下面的图片查看主 UI 结构。

<img src="../../_assets/01_postman_desc.png" style="max-height: 55vh;">

<blockquote>

(1) 您可以通过 `+` 按钮简单地创建请求请求。 </br>
(2) 这是输入有关 `request` 信息的空间。 </br>
(3) 这是检查有关 `response` 信息的空间。 </br>
(4) 这是检查通过应用 `request` URL 自动生成的每种语言的 `Code snippet` 的空间。 </br>

</blockquote>

<br>

##### b. 测试 POST 请求

1. `请求头`  
	- 在 Headers 标签下输入 `Key` 和 `值 (Value)`。
  	- 关于 `Content-Type` ([ref](https://blog.postman.com/what-are-http-headers/#Content-type))
	<br><img src="../../_assets/02_postman_headers.png" style="max-height: 14vh;">

<br>

2. `请求体`  
	- 将 API 方法选择为 `POST` 并输入 URL。  
	- 点击 `Body` 标签并输入您要请求的 `body-parameter`。 ([9.2.1 `task/cur_prog_cnt` - request body](../../9-task/2-post/1-cur_prog_cnt.md))
	- 点击 `发送`  
		<img src="../../_assets/03_postman_post.png" style="max-height: 30vh;">

<br>

3. `响应` 和 `代码片段`
	- `request` 如果请求正常完成，`HTTP 状态` 将响应 `200 OK`，如下所示。([HTTP Status](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status))
	- 您还可以检查应用于 URL 的每种语言的 `Code snippet`。  
		<img src="../../_assets/04_postman_post_result_check.png" style="max-height: 52vh;">  
		<blockquote>

		`(1) 响应体` : 来自 `post` 请求的响应 ([9.2.1 `task/cur_prog_cnt` - response body](../../9-task/2-post/1-cur_prog_cnt.md))</br>
		`(2) Python 代码片段` : python 中 `post` 请求的代码。  
抱歉，我无法处理这个请求。
[__SOURCE](0-intro/4-api-test/2-web-browser.md)
#### 0.4.2 从网络浏览器调用 API  

###### a. 发出简单的 `GET` 请求

`get` 请求可以通过网络浏览器更简单和快速地检查。步骤如下：
1. 打开网络浏览器
2. 在地址栏中输入 `get` 请求的服务器端 URL。
	- 服务器端 URL 以 `http://<IP 地址 ${cont_model} 控制器>:<http 通信端口>` 开头，后面跟着您要提取的信息的路径和查询。
	- 例如) ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
3. 该 URL 的页面打开并输出响应，如下所示。
	```json
	{
		"_type" : "JObject",
		"val" : -99
	}
	```

<br>

###### b. 使用 `extension` 调用 API
如果您使用 Chrome 或 Edge 浏览器，可以通过 Chrome 扩展程序测试除 `get` 请求以外的 API。  
以下扩展程序是许多开发人员在全球使用的 API 测试工具。
- Chrome 扩展程序 : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)  

通过这个程序，您可以像 `postman` 一样轻松调用各种 API。

<img src="../../_assets/06_Talend_api_tester.png" style="max-height: 80vh;">

<blockquote>

`(1) 请求/场景` : 您可以设置是测试对单个 API 的调用，还是创建多个 API 的场景并依次进行测试。<br>
`(2) 请求` : 输入您的请求。  
`(3) 响应` : 您可以检查对您请求的响应。  
`(4) 历史` : 打印请求历史。   
`(5) 侧边历史标签` : 此标签允许您检查比 `(4)` 中的请求历史列表更多的历史，可以打开和关闭。

</blockquote>
[__SOURCE](0-intro/5-caution/README.md)
## 0.5 注意事项

{% hint style="caution" %}

本节概述了可能导致机器人控制器严重错误的关键预防措施。

在使用 API 之前，请确保您充分理解这些内容。

{% endhint %}


0.5.1. [保持连接与关闭连接](./1-http-connection.md)
[__SOURCE](0-intro/5-caution/1-http-connection.md)
#### 0.5.1. 保持连接 vs 关闭连接

{% hint style="caution" %}

对于机器人控制器，使用 `关闭 (close)` 连接类型的重复API请求可能会导致高CPU负载，可能会导致机器人意外停止。

如果您的应用涉及频繁的API调用，请遵循以下说明，并使用 **保持连接** 方法实施它们。

{% endhint %}

<br>

###### 1-1. 比较两种HTTP连接方法

<div style="max-width: fit-content">

| | 关闭 | 保持连接 |
|--| ----- | ----- |
|推荐的HTTP版本| HTTP/1.0 | HTTP/1.1 |
|特征| 多个连接 | 持久连接 |

<img src="../../_assets/07_http_connection.png" style="max-height: 37vh;">

</div>

- `关闭 (close)` 连接类型为每个请求和响应建立并终止一个连接。<br>
  这个过程会导致延迟和资源使用增加，给服务器和客户端带来很大的负担。

- ${cont_model} 使用HTTP/1.1，默认使用保持连接，除非明确覆盖。

- 请参考下面的示例代码，确保频繁调用的API使用保持连接实现，而不是关闭方法。

<br>

###### 1-2. 示例代码

- 在 `关闭 (close)` 和 `keep-alive` 连接之间切换很简单，可以通过修改请求头来完成。

- 关闭连接
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
- 保持连接
  <div style="max-width:fit-content">

	```python
	import requests
	import time

	BASE_URL = "http://192.168.10.150:8888"
	URI = "/project/robot/po_cur"
	URL = BASE_URL + URI

	# 默认连接是保持连接
	response = requests.get(URL)
	```
	</div>
- 数据包捕获比较 - 连接头信息 <br>
	<img src="../../_assets/08_packet_compare.png" style="max-width: 80vw;"><br>
	左) 保持连接，右) 关闭

<br><br>

参考文献
  1) [HTTP/1.1 持久连接](https://datatracker.ietf.org/doc/html/rfc2616#section-8)
[__SOURCE](1-release-note/README.md)
# 1. 发布说明

- 基于 COM 版本文档记录了 API 更改。  
- 如果您希望使用在当前控制器版本之上的更高版本操作的 API，则需要进行版本升级。  
- 发布信息

	<div style="max-width:31vw;">

	|COM 版本|发布安排|链接|
	|:--:|:--:|:--:|
	|v60-34.00| 定于 2026 年 3 月 _(待定)_|[🔗](60-34.md)|
	|v60-32.00| 2025.11 |[🔗](60-32.md)|
	|v60-30.00|2025 年 3 月|[🔗](60-30.md)|
	|v60-28.00|2024 年 8 月|[🔗](60-28.md)|

	</div>
[__SOURCE](1-release-note/60-34.md)
# V60.34-00

<link rel="stylesheet" href="../_assets/style.css">

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  发布说明 - v60.34-00
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
    预览
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
  ✨ 新功能
</h4>

- joint_states<br>
  - 获取机器人的当前关节角度（°）、速度和扭矩的API。  
    它支持查询所有轴或选择性查询指定范围的轴。
- joint_traject_insert_point<br>
  - 一个API，依次将下一个目标关节点添加到活动关节轨迹中，  
    使机器人能够连续关节运动。

<br><br>

<div style="
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
  🔧 改进与变更
</div>

- none

<br><br>

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
  ❌ 废弃
</div>

- none

<br><br>

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
  📌 更新的 API 列表
</div>

- ✨ [<b style="color: #4CAF50">get</b>] [joint_states](../5-robot/1-get/8-joint_states.md)
- ✨ [<b style="color: #FF9800">帖子</b>] [joint_traject_insert_point](../5-robot/2-post/9-joint_traject_insert_point.md)
[__SOURCE](1-release-note/60-32.md)
# V60.32-00

<link rel="stylesheet" href="../_assets/style.css">

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
发布说明 - v60.32-00
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
    新
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
  ✨ 新功能
</h4>

- joint_traject_init<br>
  - 添加了一个缓冲区索引初始化 API，必须在**<u>强制</u>**请求新的步骤轨迹时执行  
    当机器人处于停止状态
- joint_traject_insert_points<br>
  - 添加了一个 API，接收来自外部源的多个轨迹点  
    并将其应用于机器人运动
- joint_traject_buf_avail<br>
  - 添加了一个 API，以查询当前可用的缓冲区数量  
    当请求来自外部源的轨迹时
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
  🔧 改进与变更
</div>

- set_cur_pc_idx<br>
  - 添加验证以防止在程序播放时调用
- emergency_stop<br>
  - 调用时显示通知弹出窗口
- emergency_stop_test<br>
  - 修复请求立即停止（类别 0）时返回 403 BAD Request 的错误
  - 通过验证案例细化错误代码
  - 调用时显示通知弹出窗口
- execute_move<br>
  - 修复与响应相关的错误并细化错误代码
  - 添加验证以允许仅在远程模式下操作
- motor_on API<br>
  - 修复在远程模式下程序播放期间切换到手动模式后 motor_on 无法正常工作的问题  
  - 添加验证以允许仅在远程模式下操作
- start<br>
  - 修复在远程模式下无法调用的问题
  - 添加验证以允许仅在远程模式下操作
- stop<br>
  - 修复在远程模式下无法调用的问题
  - 调用时显示通知弹出窗口
- reset<br>
  - 修复在远程模式下无法正确操作的问题
- 修复在以下顺序调用 API 时程序执行多次的错误<br>
  - Motor On → R0 → 删除作业 → 上传作业 → 重新加载作业 → 设置当前 PC → 启动机器人

<br><br>

<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px; 
  display: inline-block; 
  color: white;
```html
<div style="
  padding: 2px 8px; 
  font-size: 14px; 
  font-weight: bold; 
  margin: 8px 0; 
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
">
  ❌ 已弃用
</div>

- none

<br><br>

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
  📌 更新的 API 列表
</div>

- ✨ [<b style="color: #4CAF50">get</b>] [joint_traject_buf_avail](../5-robot/1-get/7-joint_traject_buf_avail.md)
- ✨ [<b style="color: #FF9800">post</b>] [joint_traject_init](../5-robot/2-post/7-joint_traject_init.md)
- ✨ [<b style="color: #FF9800">post</b>] [joint_traject_insert_points](../5-robot/2-post/8-joint_traject_insert_points.md)
- 🔧 [<b style="color: #FF9800">post</b>] [set_cur_pc_idx](../9-task/2-post/6-set_cur_pc_idx.md)
- 🔧 [<b style="color: #FF9800">post</b>] [emergency_stop_test](../5-robot/2-post/6-emergency_stop_test.md)
- 🔧 [<b style="color: #FF9800">post</b>] [execute_move](../9-task/2-post/8-execute_move.md)
- 🔧 [<b style="color: #FF9800">post</b>] [motor_on](../5-robot/2-post/1-motor-on.md)
- 🔧 [<b style="color: #FF9800">post</b>] [start](../5-robot/2-post/2-start-stop.md)
- 🔧 [<b style="color: #FF9800">post</b>] [stop](../5-robot/2-post/2-start-stop.md)
- 🔧 [<b style="color: #FF9800">post</b>] [reset](../9-task/2-post/2-reset.md)
```
[__SOURCE](1-release-note/60-30.md)
# V60.30-00

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  📝 发布说明 - v60.30-00 
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
  ✨ 新功能
</h4>


- emergency_stop 
  - 添加了状态检查请求的API。
  - 添加了与紧急停止按钮功能相同的API。


<br><br>

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
  🔧 改进与更改
</div>

- emergency_stop_test 
  - 与v60.28-00中的emergency_stop相同。
- task reset 
  - 现在使用R代码0。
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
  ❌ 已弃用
</div>

- <font style="color: #E82E8C">motor off</font> 
  - 此 API 的设计是考虑到 HRSpace 环境。为了避免在现实环境中造成混淆，它已被弃用并替换为紧急停止 API。  
- <font style="color: #E82E8C">task reset</font> 
  - 以下 URI 不再支持 
    - /project/context/tasks/reset
    - /project/context/tasks[{task index}]/reset path


<br><br>

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
  📌 API 列表
</div>  

- ✨ \[<b style="color: #4CAF50">get</b>\] [emergency_stop](../5-robot/1-get/6-emergency_stop.md)  
- ✨ \[<b style="color: #FF9800">post</b>\] [emergency_stop](../5-robot/2-post/5-emergency_stop.md)  
- 🔧 \[<b style="color: #FF9800">post</b>\] [emergency_stop_test](../5-robot/2-post/6-emergency_stop_test.md)
- 🔧 \[<b style="color: #FF9800">post</b>\] [task_reset](../9-task/2-post/2-reset.md)
- ❌ ~~\[<b style="color: #FF9800">post</b>\] motor_off~~  
[__SOURCE](1-release-note/60-28.md)
# V60.28-00

<h4 style="display: inline-flex; align-items: center; gap: 8px;">
  📝 发布说明 - v60.28-00 
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
  ✨ 新功能
</h4>

- emergency_stop - 添加了紧急停止API。支持在指定时刻通过输入如step_no和stop_at等值对特定类别执行紧急停止。
- execute_move - 添加了一个用于移动到指定姿态的API。  
- execute_cmd - 添加了一个用于在${cont_model} COM中执行控制台命令的API。  


<br><br>

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
  🔧 改善与变更
</div>

- 无

<br><br>

<div style="
  background: linear-gradient(135deg, rgb(180, 40, 20), rgb(110, 25, 9)); 
  border-radius: 5px;
```html
  ❌ 已弃用
</div>

- 无

<br><br>

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
  📌 API 列表
</div>

- ✨ \[<b style="color: #FF9800">post</b>\] [emergency_stop](../5-robot/2-post/6-emergency_stop_test.md)  
- ✨ \[<b style="color: #FF9800">post</b>\] [execute_move](../9-task/2-post/8-execute_move.md)
- ✨ \[<b style="color: #FF9800">post</b>\] [execute_cmd](../10-console/2-post/1-execute_cmd.md)
```
[__SOURCE](2-version/README.md)
# 2. `version`

- 检查当前的 API 版本或机器人控制系统版本。
[__SOURCE](2-version/1-get/README.md)
## 2.1 `version/get`

- 发送GET请求以获取当前API版本或机器人控制器系统版本的信息。
- 通过为每个API设置正确的路径参数和查询参数来接收响应。
[__SOURCE](2-version/1-get/1-api_ver.md)
#### 2.1.1 `api_ver`

##### 描述

在少数情况下，您的 API 的架构版本可能会更改与控制器的通信方式或其数据结构。  
这可能导致客户端程序出现问题，因此需要通过相应的功能进行确认。  
如果每个 API 函数的架构版本发生更改，将通过描述页面上的单独标注进行通知。  

- `GET` : 获取 Open API 版本号

##### path-parameter

```python
GET /api_ver
```

##### response-body

- Open API 版本号
- 初始 ${cont_model} Open API 是基于 `version 5` 编写的文档。

##### 示例

```python
request url:
GET /api_ver

response-body:
5
```

Python 脚本示例

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
[__SOURCE](2-version/1-get/2-sysver.md)
#### 2.1.2 `sysver`

##### 描述

- `GET` : 获取机器人控制器系统的软件版本。

##### 路径参数

```python
GET /versions/sysver
```

##### 响应体

modules : 模块版本信息数组
  - 模块版本信息 :
    - `名称 (name)` : 模块名称
		|模块名称|描述|
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
$python test.py  
{'modules': [{'build-date': '2000年01月00日', 'build-time': '00:00:00' ...
[__SOURCE](3-project/README.md)
# 3. `project`

- 读取条件设置、项目信息和工作文件信息。
- 您可以重新加载更新的工作文件或删除特定的工作文件。
[__SOURCE](3-project/1-get/README.md)
## 3.1 `project/get`

- 发送 GET 请求以获取条件设置、项目信息和作业文件信息。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](3-project/1-get/1-rgen.md)
#### 3.1.1 `rgen`

##### 描述

- `GET`: 在控制器中获取远程一般信息。

##### 路径参数

```python
GET /project/rgen
```

##### 响应体

###### 1) 模式
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0`: 手动 <br> `翻译 (1)`: 手动, 系统设置 <br>`翻译 (3)`: 自动, 1循环 <br> ` (4)`: 自动, 持续 (循环)|`int`|手动/自动模式|
|`enable_state`|`0` 字节(`LSB`): 电机开启 (0: 开 / 1: 关 / 2: 繁忙) <br> `翻译 (1)`: TP 启用 (死 man's) 开关 (0: 关闭 / 1: 开)<br>`翻译 (2)`: 机器锁 (0: 关闭 / 1: 开)<br>`翻译 (3)`: 枪锁 (0: 关闭 / 1: 开)<br>` (4)`: 枪 (0: 关闭 / 1: 开)|`int`||
|`is_playback`|`0`: 暂停 <br>`翻译 (1)`: 播放|`int`||
|`is_remote_mode`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否为远程模式|
|`is_ext_start`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否为外部启动|
|`is_ext_prog_sel`|`0`: 假 <br> `翻译 (1)`: 真|`int`|是否选择外部程序|

<br>

###### 2) 当前程序计数器
这是教导挂件 JOB 面板上条形光标在手动模式或自动模式中的位置。这是当前执行的语句或编辑的目标位置。
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|当前程序编号|
|`cur_step_no`|`int`|当前步骤编号|
|`cur_func_no`|`int`|当前功能编号|

<br>

###### 3) 移动程序计数器
这是机器人在播放过程中移动的目标步骤。
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|移动程序编号|
|`mov_step_no`|`int`|移动步骤编号|
|`mov_func_no`|`int`|移动功能编号|

<br>

###### 4) 速度
|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|手动模式的 Jog 速度等级 (1~8)|
|`manual_spd_max`|`int`|手动模式下的最大速度 (mm/sec)|
|`auto_spd`|`int`|自动模式播放速度 (%)|
|`jog_inch_status`|`int`|jog 微调状态 (0:关闭/ 1:开启)|
|`step_execute_unit_status`|`int`|StepFWD 执行单元 (运行到)<br>0: Cmd <br>1: Step<br>2: 结束 |
|`cont_path`|`int`|连续运动模式 (0~2)|

<br>

##### 示例
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
[__SOURCE](3-project/1-get/2-jobs_info.md)
#### 3.1.2 `jobs_info`

##### 描述

- `GET` : 获取作业程序的信息。

##### 路径参数

```python
GET /project/jobs_info
```

##### 响应主体

- [作业文件信息](../../99-schema/jobs_info.md)

##### 示例

<blockquote>

```python
请求 URL:
GET /project/jobs_info

响应主体:
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
Python脚本示例

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
[__SOURCE](3-project/2-post/README.md)
## 3.1 `project/post`

- 发送一个POST请求以进行条件设置、项目信息和作业文件信息。
- 您必须为每个API编写正确的请求体。
[__SOURCE](3-project/2-post/1-reload_updated_jobs.md)
#### 3.2.1 `reload_updated_jobs`

##### 描述

- `POST` : 发送请求以更新工作文件。
- 当通过 FTP 将作业文件传输到控制器时，必须通过相应的 API 发出重载请求，以便传输的作业文件能够反映在内存中。

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

- 有关响应 HTTP 状态代码，请参见 [这里](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200)。
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

[__SOURCE](3-project/2-post/2-jobs-delete_job.md)
#### 3.2.2 `delete_job`

##### 描述

- `POST` : 发送请求以删除工作文件。

##### 路径参数

```python
POST /project/jobs/delete_job
```

##### 请求体

```json
{
    "fname": "0001.job"
}
```

##### 示例

```json
请求 URL:
POST /project/jobs/delete_job

请求体: 
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
响应：200 
```
[__SOURCE](4-control/README.md)
# 4. `control`

- 应用控制器的设置并处理输入/输出值。
- 它涵盖系统输入/输出、数字输入/输出、条件设置和用户坐标系统的信息。

<br>
[__SOURCE](4-control/1-get/README.md)
## 4.1 `control/get`

- 发送 GET 请求以获取控制器设置信息和输入/输出值。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](4-control/1-get/1-op_cnd.md)
#### 4.1.1 `op_cnd`

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
[__SOURCE](4-control/1-get/2-ucss-ucs_nos.md)
#### 4.1.2 `ucss/ucs_nos`

##### 描述

- `GET` : 获取当前使用的用户坐标系统列表。
- 打印通过 `system > 2: Control parameter > 6: Coordinate registration` 注册的用户坐标系统列表。

##### 路径参数

```python
GET /project/control/ucss/ucs_nos
```

##### 示例

```python
请求 URL:
GET /project/control/ucss/ucs_nos

响应主体:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python 脚本示例

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
[__SOURCE](4-control/2-post/README.md)
## 4.2 `control/post`

- 发送一个 POST 请求以获取控制器的设置信息和输入/输出值。
- 您必须为每个 API 编写正确的请求体。
[__SOURCE](4-control/3-put/README.md)
## 4.3 `control/put`

- 发送针对控制器设置信息和输入/输出值的 PUT 请求。
- 您必须为每个 API 编写正确的请求主体。
[__SOURCE](4-control/3-put/1-op_cnd.md)
#### 4.3.1 `op_cnd`

##### 描述

- `PUT` : 更改机器人的状态设置值。
- 如果您在 TP 中打开 `条件设置窗口(cond.set)` 并请求相应的方法，  
则必须关闭并重新打开窗口以使值生效。

##### 路径参数

```python
PUT /project/control/op_cnd
```

##### 请求体

- [条件设置参数](../../99-schema/op_cnd.md)


##### 示例

```python
请求网址:
PUT /project/control/op_cnd

请求体:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}
```

Python 脚本示例

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
```
$python test.py
响应：200 
```
[__SOURCE](5-robot/README.md)
# 5. `机器人 (robot)`

- 您可以检查机器人和工具数据的远程控制和监控。
- 它涵盖电机开/关、机器人姿态、工具、手动坐标系统等。
[__SOURCE](5-robot/1-get/README.md)
## 5.1 `robot/get`

- 发送 GET 请求以获取机器人和工具数据。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](5-robot/1-get/1-motor_on_state.md)
#### 5.1.1 `motor_on_state`

##### 描述

`motor_on_state`

- `GET` : 获取电机开启状态。

##### 路径参数

```python
GET /project/robot/motor_on_state
```

##### 响应体

- val :
  - `0` : 开
  - `翻译 (1)` : 关
  - `翻译 (2)` : 忙 (过渡状态)

##### 示例
```python
请求 URL:
GET /project/robot/motor_on_state

响应体:
{
    "_type" : "JObject",
    "val" : 1
}
```

Python 脚本示例

```python
# test.py
import requests

def get_motor_on_state() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on_state'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(f"电机开启状态: {get_motor_on_state()['val']}")
```
```sh
$python test.py
电机开启状态: 1
```

[__SOURCE](5-robot/1-get/2-po_cur.md)
#### 5.1.2 `po_cur`

##### 描述

- `GET` : 获取机器人当前的姿态。

##### 路径参数

```python
GET /project/robot/po_cur
```

##### 查询参数

- `task_no` : 任务编号 (0~7)。
  - 未指定 : 应用任务 0。
  - &gt;=0 : 如果未指定 mechinfo，将应用当前任务的 mechinfo。
- `crd` :  
  - 未指定 : 获取所有 tcp、轴和编码器。
  - <0 : 遵循当前记录的坐标系统。
  - &gt;=0 : [坐标系统](../../99-schema/crdsys.md)
- `ucrd_no` : 用户坐标系统编号（仅在 crd 为用户时指定。）
- `mechinfo` : [机构信息](../../99-schema/mechinfo.md)

##### 响应体

- [姿态信息](../../99-schema/pose.md)


##### 示例

具有 6 个机器人轴（j1~j6）+ 1 个驱动轴（j7）+ 2 个定位器轴（j8, j9）的系统示例。

- 仅获取机器人的基础坐标

```python
请求网址：
GET /project/robot/po_cur?crd=0&mechinfo=1

响应体：
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
请求 URL:
GET /project/robot/po_cur?crd=2&mechinfo=-1

响应正文:
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

- 获取位置器 2 轴的轴坐标（即机制 M2）

```python
请求 URL:
GET /project/robot/po_cur?crd=2&mechinfo=2

响应正文:
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
[__SOURCE](5-robot/1-get/3-cur_tool_data.md)
#### 5.1.3 `cur_tool_data`

##### 描述

- `GET` : 获取机器人的当前工具数据。

##### 路径参数

```python
GET /project/robot/cur_tool_data
```

##### 响应正文

- val : [工具数据](../../99-schema/tool_data.md)

##### 示例

```python
请求网址:
GET /project/robot/cur_tool_data

响应正文:
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
{'_type': '工具', 'x': 0.0, 'rx': 0.0, 'y': 0.0, 'ry': 0.0, 'z': 0.0, 'rz': 0.0, 'cy': 0.0, 'mass': 20.0, 'cx': 100.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'bias_2': 0.0, 'mass_esti': 20.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```
[__SOURCE](5-robot/1-get/4-tools.md)
#### 5.1.4 `tools`

##### 描述

- `GET` : 获取机器人的所有工具信息。仅获取 T0 到 T31 之间存在的工具。

##### 路径参数

```python
GET /project/robot/tools
```

##### 响应体

- t_0 : [工具数据](../../99-schema/tool_data.md)
- t_1 : 工具数据
- t_2 : 工具数据  
...
- t_31 : 工具数据

##### 示例

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
{'_type': '工具', 't_31': {'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_0': {'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0, 'load_rate': {'_type': 'JObject', 'high_load_mode': -11, 'moment_rate': 0, 'inertia_rate': 0, 'mass_rate': 0}}, 't_1': {'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}, 't_15': {'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}}
```
[__SOURCE](5-robot/1-get/5-tools_t.md)
#### 5.1.5 `tools/t_{number}`

##### 描述

- `GET` : 这是一个接收特定工具设置信息的功能。

##### 路径参数

```python
GET /project/robot/tools/t_{number}
```

##### 响应主体

- [工具数据](../../99-schema/tool_data.md)

##### 示例

```python
请求网址:
GET /project/robot/tools/t_1

响应主体:
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
{'_type': '工具', 'rx': 0.0, 'x': 0.0, 'ry': 0.0, 'y': 0.0, 'rz': 0.0, 'z': 0.0, 'mass': 20.0, 'cx': 100.0, 'cy': 0.0, 'cz': 65.0, 'ixx': 0.059, 'iyy': 0.061, 'izz': 0.075, 'bias_0': 0.0, 'bias_1': 0.0, 'mass_esti': 20.0, 'bias_2': 0.0, 'bias_3': 0.0, 'bias_4': 0.0, 'bias_5': 0.0}
```
[__SOURCE](5-robot/1-get/6-emergency_stop.md)
#### 5.1.6 `emergency_stop`

##### 描述

- `GET` : 检索关于紧急停止按钮被按下状态的信息。  
- 当通过 API 请求紧急停止时，控制器在接收到 API 请求的那一刻返回值 1。  

##### 路径参数

```python
GET /project/robot/emergency_stop
```

##### 响应主体

- 0: 紧急按钮已释放
- 1: 紧急按钮已按下 

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
[__SOURCE](5-robot/1-get/7-joint_traject_buf_avail.md)
#### 5.1.7 `joint_traject_buf_avail`

##### 描述
- 支持版本 : `60.32-00` &uparrow;
- `GET` : 返回轨迹缓冲区的可用大小。
- 在连续请求轨迹时，必须使用此函数以确保每个轨迹请求的大小不超过可用缓冲区空间。

##### 路径参数

<div style="width: fit-content;">

```python
GET /project/robot/trajectory/joint_traject_buf_avail
```

##### 响应体

- val: 可用缓冲槽的数量（最大：2048）

##### 状态代码
  - 200 : 请求成功
  - 403 : 请求失败
    - 当调用不支持的 API 时返回

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
{'val': 2048}
```
</div>
[__SOURCE](5-robot/1-get/8-joint_states.md)
#### 5.1.8 `joint_states`

##### 描述
- 支持的版本: `60.34-00` ↑
- `GET`: 获取机器人的当前关节状态。
- 返回 **关节角度（位置，°），速度和扭矩（努力）** 信息，每个关节均有。  
  你可以查询所有轴或选择性查询指定范围的轴。

##### 路径参数

<div style="width: fit-content;">

```python
GET /project/robot/joint_states
````

</div>

##### 查询参数

* * 如果未指定参数，则查询所有关节。
* jno_start（可选）

  * 开始查询的关节索引（基于1）
* jno_n（可选）

  * 要查询的关节数量

##### 响应

1. 状态码

   * 200 : 正常
   * 400 : 请求错误

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
请求 URL:
GET /project/robot/joint_states?jno_start=1&jno_n=6

响应主体:
{
    "position": [0.0, 10.5, -20.3, 45.0, 0.0, 30.0],
    "velocity": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "effort": [1.2, 1.0, 0.8, 0.5, 0.3, 0.2]
}
```

Python 脚本示例

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
## 5.2 `robot/post`

- 发送POST请求以获取机器人和工具数据。
- 您必须为每个API编写正确的请求主体。
[__SOURCE](5-robot/2-post/1-motor-on.md)
#### 5.2.1 `motor_on`

##### 描述

- `POST` : 执行电机开启。
- `motor_off` API 已被弃用，并从 [v60.30-00](../../1-release-note/60-30.md) 开始不再支持。

##### 路径参数

```python
POST /project/robot/motor_on
```

##### 请求体

```json
{}
```

##### 响应

1. 状态码

- 200 : OK
- 400 : 错误请求
  - 请求体未通过验证
- 403 : 禁止
  - 在非远程模式下尝试进行 API 请求（自 v60.30-09 起生效）。
- 404 : 未找到


2. 响应体

```json
{
    "_type": "JObject"
}
```

3. 错误代码

- -38500 : API 请求被拒绝，因为系统不在远程模式

##### 示例

```python
POST /project/robot/motor_on

request-body:
{}
```
Python 脚本示例

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"电机开启响应: {post_motor_on()}")
```
```sh
$python test.py
电机开启响应: 200
```
[__SOURCE](5-robot/2-post/2-start-stop.md)
#### 5.2.2 `start / stop`

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

- 200 : 成功
- 400 : 错误请求
   - 请求体未通过验证。
- 403 : 禁止
    - 在非远程模式下尝试了 `开始 (start)` 请求（自 v60.30-07 起生效）。
- 404 : 未找到

2. response-body

```json
{
    "_type": "JObject"
}
```
3. 错误码

- -38500: API 请求被拒绝，因为控制器不在远程模式下

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

print(f"启动响应: {post_start()}")
print(f"停止响应: {post_stop()}")
```
```sh
$python test.py
启动响应: 200
停止响应: 200
```
[__SOURCE](5-robot/2-post/3-tool_no.md)
#### 5.2.3 `tool_no`

##### 描述

- `POST` : 设置当前工具编号。

##### path-parameter

```python
POST /project/robot/tool_no
```

##### request-body

- `val` : 工具编号
  - `robot tools` : `0` ~ `31`
  - `stationary tool` : `0` ~ `翻译 (3)`

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
[__SOURCE](5-robot/2-post/4-crd_sys.md)
#### 5.2.4 `crd_sys`

##### 描述

- `POST` : 设置当前的关节坐标系。

##### 路径参数

```python
POST /project/robot/crd_sys
```

##### 请求体

- [坐标系](../../99-schema/crdsys.md)

##### 响应体

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

请求体
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
响应：200
```
[__SOURCE](5-robot/2-post/5-emergency_stop.md)
#### 5.2.5 `emergency_stop`

- <b style="color:orange"> 对于版本低于 ***<u>60.30-00</u>*** 的，请参考 ***<u>[emergency_stop_test](./6-emergency_stop_test.md)</u>*** 而不是 emergency_stop。 </b>  

##### 描述

- 支持版本 : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  
- 应用与按下紧急停止按钮相同的减速曲线。  
- 由于网络延迟或请求处理时间，API 的响应速度可能比物理按钮慢。  


##### 路径参数

```python
POST /project/robot/emergency_stop
```

##### 请求体
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
响应: 200
```
[__SOURCE](5-robot/2-post/6-emergency_stop_test.md)
#### 5.2.6 `emergency_stop_test`

- <b style="color:orange"> 此 API 在版本 60.28-00 之前用作 `emergency_stop` API。 </b>  

##### 描述

- 支持版本 : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  

##### 路径参数


<div style="max-width:fit-content">


```python
POST /project/robot/emergency_stop_test
```

</div>

##### 请求体

  <div style="max-width:fit-content">

-  |key|type|contents|validation|
	|---|---|---|---|
	|`step_no`| int | 紧急停止的目标步骤编号，当前作业的总步骤编号内 | 1 ~ 999 |
	|`stop_at`| double | 设置指定位置的停止百分比 | 1 ~ 100 |
	|`stop_at_corner`| int | 0: 正常停止, 1: 角落停止 | 0 或 1 |
	|`category`| int | 0: 立即停止, 1: 减速停止, 2: 暂停 | 0 或 1 或 2 |

- `0: 立即停止`  
  &rightarrow; 与控制器在机器人播放期间关闭时相同。电机在停止后关闭。  

    {% hint style="warning" %}

    规格变更

    * V60.29-08 ~ V60.30-10：立即停止 API 只能在目标步骤调用。  
    * V60.32-00 及以后版本：立即停止 API 可以在任意步骤调用。

    {% endhint %}

- `1: 减速停止`  
	&rightarrow; 表现得仿佛按下了紧急停止按钮。电机在停止后关闭。   
- `2: 暂停`  
	&rightarrow; 暂时停止机器人运动。电机在停止后不关闭。  


</div>

##### 状态码

- 200 : 请求成功    
- 400 : 请求失败     
	- 请求体未通过验证    
- 403 : 请求失败    
	- 请求了未提供服务的 API  
##### 使用示例  

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

Python 脚本示例

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

[__SOURCE](5-robot/2-post/7-joint_traject_init.md)
#### 5.2.7 `joint_traject_init`

##### 描述

- 支持的版本 : `60.32-00` &uparrow;
- `POST` : 初始化轨迹缓冲区。
- 在请求新的轨迹时，若机器人处于停止状态，用户必须清除之前存储的轨迹。
- 例如)
  - 请求 traj1 → 在运动过程中发生错误 → 必须使用 `joint_traject_init` 清除缓冲区 → 请求 traj2 <br>
  : 如果错误时的轨迹数据仍然保留在缓冲区，未清除缓冲区直接请求 traj2 可能会导致另一个错误。
- 如果在通过 [joint_traject_insert_points](./8-joint_traject_insert_points.md) API 执行轨迹时调用此 API，缓冲区将立即更新。
  - 从缓冲区中移除之前存储的轨迹点可能会导致机器人停止并触发错误。请谨慎使用。


##### 路径参数

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_init
```
</div>

##### 请求体

<div style="width: fit-content;">

- {}

</div>


##### 状态代码

- 200 : 请求成功
- 403 : 请求失败
  - 调用不支持的 API 时返回
  - `err_code` (<0): 初始化失败

##### 示例

<div style="width: fit-content;">

```joint_traject_init
POST /project/robot/trajectory/joint_traject_init

request-body
{}
```
Python脚本示例
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
        print(f"[信息] 初始化成功: 状态={response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[错误] 初始化轨迹缓冲失败: {e}")
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
[信息] 初始化成功: 状态=200
```
</div>
[__SOURCE](5-robot/2-post/8-joint_traject_insert_points.md)
#### 5.2.8 `joint_traject_insert_points`

##### 描述

- 支持的版本 : `60.32-00` &uparrow;
- `POST` : 将由多个点组成的轨迹发送到机器人控制器。
  - 多个关节轨迹点存储在控制器的内部缓冲区，并反映在机器人的运动中。

---

##### 注意事项

1. 该 API 仅在程序处于 <u>运行状态</u> 时有效。
   - 例如) 只有在程序以自动模式播放时，API 才能工作。
   - 如果在未满足此条件的情况下发出请求，系统将返回错误。  
	 "[\[E01554\] 外部命令移动不在可执行状态](https://hr-alarms.web.app/#/${cont_model:lower}/zh/E01554)"

2. 一次可以 POST 的最大轨迹点数为 **<u>2048</u>**。
   - 存储轨迹点的缓冲区的最大大小为 **<u>2048</u>**。

3. 请求的轨迹点在反映到运动之前不会被丢弃，机器人将继续移动，直到到达相应的位置。
   - 缓冲区中的轨迹在运动执行之前保持不变，除非通过 [joint_traject_init](./7-joint_traject_init.md) API 明确清除。

4. 根据轨迹，可能会出现 "[\[E159\] 轴速限制值超出](https://hr-alarms.web.app/#/${cont_model:lower}/zh/E159)" 错误。如果发生此错误，机器人将停止。

5. 该 API 处理由 **<u>两个或更多点</u>** 组成的轨迹。

6. 使用附加轴时，请注意 **<u>轴坐标值的单位</u>**。

---

##### 路径参数

<div style="width: fit-content;">

```joint_traject_insert_points
POST /project/robot/trajectory/joint_traject_insert_points
```
</div>

##### 请求主体

<div style="width: fit-content;">

- 	|               键 |       类型      | 描述                          | 备注                                           |
	| ----------------: | :-----------: | --------------------------- | -------------------------------------------- |
	|     `joint_names` | array(string) | 轨迹的关节名称列表          | 例如，对于一个 6 轴机器人："j1" 到 "j6"， **顺序必须精确** |
	|          `points` |     object({})    | 要执行的轨迹点列表      | 	键： "point_n"，其中 n 从 1 开始。 **至少需要 2 个点**   |
	|       `positions` | array(double) | 每个关节的目标位置以弧度表示,<br>对于 **附加轴，请注意坐标单位**)| 位置必须根据当前的关节数量进行指定。 |
	| `time_from_start` |     number    | 点的开始时间（以秒为单位） | 必须为 **<u>0.0</u>** 或 **<u>大于</u>**，且大于前一个点。 |
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

##### 状态码

- 200 : 请求成功
- 403 : 请求失败
  - 当调用不支持的API时返回

##### 错误代码（响应 403）

<div style="width: fit-content;">

- 	| 错误代码     | 错误常量名称     | 描述                                           |
	| ---------- | --------------------------- | ----------------------------------------------------- |
	| `-2`       | `ERR_MISSING_JOINT_NAMES`   | 如果 joint_names 字段缺失 |
	| `-3`       | `ERR_INVALID_JOINT_NAMES`   | 如果 joint_name 格式无效（例如，"x1"），请求的关节数量与机器人当前的关节数量不匹配，或关节名称顺序错误。<br>（例如，["j1", "j3", "j2", ..., "j6"]） |
	| `-4`       | `ERR_MISSING_POINTS`        | 如果 points 字段缺失 |
	| `-5`       | `ERR_INVALID_POINTS`        | 如果 points 的值不是一个对象（即，不是一个 Python 字典），如整数或字符串 |
	| `-6`       | `ERR_TOO_FEW_POINTS`        | 如果轨迹点数量少于 2 |
	| `-7`       | `ERR_TOO_MANY_POINTS`       | 如果请求的轨迹点超过允许的 2048 个点 |
	| `-8`       | `ERR_POINTS_EXCEED_BUFFER`  | 如果请求的轨迹点超过当前可用的缓冲区空间 |
	| `-9`      | `ERR_INVALID_POINT_OBJECT`  | 如果 point_n 的值不是一个对象（即，不是一个 Python 字典，例：整数或字符串） |
	| `-10`      | `ERR_MISSING_POSITIONS`     | 如果 positions 字段缺失 |
	| `-11`      | `ERR_INVALID_POSITIONS`     | 如果 positions 不是一个数组，包含非数值的值，或其长度与关节数量不匹配 |
	| `-12`      | `ERR_MISSING_TIME`          | 如果 time_from_start 字段缺失        |
	| `-13`      | `ERR_INVALID_TIME`          | 如果 time_from_start 不是数字，少于 0，或在机器人运动时小于先前的值 |

</div>

##### 示例
**Ex1. 请求机器人静止时的轨迹**

<img src="../../_assets/09_online_trajectory_insert_points_single.png" style="max-height: 280px;">

1) 当请求轨迹时，请使用 [joint_traject_init](./7-joint_traject_init.md) API 清除包含先前轨迹的缓冲区。
2) 在请求轨迹之前，请检查程序是否正在运行，并确保有可用的缓冲区。
3) 请求一个由 **至少两个点** 组成的轨迹。
   - 将起始点 (`position of the starting point`) (point_1) 设置为机器人的 **当前位置信息**。
   - 将起始点 (`time_from_start of the starting point`) (point_1) 设置为 **0.0**。
   - 后续点的位置信息和 `time_from_start` 值应设置为可以从前一个点到达的值，然后再进行发布。
4) 如果机器人由于错误停止，请重新初始化并使用 joint_traject_init，然后继续执行步骤 1 到 3。

<br>

**Ex2. 请求包含不连续运动的轨迹（在轨迹之间包括停顿时间）**

<img src="../../_assets/10_online_trajectory_insert_points_two.png" style="max-height: 240px;">

1) 您必须根据示例 1 中指定的条件发送 traj1 和 traj2。
2) 请注意以下几点：
   - traj2 中 P1 的位置必须与 traj1 中 Pn 的位置相等。
   - traj2 中 P1 的 `time_from_start` 必须为 0.0。

<br>

**Ex3. 请求包含连续运动的轨迹**

<img src="../../_assets/11_online_trajectory_insert_points_continuous.png" style="max-height: 350px;">

1) 根据示例 1 中指定的条件发送 traj1。
2) 当机器人朝着 Pn-1 的位置移动时，您必须发送 traj2，并注意以下条件。
   - traj1 的 Pn 和 traj2 的 P1 必须配置为使机器人能够在它们之间平滑连续移动。
     - traj2 中 P1 的 `time_from_start` 必须是一个累积值，Δ (> 0) 大于 traj1 中最后一点 Pn 的 `time_from_start`。
     - traj2 中 P1 的位置必须在时间间隔 Δ 内可以从 traj1 的 Pn 到达。
   - 如果连续请求无法连续跟随的轨迹，可能会发生 "[\[E159\] 轴速度限制值超出](https://hr-alarms.web.app/#/${cont_model:lower}/zh/E159)" 错误。

<div style="width: fit-content;">

<br>

##### Python 脚本示例

- 将机器人移动到其默认姿态（基于 6 轴配置， [0, 90, 0, 0, 0, 0]）
- 创建并在 `自动模式` 下 `播放` 以下 0001.job 以进入程序播放状态。
- 0001.job
	```job
	Hyundai Robot Job File; { version: 1.6, mech_type: "-1()", total_axis: -1, aux_axis: -1 }
	  > wait di1
		end
	```
- 运行测试脚本（示例 3：请求连续运动中的两个轨迹）

	```
	条件 1)
	`traj_2` 中 `point_1` 的 `time_from_start` 必须是大于 `traj_1` 中 `point_2` 的累计值 Δ （> 0）。

	条件 2)
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
			print("程序未运行！")
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
					f"[{post_cnt}] elapsed_ms: {elapsed_ms:.3f} ms. 可用关节缓冲区: {n_jt_buff_avail - 1}/2048"
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
			# 从停止状态请求轨迹时初始化缓冲区
			post_init_trajectories(base_url)

			# 连续发布轨迹
			ret = post_trajectories(base_url, trajectories_go)
			time.sleep(1)
			ret = post_trajectories(base_url, trajectories_back)
			time.sleep(8)

	```
- ```sh
		$python test.py
		[0] 消逝时间(ms): 6.122 ms. 可用 jt 缓冲区: 2047/2048
		<Response [200]> {'_type': 'JObject'}
		[1] 消逝时间(ms): 3.997 ms. 可用 jt 缓冲区: 2046/2048
		<Response [200]> {'_type': 'JObject'}
		...
	```


</div>

[__SOURCE](5-robot/2-post/9-joint_traject_insert_point.md)
#### 5.1.9 `joint_traject_insert_point`

##### 描述
- 支持的版本: `70.00-00` ↑
- `POST`: **顺序附加下一个关节目标点**以执行关节轨迹。
- 通过重复调用此 API，可以构建连续的关节轨迹。

---

##### 注意事项

* [轴速度限制超出 (E159)](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E159)

  * 不要超过机器人的**最大允许速度和扭矩**以及辅助轴的限制。
  * 如果发出需要过大扭矩的命令，可能会发生以下**错误或警告**。
  * 减速机过扭矩
    * [E249](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E249), [E6402](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E6402), [E6403](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E6403)
  * 减速机过电流
    * [W153](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W153), [W181](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W181), [W182](https://hr-alarms.web.app/#/${cont_model:lower}/ko/W153)
  * 位置偏差错误
    * [E2630](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2630), [E2636](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2636), [E2638](https://hr-alarms.web.app/#/${cont_model:lower}/ko/E2638)
* 实际的错误或警告可能会根据**轴配置、负载条件和操作状态**而有所不同。

---

##### 路径参数

<div style="width: fit-content;">

```python
POST /project/robot/trajectory/joint_traject_insert_point
````</div>

---

##### 请求体

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
* 间隔

  * 增量添加点时使用的时间间隔
* 从开始时间

  * 从轨迹开始的累积时间
* 前瞻时间

  * 轨迹执行的前瞻时间
* 点

  * 目标关节角度数组（度）

---

##### 响应

1. 状态码

   * 200 : 成功
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 禁止
   * 404 : 未找到

---

##### 使用示例

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

##### Python 脚本示例

###### 先决条件
1. 将机器人移动到参考位置。
   (示例 - 对于6轴机器人：( 

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

  * 在逐步添加点时使用的时间间隔
* time_from_start

  * 从轨迹开始的累计时间
* look_ahead_time

  * 轨迹执行的前瞻时间
* point

  * 目标关节角度数组（度）

---

##### response

1. 状态代码

   * 200 : 成功
   * 400 : 错误请求

     * 请求体验证失败
   * 403 : 被禁止
   * 404 : 未找到

---
##### 使用示例

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

##### Python 脚本示例

###### 先决条件

1. 将机器人移动到参考姿态。
   (示例 - 对于一个 6 轴机器人: )`[0, 90, 0, 0, -90, 0]`)
2. 插入语句 ()
2. 在作业中插入语句 )`wait di1`。
3. 切换到自动模式并开始程序播放。
4. 在该状态下运行以下测试代码。

<div style="width: fit-content;">

```python
import time
import requests

BASE_URL = "http://192.168.1.150:8888"
# BASE_URL = "http://127.0.0.1:8888"  # hrspace


def get_joint_positions(session):
    path = "/project/robot/joints/joint_states"
    params = {"jno_start": 1, "jno_n": 6}
    return session.get(BASE_URL + path, params=params).json()["position"]


def insert_point(session, point, interval, look_ahead_time, time_from_start):
    path = "/project/robot/trajectory/joint_traject_insert_point"
    body = {
        "interval": interval,
        "look_ahead_time": look_ahead_time,
        "time_from_start": time_from_start,
        "point": point,
    }
    session.post(BASE_URL + path, json=body)


def fmt6(arr):
    return [f"{v:.6f}" for v in arr]


def main():
    interval = 0.002
    look_ahead_time = 0.010

    points = [
        [0.02,  89.98, 0.0, 0.0, -90.0, 0.0],
        [0.04,  89.96, 0.0, 0.0, -90.0, 0.0],
        [0.06,  89.94, 0.0, 0.0, -90.0, 0.0],
        [0.08,  89.92, 0.0, 0.0, -90.0, 0.0],
        [0.10,  89.90, 0.0, 0.0, -90.0, 0.0],
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
之前:  ['0.000000', '90.000000', '0.000000', '0.000000', '-90.000000', '0.000000']

[插入 1] 已确认  t=0.002000s
[插入 2] 已确认  t=0.004000s
[插入 3] 已确认  t=0.006000s
[插入 4] 已确认  t=0.008000s
[插入 5] 已确认  t=0.010000s

之后: ['0.072196', '89.928004', '0.000000', '-0.000574', '-90.000000', '-0.001393']
```

[__SOURCE](6-io_plc/README.md)
# 6. I/O PLC

- 读取或设置内置PLC的输入/输出值。
[__SOURCE](6-io_plc/1-get/README.md)
## 6.1 `io_plc/get`

- 发送对内置PLC的输入/输出值的GET请求。
- 通过为每个API设置正确的路径参数和查询参数来接收响应。
[__SOURCE](6-io_plc/1-get/1-relay-value.md)
#### 6.1.1 `get relay values`

##### 描述

- `GET` : 获取整个对象类型的继电器值。

##### 路径参数

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

##### 路径变量

[继电器表达式](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model})（小写字母）

* (`{obj_type}{obj_idx}_` 必须为 `di`、`do`、`x` 和 `y` 指定。剩余的 `relay_type` 不做规定。)

- `obj_type` : 对象类型
  - `fb`
  - `fn`

- `obj_idx` : 对象索引（fb: 0~9, fn: 0~63）

- `relay_type` : `di`、`do`、`x`、`y`、`m`、`字母s (s)`、`r`、`k`

##### 查询参数

- `st` : 起始字节索引（默认: 0）
- `len` : 字数（默认: 8）

##### 示例

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
请求 URL:
GET /project/plc/m/val_s32?st=32&len=4

响应主体:
[
    0,
    -2139095040,
    0,
    134217728
]
```

Python 脚本示例

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

[__SOURCE](6-io_plc/1-get/2-ios-dio.md)
#### 6.1.2 `ios/dio/{dio_val}`

##### 描述

- `GET` : 获取用户 IO 值。
- 请参考 [sio api](./3-ios-sio.md) 以获取系统输入/输出值。

##### 路径参数

<div style="width: fit-content;">

```python
GET /project/control/ios/dio/{dio_val}
```

</div>

##### 路径变量

- `dio_val` :
  - `di_val` : 获取输入 (di) 值。
  - `do_val` : 获取输出 (do) 值。

##### 查询参数

- `类型 (type)` : IO 值的类型
  - di 或 do : 位
  - dib 或 dob : 有符号字节
  - diw 或 dow : 有符号字 (2byte)
  - dil 或 dol : 有符号双字 (4byte)
  - dif 或 dof : 浮点数
- `blk_no` : 块号 (0~9)
- `sig_no` : 信号索引 (0~)

##### 响应

1) 状态码
   - 200 : OK
   - 400 : Bad Request
   - 403 : Forbidden
   - 404 : Not Found

2) 响应体
	- 正常响应时返回有符号十进制值
		<div style="width: fit-content;">

		```json
		{"_type" : "JObject", "val" : -99}
		
        ```

		</div>

##### 示例

- 获取 fb2.dob3 值。 (结果 : 0b11001000 = 0xc8 = -56)

<div style="max-width:fit-content;">

```python
request url:
GET /project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3

response-body:
{
    "_type" : "JObject",
    "val" : -56,
}
```

Python 脚本示例

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

    # MSB (最高有效位) -> LSB (最低有效位)
    return int(payload["val"]) & 0xFF


def lsb_first(u8: int) -> str:
    # LSB -> MSB
    return format(u8, "08b")[::-1]


do_u8 = extract_u8(get_do_val(2))
di_u8 = extract_u8(get_di_val(1))

print("do 值:", lsb_first(do_u8))
print("di 值:", lsb_first(di_u8))

```

```python
# (当 fb0.do18 = 1, fb0.do20 = 1 / fb0.di14 = 1)
$python test.py
do 值: 00101000
di 值: 00000010
```

</div>


[__SOURCE](6-io_plc/1-get/3-ios-sio.md)
#### 6.1.3 `ios/sio/{sio_val}` 

##### 描述

- `GET` : 获取系统 IO 值。

##### 路径参数

```python
GET /project/control/ios/sio/{sio_val}
```

##### 路径变量

- `sio_val` :
  - `si_val` : 获取输入 (si) 值。
  - `so_val` : 获取输出 (so) 值。

##### 查询参数

- `类型 (type)` : IO 值的类型
  - si 或 so : 位
  - sib 或 sob : 有符号字节
  - siw 或 sow : 有符号字 (2字节)
  - sil 或 sol : 有符号双字 (4字节)
  - sif 或 sof : 浮点数
- `sig_no` : 信号索引 (0~)

##### 示例

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

Python 脚本示例

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
[__SOURCE](6-io_plc/2-post/README.md)
## 6.2 `io_plc/post`

- 从内置PLC发送输入/输出值的POST请求。
- 您必须为每个API编写正确的请求体。
[__SOURCE](6-io_plc/2-post/1-set_relay_value.md)
#### 6.2.1 `设置继电器值`

##### 描述

- `POST` : 设置继电器值。

##### 路径参数

```python
POST /project/plc/set_relay_value
```

##### 请求参数

- `名称 (name)` : 根据 [继电器表达式](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-embedded-plc/zh/3-relay/2-relay-expression?cont_model=${cont_model}) 输入您想要设置的继电器名称。
- `值 (value)` : 请注意上面的标记中的 'data-type'，并输入您想要设置的值。
```json
{
    "name": "fb3.dof14",
    "value": "2.718"
}
```

##### 示例

```json
请求 URL:
POST /project/plc/set_relay_value

请求体:
{
    "name": "fb1.do0",
    "value": "1"
}
```

Python 脚本示例

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
响应: 200
[1, 0, 0, 0, 0, 0, 0, 0]
```

[__SOURCE](6-io_plc/2-post/2-ios-dio.md)
#### 6.2.2 `ios/dio/{do_val}`

##### 描述

- `POST` : 更改数字输出。

##### 路径参数

```python
POST /project/control/ios/dio/do_val
```

##### 请求体

```json
{
    "type": "do",
    "blk_no": 1,
    "sig_no": 1,
    "val": 1
}
```


##### 查询参数

- `类型 (type)` : io 值的类型
  - do : 位
  - dob : 有符号字节
  - dow : 有符号字 (2字节)
  - dol : 有符号双字 (4字节)
  - dof : 浮点数
- `blk_no` : 块号 (0~9)
- `sig_no` : 信号索引 (0~)
- `val` : 您想要更改的设置值


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

- 请参阅 [here](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200) 以获取响应的 HTTP 状态码。
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
[__SOURCE](7-log_manager/README.md)
# 7.1 事件日志

- 输出记录在控制器中的错误、警告、执行历史等。
[__SOURCE](7-log_manager/1-get/README.md)
## 7.1 `log_manager/get`

- 发送 GET 请求以获取控制器中记录的错误、警告和执行历史。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](7-log_manager/1-get/1-search.md)
#### 7.1.1 `搜索 (search)`

##### 描述

- `GET` : 使用指定的过滤条件查看事件日志。

##### 路径参数

```python
GET /logManager/search
```

##### 查询参数

- `n_item` : 请求的事件数量 (默认=100)
- `cat_p` : 请求类别过滤 (类别正). 通过用逗号 (,) 连接代表每种类型的字母来指定它们。 (cat_p=E,W,N)
  - `E` : 错误
  - `W` : 警告
  - `N` : 通知
  - `S` : 启动/停止
  - `O` : 用户操作
  - `I` : I/O, 继电器值
  - `P` : 定期状态
  - `H` : 历史
  - `C` : 控制台输出
  - `M` : 杂项
- `id_min` : 最小 ID 过滤。 (可选)
  - 每个事件都有一个唯一的事件 ID (eid)。 (0~)  
    如果您通过将以前接收到的事件的最大 ID 加 1 并在 `id_min` 中指定它来请求历史记录，您可以仅获取新发生的历史记录，排除已接收的事件。
  - 但是，当控制器中的事件 ID 达到最大值 (0xffffffffffffffff) 时，它将从 0 开始重新生成。  
    过滤将适当地考虑这些情况。  
    例如，如果 id_min 是 0xfffffffffffffffa，ID 为 0、1 和 2 的事件不会被过滤掉，而是包含在响应中。
- `id_max` : 最大 ID 过滤。 (可选)
- `ts_min` : 最小时间戳过滤。 (可选)
  - 年/月/日 时:分:秒.毫秒格式。例如：2023/11/20 18:50:30.955
- `ts_max` : 最大时间戳过滤。 (可选)
  - 年/月/日 时:分:秒.毫秒格式。例如：2023/11/20 18:50:30.955

##### 响应体

- `标识符 (id)` : 事件 ID
- `ts` : 时间戳
- `cat` : 事件类别
- `代码 (code)` : 事件代码号码
- `aux` : 事件辅助信息。最多 280 个字符。
  - 在错误、警告和启动/停止的情况下，会包含快照信息。

```json
{ "id" : 19964, "ts" : "2023/11/20 15:53:11.275", "cat" : "E", "code" : "11,0,0", "aux" : "{ 'pc' : '20/3/1', 'j1' : 18.525, 'j2' : 105.000, 'j3' : -2.577, 'j4' : -14.432, 'j5' : -0.776, 'j6' : 0.314, 'sin' : '00 01 00 00 00 00 00 00', 'sout' : '05 08 06 00 00 00 00 01', 'din' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0', 'dout' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0' }" }
{ "id" : 18314, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(    976)省电模式 = 打开 " }
{ "id" : 18313, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(=时间戳=)[2023/11/20 15:05:33](+299996445微秒) " }
{ "id" : 18312, "ts" : "2023/11/20 15:05:33.787", "cat" : "N", "code" : "5", "aux" : "{ 'pc' : '20/3/1' }" }
{ "id" : 18267, "ts" : "2023/11/20 15:00:33.791", "cat" : "H", "code" : "hist", "aux" : "(   2001)    .结束 ;(P20/S3/F1) " }
{ "id" : 18266, "ts" : "2023/11/20 15:00:33.789", "cat" : "H", "code" : "hist", "aux" : "( 738785)S3  .移动 P,速度=500mm/秒,加速度=4,工具=0 " }
##### 示例

<blockquote>

```python
请求 URL:
GET /logManager/search?cat_p=O&id_max=24258&id_min=24253

响应主体:
{
    { "id" : 24258, "ts" : "2023/11/28 16:53:31.239", "cat" : "O", "code" : "K.Click", "aux" : "右" }
    { "id" : 24257, "ts" : "2023/11/28 16:53:30.462", "cat" : "O", "code" : "K.Down", "aux" : "SHIFT" }
    { "id" : 24256, "ts" : "2023/11/28 16:53:23.450", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24255, "ts" : "2023/11/28 16:53:23.045", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
    { "id" : 24254, "ts" : "2023/11/28 16:53:13.695", "cat" : "O", "code" : "K.Up", "aux" : "CTRL" }
    { "id" : 24253, "ts" : "2023/11/28 16:53:13.202", "cat" : "O", "code" : "K.Down", "aux" : "CTRL" }
}
```

Python 脚本示例

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

[__SOURCE](8-file_manager/README.md)
# 8. `file_manager`

- 这涵盖了从控制器读取文件信息、更改文件名和传输文件等功能。
- 还涵盖了检查目录是否存在或创建和删除目录的功能。
[__SOURCE](8-file_manager/1-get/README.md)
## 8.1 `file_manager/get`

- 发送 GET 请求以从控制器获取文件信息。
- 通过为每个 API 设置正确的路径参数和查询参数来接收响应。
[__SOURCE](8-file_manager/1-get/1-files.md)
#### 8.1.1 `文件 (files)`

##### 描述

- `GET` : 文件内容由控制器返回。

##### 路径参数

```python
GET /file_manager/files
```

##### 查询参数

查询参数必须输入。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 要获取的文件名

##### 状态码

- 200 : 请求成功
  - 返回文件内容
- 403 : 请求失败
  - 当文件不存在时返回错误状态码

##### 示例

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
请求 URL:
GET /file_manager/files?pathname=project/jobs/0001.job

响应主体:
{
    Hyundai Robot Job File; { version: 2.0 ... }
    ...
}
```
</blockquote>

Python 脚本示例

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
现代机器人作业文件; { version: 2.0, mech_type: "576(HH020-03)", total_axis: 6, aux_axis: 0 }
     位姿 P1 =po1 = 位姿(10, 90, 0, 0, -30, 0, -1240.8)
     位姿 P2
     位姿 P3
     位姿 P4
S1   move P,tg=po1,spd=100%,accu=0,tool=1
S2   move P,tg=po1,spd=100%,accu=0,tool=1
S3   move P,tg=po1,spd=100%,accu=0,tool=1
S4   move P,tg=po1,spd=100%,accu=0,tool=1
     end
```

[__SOURCE](8-file_manager/1-get/2-file_info.md)
#### 8.1.2 `file_info`

##### 描述

- `GET` : 基于文件路径获取该文件的信息。

##### 路径参数

```python
GET /file_manager/file_info
```

##### 查询参数

必须输入查询参数。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### 响应体

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

[__SOURCE](8-file_manager/1-get/3-file_list.md)
#### 8.1.3 `file_list`

##### 描述

- `GET` : 获取文件和目录的列表。

##### path-parameter

```python
GET /file_manager/file_list
```

##### query-parameter

必须输入 query-parameter。  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|描述|
|:---|:---|
|`路径 (path)`|您想检查的目标路径|
|`incl_file`|在输出列表时是否包括文件|
|`incl_dir`|在输出列表时是否包括目录|


##### 状态码

- 200 : 请求成功
  - 返回 [文件信息](../../99-schema/file_info) `list`
- 403 : 请求失败
  - 没有文件存在


##### 示例

<blockquote>

```
${cont_model}
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- ${cont_model:lower}_proj.json
```

```python
请求 URL:
GET /file_manager/file_list?path=project&incl_file=true&incl_dir=true

响应主体:
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

Python 脚本示例

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

[__SOURCE](8-file_manager/1-get/4-file_exist.md)
#### 8.1.4 `file_exist`

##### 描述

- `GET` : 获取目标文件的存在性。

##### 路径参数

```python
GET /file_manager/file_exist
```

##### 查询参数

必须输入查询参数。  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : 目标文件路径

##### 响应主体

- `true` （文件存在）
- `false` （文件不存在）

##### 状态码

- 200 : 请求成功
  - 返回 [文件信息](../../99-schema/file_info) `list`
- 404 : 请求失败
  - 不允许的路径参数


##### 示例

<blockquote>

```python
请求网址：
GET /file_manager/file_exist?pathname=project/jobs/1234.job

响应主体: 
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

Python脚本示例

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

[__SOURCE](8-file_manager/2-post/README.md)
## 8.2 `file_manager/post`

- 发送控制器的文件信息的 POST 请求。
- 您必须为每个 API 编写正确的请求体。
[__SOURCE](8-file_manager/2-post/1-rename_file.md)
#### 8.2.1 `rename_file`

##### 描述

- `POST` : 更改目标文件的文件名。

##### 路径参数

```python
POST /file_manager/rename_file
```

##### 请求体

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : 更改前的文件路径
- `pathname_to` : 更改后的文件路径

##### 状态码

- 200 : 请求成功
  - 一切正常
- 400 : 请求失败
  - 没有文件存在可以重命名

##### 示例

<blockquote>

```python
请求网址:
POST /file_manager/rename_file

请求体: 
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

Python 脚本示例

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
[__SOURCE](8-file_manager/2-post/2-mkdir.md)
#### 8.2.2 `mkdir`

##### 描述

- `POST` : 在目标路径中创建目录。

##### 路径参数

```python
GET /file_manager/mkdir
```

##### 请求体

|键|值|描述|
|:---|:---|:---|
|`路径 (path)`|`str`|创建目录的位置|

##### 响应体

- { `路径 (path)`: ${target path} }

##### 状态码

- 200 : 请求成功
  - 目标位置的目录创建完成
- 400 : 请求失败
  - 当目标位置的目录名称重复时

##### 示例

<blockquote>

```python
请求 URL:
GET /file_manager/mkdir

请求体: 
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

Python 脚本示例

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

[__SOURCE](8-file_manager/2-post/3-files.md)
#### 8.2.3 `文件 (files)`

##### 描述

- `POST` : 将文件传输到目标路径。

##### path-parameter

```python
POST /file_manager/files/{target_filepath}
```

##### path-variable

- `target_filepath` : 包含扩展名的目标文件路径。

##### request-body

- `Content-Type` 必须是 `application/octet-stream`。

##### 状态代码

- 200 : 请求成功
  - 传输完成

##### 示例

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

Python 脚本示例

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

[__SOURCE](8-file_manager/3-delete/README.md)
## 8.3 `file_manager/delete`

- 从控制器发送文件信息的 DELETE 请求。
[__SOURCE](8-file_manager/3-delete/1-files.md)
#### 8.3.1 `文件 (files)`

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
请求 URL:
DELETE /file_manager/files/project/jobs/special
```
```
${cont_model}
`-- project
    `-- jobs
        `-- test.job   <- 目标
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
响应：200
```
[__SOURCE](9-task/README.md)
# 9. `任务 (task)`

- 这部分内容涉及任务相关的内容。
- 您可以重置特定任务或所有任务。
- 您可以从当前任务的本地或全局变量中读取值或声明新变量。
- 在任务执行期间，可以针对特定工作流程（例如，等待）采取特定操作（例如，释放）。
[__SOURCE](9-task/1-get/README.md)
## 9.1 `task/get`

- 发送GET请求以获取与任务相关的信息。
- 通过为每个API设置正确的路径参数和查询参数来接收响应。
[__SOURCE](9-task/2-post/README.md)
## 9.2 `task/post`

- 发送与任务相关的信息的POST请求。
- 您必须为每个API编写正确的请求体。
[__SOURCE](9-task/2-post/1-cur_prog_cnt.md)
#### 9.2.1 `task/cur_prog_cnt`

##### 描述

- `POST` : 设置任务的当前程序计数器。

##### 路径参数

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

##### 请求体

- [cur_prog_cnt 请求参数](../../99-schema/cur_prog_cnt.md)

##### 响应体

- [cur_prog_cnt 响应参数](../../99-schema/cur_prog_cnt.md)

##### 示例

```python
请求 URL:
POST /project/context/tasks[0]/cur_prog_cnt

请求体:
{
    "pno":-1,
    "sno":-1,
    "fno":-1,
    "ext_sel":0
}
```

Python 脚本示例

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
[__SOURCE](9-task/2-post/2-reset.md)
#### 9.2.2 `task/reset`

##### 描述

- `POST` : 对任务执行重置。  
- 它的操作方式与使用 [RCode 0](https://hrbook-hrc.web.app/#/view/doc-${cont_model:lower}-operation/zh-tp630/8-r-code/1-use-r-code?cont_model=${cont_model}) 相同。
  - <span style="text-decoration: underline; text-decoration-style: wavy; text-decoration-color: #E82E8C;"> 任何其他代码都不适用于操作 </span>

##### 路径参数

```python
# 重置所有任务
POST /project/service/r_code/execute
```

##### 请求体

```json
{"code": 0}
```

##### 示例

```python
请求 URL:
POST /project/service/r_code/execute

请求体:
{
    "code":0
}
```

Python 脚本

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

[__SOURCE](9-task/2-post/3-assign_var_expr.md)
#### 9.2.3 `assign_var_expr`

##### 描述

- `POST` : 在当前任务语句中重新分配一个变量。

##### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

##### request-body

- `名称 (name)` : 变量名称
- `expr` : 代入变量的表达式
- `保存 (save)` : 是否保存（true/false）。这是为了将数据保存在变量文件中。
- `scope` : 设置变量的有效范围
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|局部变量|全局变量|完整范围（局部和全局自动设置）|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
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

当上述作业文件被执行并在任务中声明一个局部变量 `字母a (a)`

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

def assign_var_expr(var_name: str, scope = None, expression: str = '') -> int:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/project/context/tasks[0]/assign_var_expr"
    head             = {'Content-Type': 'application/json; charset=utf-8'}
    body             = {"name": f"{var_name}", "expr": f"{expression}", "scope": f"{scope}"}

    response = requests.post(url = base_url + path_parameter, headers=head, json=body)

    return response.status_code

print(f"之前: {post_read_var('a', 'local')}")
print(f"响应: {assign_var_expr('a', 'local', '465 + 312')}")
print(f"之后: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
之前: 1234
响应: 200
之后: 777   
```
[__SOURCE](9-task/2-post/4-assign_var_json.md)
#### 9.2.4 `assign_var_json`

##### 描述

- `POST` : 在当前任务语句中重新分配变量。  

##### 路径参数

```python
POST /project/context/tasks[0]/assign_var_json
```

##### 请求体

- `名称 (name)` : 变量名称
- `json` : 要替换为变量的 json 格式 `string`。
- `保存 (save)` : 保存内容 (true/false)。即在您将该数据保存到活动文件之前。
- `范围 (scope)` : 设置变量的有效作用域
	|`local`|`global`|`未设置`|
	|:---|:---|:---|
	|局部变量|全局变量|完整作用域（局部和全局会自动设置）|


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

当上述作业文件被执行并在任务中声明了一个局部变量 `字母a (a)`

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

print(f"之前: {post_read_var('a', 'local')}")
print(f"""响应: {assign_var_json('a', 'local', '{"test": 10}')}""")
print(f"之后: {post_read_var('a', 'local')}")
```
```sh
$python test.py 
之前: 1234
响应: 200
之后: {'_type': 'JObject', 'test': 10}
```
[__SOURCE](9-task/2-post/5-release_wait.md)
#### 9.2.5 `release_wait`

##### 描述

- `POST` : release 语法
- 要求：TP > 系统 > 1: 用户环境 > `wait(di/wi) release` > `启用 (Enable)` 点击

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
- -1442069 : 用户环境配置错误。请确保满足所有先决条件

##### 示例

<blockquote>

```json
请求 URL:
POST /project/context/tasks[0]/release_wait

请求体
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
[__SOURCE](9-task/2-post/6-set_cur_pc_idx.md)
#### 9.2.6 `set_cur_pc_idx`

##### 描述

- `POST` : 定位当前光标在索引行的功能

##### 路径参数

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

##### 请求主体
```json
{
    "idx": 1
}
```

##### 示例

<blockquote>

```python
请求 URL:
POST /project/context/tasks[0]/set_cur_pc_idx

请求主体
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
响应 200 # 光标位置在 TP 上改变
```
[__SOURCE](9-task/2-post/7-solve_expr.md)
#### 9.2.7 `solve_expr`

##### 描述

- `POST` : 求解表达式并将结果值设置为任务的本地或全局变量。

##### 路径参数

```python
POST /project/context/tasks[0]/solve_expr
```

##### 请求体
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

##### 响应体

```json
13 // 读取当前指定作用域内的 expr 值。
```

##### 示例

<blockquote>

```python
# 1. 读取当前任务中声明的 "local" 变量 a 的值
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr"  : "a",
    "scope" : "local"
}

响应体:
13
```
</blockquote>

<blockquote>

```python
# 2. 读取在当前任务中声明的 "global" 变量 a 的值
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr"  : "a",
    "scope" : "global"
}

响应体:
10
```

</blockquote>

<blockquote>

```python
# 3. 将 -234 加到局部变量 a 的值上
请求 URL:
GET /project/context/tasks[0]/solve_expr

请求体:
{
    "expr": "a + (-234)"
}

响应体:
1000
```

</blockquote>

Python 脚本示例
- 在机器人控制器的任务区域中设置局部和全局变量 a 的值，执行以下代码。

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
[__SOURCE](9-task/2-post/8-execute_move.md)
#### 9.2.8 `execute_move`

##### 描述

- 支持的版本 : `60.28-00` &uparrow;
- `POST` : 移动到指定的姿态。

{% hint style="warning" %}
仅限HRSpace用户<br>
由于VRC_Hi6 v60.30-10到v60.32-06上的远程模式验证错误，execute_move可能会失败<br>
→ 使用v60.30-09或更早版本，或v60.32-07或更高版本（物理Hi6控制器不受影响）
{% endhint %}

##### 路径参数

```python
POST /project/context/tasks[{task index}]/execute_move
```

##### 请求体
- `stmt` : 请求体中的键值，指向该语句。
- 有关如何编写移动语句的详细信息，请参阅 [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/zh/5-moving-robot/4-move?cont_model=${cont_model})。

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

##### 响应

1. 状态码
- 200 : OK
- 400 : Bad Request
    - 请求体未通过验证。
- 403 : Forbidden
    - 尝试在非远程模式下进行API请求（自v60.30-07起生效）。
- 404 : Not Found

2. 响应体

- v60.30或更早版本的正常响应

```json
{ "err_code" : 0 }
```

- v60.32或更高版本的正常响应

```json
{ "_type" : "JObject" }
```
3. 错误代码

- -38500 : 尝试在非远程模式下发出API请求
- -1442071 : 尝试在电机关闭时发出API请求
- -1442080 : 尝试在自动程序执行期间发出API请求
- -1376272 : 处理API请求时发生机器人语言语法错误

Python脚本示例
- 在电机开启并符合当前机器人轴时输入位姿命令。

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
[__SOURCE](10-console/README.md)
# 10. `console`

- 您可以使用 ${cont_model} 控制器软件的 CLI 命令。  
- 可以使用机器人语言执行各种操作。
[__SOURCE](10-console/1-get/README.md)
## 10.1 `console/get`

- 发送与执行机器人命令相关的信息的 GET 请求。  
- 每个 API 必须设置确切的路径参数和查询参数才能接收响应。  
[__SOURCE](10-console/2-post/README.md)
## 10.2 `console/post`

- 发送关于执行机器人命令的信息的POST请求。  
- 每个API的确切请求体必须单独编写。  
[__SOURCE](10-console/2-post/1-execute_cmd.md)
#### 10.2.1 `execute_cmd`

##### 描述

- 支持的版本 : `60.28-00` &uparrow;
- `POST` : 为 ${cont_model} 控制器执行控制台命令。  
- 您可以执行 [CLI 机器人语言命令](../.././99-schema/robotlang.md)。  

##### 路径参数

```python
POST /console/execute_cmd
```

##### 请求主体

```json
{
    "cmd_line" : "rl.reinit"
}
```

##### 状态代码

- 200: 请求成功  
	- 需要应用 [CLI 机器人语言命令](../.././99-schema/robotlang.md) 规则  
	- 如果命令违反机器人语言规则，将返回 ecode 1，如下所示。
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400: 请求失败
	- 请求主体验证失败
- 403/4: 请求失败
	- 请求了未提供服务的 API

##### 示例

</blockquote>

Python 脚本示例
- 命令可以在 `电机 开 (motor on)` 和 `远程模式` 状态下执行。  
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
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: 200
```
[__SOURCE](11-etc/README.md)
# 11. `etc`

- 它包含系统版本、事件日志、时钟等。
[__SOURCE](11-etc/1-clock/README.md)
# 11.1 `clock`

- 您可以读取和设置控制器的系统时间。
[__SOURCE](11-etc/1-clock/1-get/README.md)
#### 11.1.1 `clock/get`

- 发送GET请求以获取控制器系统时间。
- 通过为每个API设置正确的路径参数和查询参数来接收响应。
[__SOURCE](11-etc/1-clock/1-get/1-date_time.md)
#### 11.1.1.1 `date_time`

##### 描述

- `GET` : 获取系统设置时间。

##### 响应主体

- [date time](../../../99-schema/date_time.md)

##### 示例

<blockquote>

```python
请求 URL:
GET /clock/date_time

响应主体:
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

[__SOURCE](11-etc/1-clock/2-put/README.md)
#### 11.1.2 `clock/put`

- 发送一个 PUT 请求到控制器系统时间。
- 您必须为每个 API 编写正确的请求体。
[__SOURCE](11-etc/1-clock/2-put/1-date_time.md)
#### 11.1.2.1 `date_time`

##### 描述

- `PUT` : 更改系统时间。

##### request-body

- [日期时间](../../../99-schema/date_time.md)

##### 示例

<blockquote>

```python
请求 URL:
PUT /clock/date_time

请求体:
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

print(f"响应: {put_system_time()}")
```
```sh
$python test.py
响应: 200
```

[__SOURCE](99-schema/README.md)
# 12. 结构

本章包含对在 Open API 中使用的各种枚举和结构的引用。
[__SOURCE](99-schema/crdsys.md)
### `crdsys`

#### 描述

这是一个枚举，指定坐标系统。
|值|描述|
|:---:|:---|
|`-1`|`下一个 (Next)` 坐标系统|
|`0`|`轴 (axis)` 坐标系统|
|`翻译 (1)`|`正交`(= `机器人 (robot)`) 坐标系统|
|`翻译 (2)`|`用户 (user)` 坐标系统|
|`翻译 (3)`|`工具 (tool)` 坐标系统|
[__SOURCE](99-schema/cur_prog_cnt.md)
### `cur_prog_cnt`

#### 描述
设置任务的当前程序计数器。

#### 请求体
|key|type|description|
|:---|:---|:---|
|`pno`|int|程序编号（如果为-1，则保持当前编号）|
|`sno`|int|步骤编号（如果为-1，则保持当前编号）|
|`fno`|int|功能编号（如果为-1，则保持当前编号）|
|`ext_sel`|int|`0` : 内部选择（在远程模式下禁止） <br> `翻译 (1)` : 外部选择（仅在远程模式下允许）|

#### 响应体
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|新移动的步骤编号|
|`fno_new`|int|新移动的功能编号|
|`ln_new`|int|新移动的行编号（程序头为0，第一条语句为1）|
[__SOURCE](99-schema/date_time.md)
### `date_time`

#### 描述

指示系统时间相关信息。
|值|类型|描述|
|:---:|:---|:---|
|"year"|`int`|当前系统年份|
|"mon"|`int`|当前系统月份|
|"day"|`int`|当前系统天数|
|"hour"|`int`|当前系统小时|
|"min"|`int`|当前系统分钟|
|"sec"|`int`|当前系统秒数|
[__SOURCE](99-schema/file_info.md)
### `file_info`

#### 描述

请求文件信息时返回此参数。

|key|type|描述|
|:---:|:---|:---|
|fname|`str`|文件名|
|size|`int`|文件大小(B, Byte)|
|year|`int`|`文件修改年份`|
|month|`int`|`文件修改月份`|
|mday|`int`|`文件修改日期`|
|wday|`int`|`文件修改的星期几` (0: 日, 1: 一, 2: 二, ...) |
|hour|`int`|`文件修改的小时`|
|min|`int`|`文件修改的分钟`|
|sec|`int`|`文件修改的秒数`|
|is_dir|`bool`|检查当前文件是否为目录|
|readonly|`bool`|检查该文件是否为只读|
[__SOURCE](99-schema/jobs_info.md)
### `jobs_info`

#### 描述

这是一个作业文件信息参数。

|key|type|description|
|:---:|:---|:---|
|fname|`str`|作业文件名|
|job_comment|`str`|评论|
|n_step|`int`|步骤数量|
|n_total_ax|`int`|轴的数量|
|n_aux_ax|`int`|附加轴的数量|
[__SOURCE](99-schema/mechinfo.md)
### `mechinfo`

#### 描述

机制信息  
通过位域庆祝使用的活动。

- 位 0 : M0
- 位 1 : M1
- 位 2 : M2
- 位 3 : M3
- 位 4 : M4
- 位 5 : M5
- 位 6 : M6
- 位 7 : M7

#### 示例

```python
0x13 = 0b00010011 = M4 | M1 | M0
# 指定机制 M0、M1 和 M4。
```
[__SOURCE](99-schema/op_cnd.md)
### `op_cnd`

#### 描述
op_cnd (操作条件) : `条件设置 (Condition setting)` 的值  
当您在 TP 中按下 `条件设置 (Condition setting)` 按钮时，可以查看这些值。

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `翻译 (1)` : 1 周期 <br> `翻译 (2)` : 重复|自动操作周期模式|
|step_goback_max_spd|`10` ~ `250` (毫米/秒)|前进/后退时的最大速度|
|step_go_func_ex|`0` : 无效 <br> `翻译 (1)` : 有效 <br> `翻译 (2)` : I ON (=DI 信号)|前进步骤时的功能执行|
|func_reexe_on_trace| `0` : 无效 <br> `翻译 (1)` : 有效 |向后走后，在向前移动时重新执行功能|
|path_recov_confirm|`0` : 无效 <br> `翻译 (1)` : 有效|前进/后退时的路径恢复|
|playback_spd_rate|`翻译 (1)` ~ `100` (%)|自动操作速度比例|
|robot_lock|`0` : 无效 <br> `翻译 (1)` : 有效 |机器人锁定|
|intp_base|`0` : 机器人工具 <br> `翻译 (1)` : 静止工具|插补标准|
|ucrd_num|`0` ~ `20`|指定用户坐标系|
|plc_mode|`0` : 关闭 -> 停止 <br> `翻译 (1)` : 停止 -> 远程停止 <br> `翻译 (2)` : 远程停止 -> 远程停止 <br> `翻译 (3)` : 远程运行 -> 远程停止 <br> ` (4)` : 运行 -> 关闭|PLC 操作模式|

<br>

#### 示例

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

#### 描述

姿势数据。

|键|描述|
|:---|:---|
|x|X 位置 (毫米)|
|y|Y 位置 (毫米)|
|z|Z 位置 (毫米)|
|rx|RX 角度 (度)|
|ry|RY 角度 (度)|
|rz|RZ 角度 (度)|
|j1~j16|1~16 轴值 (毫米或度)|
|crd|[坐标系统](./crdsys.md)|
|mechinfo|[机制信息](./mechinfo.md)|
|nsync|传感器同步值的数量 (0~2)|
|sync|传感器同步值 (字符串)。例如 `"sync(220.5,195.3)"`|
[__SOURCE](99-schema/tool_data.md)
### `tool_data`

#### 描述

机器人的工具数据。

|关键|描述|
|:---:|:---|
|`x`|X 位置 (mm)|
|`y`|Y 位置 (mm)|
|`z`|Z 位置 (mm)|
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
|`mass_esti`|负载估计重量 (kg)|
[__SOURCE](99-schema/robotlang.md)
### CLI 机器人语言命令

#### 描述

这是可以从 ${cont_model} 控制台执行的机器人语言命令的列表。  

|选项|描述|示例|
|:---|:---|:---|
|`reinit`| 执行机器人语言重启命令。 |rl.reinit|
|`i`| 将机器人语言命令插入到作业文件中。 |rl.i \<cmdline><br>rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0,0,0]<br>rl.i end|
|`开始 (start)`| 在 `电机开启` 且处于 `远程模式` 时执行机器人语言。|rl.start|
|`停止 (stop)`| 当机器人语言当前正在运行时执行 `外部停止`。|rl.stop|
|`exit`| 终止当前运行的机器人语言。|rl.exit|