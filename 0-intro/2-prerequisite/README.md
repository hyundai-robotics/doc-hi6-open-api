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
