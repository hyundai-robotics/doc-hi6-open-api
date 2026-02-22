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