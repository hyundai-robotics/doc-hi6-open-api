## 1.2 Required prior knowledge

In order to utilize Open API,you must first understand how to use the Hi6 controller.  
Please refer to the manual below or take training at the Hyundai Robotics Joint Training Center.

- [Hi6 Robot Controller Operation Manual](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/english-tp630/README)
- [HD Hyundai Robotics Joint training center](https://www.hyundai-robotics.com/customer/customer5intro.html)

<br>

Open API is an HTTP-based REST API.Various development languages provide libraries for calling REST API (aka RESTful API),  
and many developers use them to develop programs. Unless you are an experienced developer,  
you must be familiar with the basic concepts of how web-based service calls and responses are made, as mentioned in [1.1 About Hi6 Open API](./1-intro.md#11-overview).

In this regard, please refer to the points below.

* If you are unfamiliar with the simple API-related explanation below or are not an expert with  
extensive development experience in applying it, please study first and then use the document.
* If you need to learn, please learn how to code client functions through REST API calls.

<br>


{% hint style="warning" %}

We do not accept inquiries about how to code conventional REST API clients.

We are not responsible for any damages or problems arising from the use of APIs not officially mentioned in the Hi6 Open API manual.

{% endhint %}

---- 

### 1.2.1 What is an API?

`API` (Application Programming Interface) is a `set of definitions and protocols` for building and  integrating application software ([ref](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces)).  
This is how the user sends a `request structured in a particular way` and the provider's software `responds` to it.  
This allows you to communicate with products or services you don't know how to specifically develop, and simplifies application development, saving time and money.

<br>


### 1.2.2 What is REST API?

`REST` (Representational State Transfer) is a `software architecture` that imposes conditions on how an API behaves.  
`REST API` refers to an API that follows the REST architecture style. Also called RESTful API ([ref](https://aws.amazon.com/what-is/restful-api/)).  
By communicating through HTTP requests, it performs standard database functions (CRUD) such as Create, Read, Update, and Delete records within the resource.  

Developers often implement RESTful APIs using four common Hypertext Transfer Protocol (HTTP) methods ([ref](https://aws.amazon.com/what-is/restful-api/#seo-faq-pairs#what-restful-api-client-contain)).

- `GET` : Clients use GET to access resources that are located at the specified URL on the server. They can cache GET requests and send parameters in the RESTful API request to instruct the server to filter data before sending.
- `POST` : Clients use POST to send data to the server. They include the data representation with the request. Sending the same POST request multiple times has the side effect of creating the same resource multiple times.
- `PUT` : Clients use PUT to update existing resources on the server. Unlike POST, sending the same PUT request multiple times in a RESTful web service gives the same result.
- `DELETE` : Clients use the DELETE request to remove the resource. A DELETE request can change the server state. However, if the user does not have appropriate authentication, the request fails.