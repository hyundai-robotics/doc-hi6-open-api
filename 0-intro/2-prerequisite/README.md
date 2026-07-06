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