# Hi6 Open API Manual

{% hint style="warning" %}

The information provided in this product manual is the property of Hyundai Robotics.

It cannot be reproduced or redistributed in whole or in part without the written consent of Hyundai Robotics, and cannot be provided to a third party or used for any other purpose.


This manual is subject to change without prior notice.


**Copyright ⓒ 2023 by HD Hyundai Robotics**



{% endhint %}

{% hint style="warning" %}

We are not responsible for any damage or problems that arise from using an API that is not officially mentioned in the Hi6 Open API manual.

{% endhint %}## 1.1 Intro

You can check the basic information related to Hi6 Open API below.

[1.1 About Hi6 Open API](./1-concept/README.md) <br>
[1.2 Required prior knowledge](./2-prerequisite/README.md) <br>
[1.3 Sample code](./3-sample-code/README.md) <br>
[1.4 Simple API call without coding](./4-api-test/README.md)## 1.1 About Hi6 Open API

In this document, HD Hyundai Robotics publishes an API for application developers to easily monitor and remotely control the robot controller (hereafter referred to as Hi6).<br>
This enables developers to read and write Hi6 data without requiring a thorough comprehension of the source code used in Hi6 development.<br>
The image below will help you better grasp the role of Open API.

<img src="../../_assets/05_open_api_flow.png" style="max-height: 25vh;">

The parts marked in orange in the picture above show the role of Open API.

|Arrow sign|Description|
|:---|:---|
|`Solid line`|This means that the `developer` (`client`) `requests` information to `Hi6` (`server`) using one of four methods (GET, POST, PUT, DELETE).|
|`Dotted line`|This means that the `controller` that `received` the `request` `sends back` the appropriate `response` in json or text format.|

In this way, developers can use the Open API in the document to remotely control or monitor their desktops, laptops, tablet PCs, etc. connected via Hi6 and Ethernet based on http and REST API.


<br><br>


### Be sure to check before you start!

* The current document is an initial version and was written based on Hi6 Open API version 5.

* There may be continuous version updates in the future. If the version is updated, please refer to the corresponding section.

* For developers who are familiar with developing HTTP REST API client functions, you can skip from [1.2 Required prior knowledge](../2-prerequisite/README.md) to [1.4 Simple API call without coding](../4-api-test/README.md).


{% hint style="warning" %}

The APIs described in this document are supported starting from `Hi6 V60.24-00` unless otherwise specified.

Please note that URLs and properties not specified in this document may change without notice in the same API version.

{% endhint %}## 1.2 Required prior knowledge

In order to utilize Open API,you must first understand how to use the Hi6 controller.  
Please refer to the manual below or take training at the Hyundai Robotics Joint Training Center.

- [Hi6 Robot Controller Operation Manual](https://hrbook-hrc.web.app/#/view/doc-hi6-operation/english-tp630/README)
- [HD Hyundai Robotics Joint training center](https://www.hyundai-robotics.com/customer/customer5intro.html)

<br>

Open API is an HTTP-based REST API.Various development languages provide libraries for calling REST API (aka RESTful API),  
and many developers use them to develop programs. Unless you are an experienced developer,  
you must be familiar with the basic concepts of how web-based service calls and responses are made, as mentioned in [1.1 About Hi6 Open API](../1-concept/README.md).

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
- `DELETE` : Clients use the DELETE request to remove the resource. A DELETE request can change the server state. However, if the user does not have appropriate authentication, the request fails.## 1.3 Sample code

Various development languages provide libraries for calling REST APIs.  
To learn how to use it, you can easily search and refer to the technical documentation for each development language.

- In this document, we will only explain the calls to the GET and POST methods using C# and python.

- Let's assume you are making a request to a Hi6 controller with IP address 192.168.1.150.
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
> Link : [https://github.com/hyundai-robotics/OpenAPI](https://github.com/hyundai-robotics/OpenAPI)### 1.3.2 Sample code - python

The example code is `a. Synchronous request (blocking & synchronous)` and `b. Asynchronous request (non-blocking & asynchronous)` Two methods are explained.
||Synchronous|Asynchronous|
|:---|:---|:---|
|blocking|`a. Synchronous request`||
|non-blocking||`b. Asynchronous request`|

Differences between the two methods can have serious consequences for TPs and controllers, such as:
1. Due to frequent synchronous function calls in the UI thread, the UI may not run smoothly and may freeze (`Hanging problem`). 
2. If no response is received due to a problem on the server (controller) side, the application UI may freeze (`Hanging problem`).

	
Therefore, when developing actual applications, please write your code in an asynchronous manner.  
- Please note that the python script example written in the Hi6 Open API description is written synchronously for easy understanding.  


<br>

### a. Synchronous request
Synchronous is a request method in a blocking state in which other tasks cannot be executed until one request is completed and a response is received.  
A widely used library for `synchronous` HTTP requests in Python is `requests`.
If you do not have the `requests` library, you can install it through the Python package manager.  
	
```sh
$pip install requests
```

- Please keep in mind that if you do not receive a response when communicating or if it takes a long time to receive a response, the possibility of a hanging problem may be very high.

```python
# sync.py - Synchronous, getting and setting user IO output values
import requests
import time

url='http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) set fb2.do3 value
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
start_time = time.time()
resp = requests.post(url + path, headers=head, json=req_body)
end_time = time.time()
print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

# (GET) get fb2.do3 value
total_start_time = time.time()
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")
total_end_time = time.time()
print(f"total request time : {total_end_time - total_start_time} seconds")
```
```bash
$python sync.py
[post] 0x79 to fb2.do3 Time taken: 0.004312038421630859 seconds
[get] 0x79 from fb2.do3 Time taken: 0.05764031410217285 seconds
[get] 0x79 from fb2.do3 Time taken: 0.06277251243591309 seconds
[get] 0x79 from fb2.do3 Time taken: 0.0634009838104248 seconds
[get] 0x79 from fb2.do3 Time taken: 0.06106710433959961 seconds
[get] 0x79 from fb2.do3 Time taken: 0.04711771011352539 seconds
total request time : 0.292741060256958 seconds
```

<br>

### b. Asynchronous request  
This is a method that complements the problems of synchronous requests. It operates a callback function when requested and processes the request in the callback function, allowing other tasks to be executed in the meantime.  
Asynchronous differs from synchronous in that it does not guarantee the order in which tasks are completed, but because all requests start at approximately the same time, overall response time can be shorter.  
Python provides a built-in library for implementing asynchronous programming called `asyncio`. This allows CPU tasks and I/O to be processed in parallel.  
Additionally, a popular library for `asynchronous` HTTP requests is `aiohttp`.  
If you do not have the `aiohttp` library, you can install it through the Python package manager.  
```sh
$pip install aiohttp
```

```python
# async.py -  Asynchronous, getting and setting user IO output values
import asyncio
import aiohttp
import time

url = 'http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3}

async def set_value(session):
    val = 0x60
    req_body = {'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val': val}
    start_time = time.time()
    async with session.post(url + path, headers=head, json=req_body) as resp:
        pass
    end_time = time.time()
    print('[post]', hex(val), 'to fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def get_value(session):
    start_time = time.time()
    async with session.get(url + path, headers=head, params=query) as resp:
        resp_body = await resp.json()
    end_time = time.time()
    print('[get]', hex(resp_body['val']), 'from fb2.do3', f"Time taken: {end_time - start_time} seconds")

async def main():
    async with aiohttp.ClientSession() as session:
        await set_value(session)
        tasks = [get_value(session) for _ in range(5)]
        total_start_time = time.time()
        await asyncio.gather(*tasks)
        total_end_time = time.time()
        print(f"total request time : {total_end_time - total_start_time} seconds")

asyncio.run(main())
```
```bash
$python async.py
[post] 0x60 to fb2.do3 Time taken: 0.0027306079864501953 seconds
[get] 0x60 from fb2.do3 Time taken: 0.04407477378845215 seconds
[get] 0x60 from fb2.do3 Time taken: 0.05881357192993164 seconds
[get] 0x60 from fb2.do3 Time taken: 0.057793378829956055 seconds
[get] 0x60 from fb2.do3 Time taken: 0.057793378829956055 seconds
[get] 0x60 from fb2.do3 Time taken: 0.05912017822265625 seconds
total request time : 0.06045794486999512 seconds
```## 1.4 Simple API call without coding

If you use Open API while developing a client application like [previous example code](../3-sample-code/README.md), you can easily call the API without coding.  
Through this calling process, you can check whether the request worked properly and what data is returned in response.  
There are several ways to do this. This section covers two representative ones.

<br>

### 1.4.1 Using `postman`

`postman` is a widely used API testing platform around the world.
Postman's `workspace` function enables project-level API testing and history tracking, and is equipped with language-specific code snippets and intuitive UI.
Simple usage instructions can be found in [1.4.1 Requesting POST in Postman](../4-api-test/1-postman.md).


<br>


### 1.4.2 Using `Web Browser`

Simple `get` requests can be made easily and quickly through a web browser.  
Additionally, you can use your web browser's extension to directly call `get` requests and other API requests and view the results.  
You can check simple usage instructions in [1.4.2 Calling API from web browser](../4-api-test/2-web-browser.md).## 1.4.1 Requesting POST in Postman

On this page, use `postman` to call the `POST` request of the REST API and check the result.  
Additionally, simple UI configuration helps you understand how to use it.

<br>

### a. Main UI composition

You can check the main UI composition through the picture below.

<img src="../../_assets/01_postman_desc.png" style="max-height: 55vh;">

<blockquote>

(1) You can simply create a request request through the `+` button. </br>
(2) This is a space to enter information about the `request`. </br>
(3) This is a space to check information about `response`. </br>
(4) This is a space to check the `Code snippet` for each language that is automatically generated by applying the `request` url. </br>

</blockquote>

<br>

### b. Testing POST Requests

1. `Request Header`  
	- Enter the `Key`, `Value` below in the Headers tab.
  	- About `Content-Type` ([ref](https://blog.postman.com/what-are-http-headers/#Content-type))
	<br><img src="../../_assets/02_postman_headers.png" style="max-height: 14vh;">

<br>

2. `Request Body`  
	- Select API method as `POST` and enter URL.  
	- Click the `Body` tab and enter the `body-parameter` you want to request. ([9.2.1 `task/cur_prog_cnt` - request body](../../9-task/2-post/1-cur_prog_cnt.md))
	- Click `Send`  
		<img src="../../_assets/03_postman_post.png" style="max-height: 30vh;">

<br>

3. `Response` and `Code snippet`
	- `request` If the request is completed normally, `HTTP Status` responds with `200 OK` as shown below.([HTTP Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status))
	- You can also check the `Code snippet` for each language to which the URL is applied.  
		<img src="../../_assets/04_postman_post_result_check.png" style="max-height: 52vh;">  
		<blockquote>

		`(1) Response body` : response from the `post` request ([9.2.1 `task/cur_prog_cnt` - response body](../../9-task/2-post/1-cur_prog_cnt.md))</br>
		`(2) Python Code snippet` : codes for `post` request in python.  

		</blockquote>## 1.4.2 Calling API from web browser  

### a. Make a simple `GET` request

`get` requests can be checked more simply and quickly through a web browser. The order is as follows:
1. Open web browser
2. Enter the server-side url of the `get` request in the address bar.
	- The server-side URL begins with `http://<IP address of Hi6 controller>:<http communication port>`, followed by the path and query appropriate for the information you want to extract.
	- ex) ```http://192.168.1.150:8888/project/control/ios/dio/do_val?type=dob&blk_no=2&sig_no=3```
3. The page for that URL opens and a response is output as shown below.
	```json
	{
		"_type" : "JObject",
		"val" : -99
	}
	```

<br>

### b. Calling API with `extension`
If you use Chrome or Edge browsers, you can test APIs other than `get` requests through the Chrome extension.  
The following extension program is an API tester used by many developers around the world.
- Chrome extension program : [Talend API Tester](https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm)  

Through this program, you can easily call various APIs like `postman`.

<img src="../../_assets/06_Talend_api_tester.png" style="max-height: 80vh;">

<blockquote>

`(1) Requests/Senarios` : You can set whether to test calls to one API or create a scenario with multiple APIs and test them sequentially.<br>
`(2) Request` : Enter your request.  
`(3) Response` : You can check the response to your request.  
`(4) History` : Prints request history.   
`(5) Side History Tab` : This tab allows you to check a larger amount of history than the request history list in `(4)`, which can be opened and closed.

</blockquote>## 2. version

- Check the current API version or robot controller system version.## 2.1 version/get

- Send a GET request for information about the current API version or robot controller system version.  
- Receive a response by setting the correct path-parameter and query-parameter for each API.  ## 2.1.1 api_ver

### Description

- GET : Optain the Open API version number

### path-parameter

```python
GET /api_ver
```

### response-body

- Open API version number
- The initial Hi6 Open API is a document written based on `version 5`.

### Example

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
```## 2.1.2 sysver

### Description

- GET : Obtain the software version of the robot controller system.

### path-parameter

```python
GET /versions/sysver
```

### response-body

modules : Array of module version information
  - module version information :
    - `name` : module name
		|module name|description|
		|---:|:---|
		|com|robot controller|
		|tp|teaching pendant|
    - `ver` : version number
    - `build-date` : build date
    - `build-time` : build time
    - `commit-id` : Commit ID of source code

### Example

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

Python Script Example

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
```# 3. project

- Reads condition settings, project information, and job file information.
- You can reload updated job files or delete specific job files.## 3.1 project/get

- Send a GET request for condition settings, project information, and job file information.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 3.1.1 `rgen`

### Description

`rgen` (remote general status)

- `GET` : Obtain general information set in the controller.

### path-parameter

```python
GET /project/rgen
```

### response-body

#### 1) Mode
|key|value|type|description|
|:---|:---|:---|:---|
|`cur_mode`| `0` : manual <br> `1` : manual, system settings <br>`3` : auto, 1-cycle <br> `4` : auto, continue (cycle)|`int`|manual/auto mode|
|`enable_state`|`0` Byte(`LSB`) : Motor ON (0: On / 1: Off / 2: Busy) <br> `1` Byte : TP Enable (deadman) Switch (0: OFF / 1: ON)<br>`2` Byte : Machine Lock (0: OFF / 1: ON)<br>`3` Byte : gun Lock (0: OFF / 1: ON)<br>`4` Byte : gun (0: OFF / 1: ON)|`int`||
|`is_playback`|`0` : Pause <br>`1` : play|`int`||
|`is_remote_mode`|`0`: False <br> `1`: True|`int`|Remote mode or not|
|`is_ext_start`|`0`: False <br> `1`: True|`int`|External start-up or not|
|`is_ext_prog_sel`|`0`: False <br> `1`: True|`int`|Whether to select an external program|

<br>

#### 2) current program counter
This is the point where the bar cursor on the teach pendant JOB panel is located in manual mode or automatic mode. This is the currently executing statement or the target location for editing.
|key|type|description|
|:---|:---|:---|
|`cur_prog_no`|`int`|current program number|
|`cur_step_no`|`int`|current step number|
|`cur_func_no`|`int`|current function number|

<br>

#### 3) moving program counter

This is the target step the robot is moving during playback.
|key|type|description|
|:---|:---|:---|
|`mov_prog_no`|`int`|moving program number|
|`mov_step_no`|`int`|moving step number|
|`mov_func_no`|`int`|moving function number|

<br>

#### 4) Speed

|key|type|description|
|:---|:---|:---|
|`spd_lev`|`int`|Manual mode jog speed level (1~8)|
|`manual_spd_max`|`int`|Manual mode maximum speed (mm/sec)|
|`auto_spd`|`int`|Auto mode playback speed (%)|
|`jog_inch_status`|`int`|jog inching state (0:OFF/ 1:ON)|
|`step_execute_unit_status`|`int`|StepFWD execution unit (run to)<br>0: Cmd <br>1: Step<br>2: End |
|`cont_path`|`int`|continuous motion mode (0~2)|

<br>

### Example
Python Script Example

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
## 3.1.2 `jobs_info`

### Description

`jobs_info`

- `GET` : Obtain information about job programs.

### path-parameter

```python
GET /project/jobs_info
```

### response-body

- [job file information](../../99-schema/jobs_info.md)
### Example

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

Python Script Example

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
```## 3.1 project/post

- Send a POST request for condition settings, project information, and job file information.
- You must write the correct request-body for each API.## 3.2.1 `reload_updated_jobs`

### Description

`reload_updated_jobs`

- `POST` : Send a request to update working files.
- When transmitting a job file to the controller via FTP, a reload request must be made through the corresponding API for the transmitted job file to be reflected in memory.

### path-parameter

```python
POST /project/reload_updated_jobs
```

### request-body

```json
{}
```

### Description

```python
request url:
POST /project/reload_updated_jobs

request-body: {}
```

Python Script Example

- Please refer to [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) for the response HTTP status code.
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
## 3.2.2 `delete_job`

### Description

`delete_job`

- `POST` : Send a request to remove a working file.

### path-parameter

```python
POST /project/jobs/delete_job
```

### request-body

```json
{
  "fname": "0001.job"
}
```

### Example

```json
request url:
POST /project/jobs/delete_job

request-body: 
{
	"fname": "0001.job"
}
```

Python Script Example

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
```# 4. control

- Apply settings of the controller and process input/output values.
- It covers information on system input/output, digital input/output, condition settings, and user coordinate system.

<br>## 4.1 control/get

- Send a GET request for controller setting information and input/output values.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 4.1.1 `op_cnd`

### Description

`op_cnd` (operation condition)

- `GET` : Obtain the condition setting value.

### path-parameter

```python
GET /project/control/op_cnd
```

### response-body

- [Condition Setting parameter](../../99-schema/op_cnd.md)

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

Python Script Example

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
```## 4.1.2 `ios/dio/{dio_val}`

### Description

`dio` (digital input/output)

- `GET` : Obtain user IO values.

### path-parameter

```python
GET /project/control/ios/dio/{dio_val}
```

### path-variable

- `dio_val` :
  - `di_val` : Get the input(di) value.
  - `do_val` : Get the output(do) value.

### query-parameter

- `type` : Type of io value
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : block number (0~9)
- `sig_no` : signal index (0~)

### Example

- Get the fb2.dob3 value. (Result : 0b11001000 = 0xc8 = -56)

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

def get_dio_val() -> dict:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/project/control/ios/dio/do_val'
    query_parameter = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3 }
    
    response = requests.get(url=base_url + path_parameter, params=query_parameter).json()

    return response

print(get_dio_val())
```
```sh
$python test.py
{'_type': 'JObject', 'val': -56}
```## 4.1.3 `ios/sio/{sio_val}`

### Description

`sio` (system input/output)

- `GET` : Get system IO values.

### path-parameter

```python
GET /project/control/ios/sio/{sio_val}
```

### path-variable

- `sio_val` :
  - `si_val` : Get the input(si) value.
  - `so_val` : Get the output(so) value.

### query-parameter

- `type` : Type of io value
  - si or so : bit
  - sib or sob : signed-byte
  - siw or sow : signed-word (2byte)
  - sil or sol : signed-dword (4yte)
  - sif or sof : float
- `sig_no` : signal index (0~)


### Example

- Get sib1 value. (Result : 0b00000010 = 0x02 = 2)

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
```## 4.1.4 `ucss/ucs_nos`

### Description

`ucss/ucs_nos` (user coordinate system numbers)

- `GET` : Obtains a list of user coordinate systems currently in use.
- Prints a list of user coordinate systems registered through `system > 2: Control parameter > 6: Coordinate registration`.

### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

### Example

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
```## 4.2 control/post

- Sends a POST request for the controller’s setting information and input/output values.
- You must write the correct request-body for each API.## 4.2.1 `ios/dio/{do_val}`

### Description

`do` (digital output)

- `POST` : Change digital output.

### path-parameter

```python
POST /project/control/ios/dio/do_val
```

### request-body

```json
{
  "type": "do",
  "blk_no": 1,
  "sig_no": 1,
  "val": 1
}
```


### query-parameter

- `type` : Type of io value
  - di or do : bit
  - dib or dob : signed-byte
  - diw or dow : signed-word (2byte)
  - dil or dol : signed-dword (4yte)
  - dif or dof : float
- `blk_no` : block number (0~9)
- `sig_no` : signal index (0~)
- `val` : Setting value you want to change


### Example

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

Python Script Example

- Please refer to [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) for the response HTTP status code.
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
```## 4.3 control/put

- Sends a PUT request for the controller’s setting information and input/output values.
- You must write the correct request-body for each API.## 4.3.1 `op_cnd`

### Description

`op_cnd` (operation condition)

- `PUT` : Change the robot’s condition setting values.
- If you open the `condition setting window(cond.set)` in TP and request the corresponding method,  
you must close and reopen the window for the value to be reflected.

### path-parameter

```python
PUT /project/control/op_cnd
```

### request-body

- [Condition Setting parameter](../../99-schema/op_cnd.md)


### Example

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
```# 5. robot

- You can check remote control and monitoring of robot and tool data.
- It covers motor on/off, robot posture, tools, jog coordinate system, etc.
## 5.1 robot/get

- Send GET requests for robot and tool data.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 5.1.1 `motor_on_state`

### Description

`motor_on_state`

- `GET` : Obtain the motor on status.

### path-parameter

```python
GET /project/robot/motor_on_state
```

### response-body

- val :
  - `0` : on
  - `1` : busy (Transitioning state)
  - `2` : off

### Example
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
```## 5.1.2 `po_cur`

### Description

`po_cur` (pose current)

- `GET` : Get the pose the robot is currently taking.

### path-parameter

```python
GET /project/robot/po_cur
```

### query-parameter

- `task_no` : task number (0~7).
  - unspecified : Applied as task 0.
  - &gt;=0 : If mechinfo is not specified, the current mechinfo of the task is applied.
- `crd` :  
  - unspecified : Obtain all tcp, axis, and encoder.
  - <0 : Follows the current recording coordinate system.
  - &gt;=0 : [coordinate system](../../99-schema/crdsys.md)
- `ucrd_no` : User coordinate system number (Specified only when crd is user.)
- `mechinfo` : [Mechanism information](../../99-schema/mechinfo.md)

### response-body

- [Pose information](../../99-schema/pose.md)


### Example

Example of a system with 6 robot axes (j1~j6) + 1 driving axis (j7) + 2 positioner axes (j8, j9).

- Obtain only the base coordinates of the robot

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

- Obtaining axis coordinates of all axes

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

- Obtain the axis coordinates of the positioner 2 axis (i.e. mechanism M2)

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

Python Script Example

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
```## 5.1.3 `cur_tool_data`

### Description

`cur_tool_data`

- `GET` : Obtaining the robot's current tool data.

### path-parameter

```python
GET /project/robot/cur_tool_data
```

### response-body

- val : [Tool Data](../../99-schema/tool_data.md)

### Example

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

Python Script Example

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
```## 5.1.4 `tools`

### Description

`tools`

- `GET` : Get all tool information for the robot. Only tools that exist among tools from T0 to T31 are obtained.

### path-parameter

```python
GET /project/robot/tools
```

### response-body

- t_0 : [Tool data](../../99-schema/tool_data.md)
- t_1 : Tool data
- t_2 : Tool data  
...
- t_31 : Tool data

### Example

An example of a system in which only tool 0 and tool 31 exist.

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

Python Script Example

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
```## 5.1.5 `tools/t_{number}`

### Description

`tools/t_{number}`

- GET : This is a function that receives information on the settings of a specific tool.

### path-parameter

```python
GET /project/robot/tools/t_{number}
```

### response-body

- [Tool data](../../99-schema/tool_data.md)

### Example

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

Python Script Example

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
```## 5.2 robot/post

- Send POST requests for robot and tool data.
- You must write the correct request-body for each API.## 5.2.1 `motor_on / motor_off`

### Description

- POST : Performs motor ON and motor OFF.

### path-parameter

```python
POST /project/robot/motor_on
POST /project/robot/motor_off
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### Example

```python
POST /project/robot/motor_off

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

def post_motor_off() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_off'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
print(f"Motor-OFF response: {post_motor_off()}")
```
```sh
$python test.py
Motor-ON  response: 200
Motor-OFF response: 200
```## 5.2.2 `start / stop`

### Description

- POST : Performs robot start and robot stop.

### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### Example

```python
POST /project/robot/motor_off

request-body: 
{}
```

Python Script Example

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # Requires automatic mode and motor on settings
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
```## 5.2.3 `tool_no`

### Description

- POST : Set the current tool number.

### path-parameter

```python
POST /project/robot/tool_no
```

### request-body

- `val` : Tool number
  - `robot tools` : `0` ~ `31`
  - `stationary tool` : `0` ~ `3`

### response-body

```json
{
    "_type": "JObject"
}
```

### Example

```json
POST /project/robot/tool_no

request-body
{
  "val": 1
}
```

Python Script Example

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
```## 5.2.4 `crd_sys`

### 설명

- POST : Set the current jog coordinate system.

### path-parameter

```python
POST /project/robot/crd_sys
```

### request-body

- [Coordinate system](../../99-schema/crdsys.md)

### response-body

```json
{
  "_type": "JObject",
  "cur_crd": 1,
  "ucrd_no": 1
}
```


### Example

```json
POST /project/robot/crd_sys

request-body
{
  "val": 1
}
```

Python Script Example

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
```# 6. I/O PLC

- Reads or sets the input/output values of the built-in PLC.## 6.1 io_plc/get

- Sends a GET request for input/output values of a built-in PLC.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 6.1.1 `relay values`

### Description

- `GET` :Obtain the relay value for the entire object type.

### path-parameter

```python
GET /project/plc/[{obj_type}{obj_idx}_]{relay_type}/val_s32
```

### path-variable

[relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/english/3-relay/2-relay-expression) (lowercase letter)

* (`{obj_type}{obj_idx}_` must be specified for `di`, `do`, `x`, and `y`. The remaining `relay_type` is not specified.)

- `obj_type` : object type
  - `fb`
  - `fn`

- `obj_idx` : object index (fb: 0~9, fn: 0~63)

- `relay_type` : 
	|`di`|`do`|`x` |`y` |`m` |`s` |`r`|`k`|
	|:---|:---|:---|:---|:---|:---|:---|:---|

	

### query-parameter

- `st` : start byte index (default: 0)
- `len` : number of words (default: 8)


### Example

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
```## 6.2 io_plc/post

- Sends a POST request for input/output values from a built-in PLC.
- You must write the correct request-body for each API.## 6.2.1 `set_relay_value`

### Description
`set_relay_value`

- `POST` : Set the relay value.

### path-parameter

```python
POST /project/plc/set_relay_value
```

### request-parameter

- `name` : Enter the relay name you want to set according to [relay expression](https://hrbook-hrc.web.app/#/view/doc-hi6-embedded-plc/english/3-relay/2-relay-expression).
- `value` : Please pay attention to ‘data-type’ in the notation above and enter the value you want to set.
```json
{
	"name": "fb3.dof14",
	"value": "2.718"
}
```

### Example

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
```# 7.1 event-log

- Outputs errors, warnings, execution history, etc. recorded in the controller.## 7.1 log_manager/get

- Send a GET request for errors, warnings, and execution history recorded in the controller.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 7.1.1 search

### Description

`search`

- `GET` : View the event log using the specified filter conditions.

### path-parameter

```python
GET /logManager/search
```

### query-parameter

- `n_item` : Number of requested events (default=100)
- `cat_p` : Request category filter (category positive). Specify the letters representing each type by combining them with a comma (,). (cat_p=E,W,N)
  - `E` : Error
  - `W` : Warning
  - `N` : Notice
  - `S` : Start/Stop
  - `O` : user's Operation
  - `I` : I/O, relay value
  - `P` : Periodic state
  - `H` : History
  - `C` : Console out
  - `M` : Miscellany
- `id_min` : min id filter. (optional)
  - Every event has a unique event ID (eid). (0~)  
    If you request a history by adding 1 to the maximum ID of the previously received events and specifying it in `id_min`, you can obtain only the newly occurring history, excluding the events already received.
  - However, when the event ID in the controller reaches the maximum value (0xffffffffffffffff), it is generated again starting from 0.  
    Filtering is applied appropriately by taking these situations into consideration.  
    For example, if id_min is 0xfffffffffffffffa, events with ids such as 0, 1, and 2 are not filtered out but are included in the response.
- `id_max` : max id filter. (optional)
- `ts_min` : min timestamp filter. (optional)
  - Year/Month/Date Hour:Minute:Second.Millisecond Format. e.g. 2023/11/20 18:50:30.955
- `ts_max` : max timestamp filter. (optional)
  - Year/Month/Date Hour:Minute:Second.Millisecond Format. e.g. 2023/11/20 18:50:30.955

### response-body

- `id` : event ID
- `ts` : timestamp
- `cat` : event category
- `code` : event code number
- `aux` : event auxiliary info. Up to 280 characters.
  - In case of errors, warnings, and start/stop, snapshot information is included.

```json
{ "id" : 19964, "ts" : "2023/11/20 15:53:11.275", "cat" : "E", "code" : "11,0,0", "aux" : "{ 'pc' : '20/3/1', 'j1' : 18.525, 'j2' : 105.000, 'j3' : -2.577, 'j4' : -14.432, 'j5' : -0.776, 'j6' : 0.314, 'sin' : '00 01 00 00 00 00 00 00', 'sout' : '05 08 06 00 00 00 00 01', 'din' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0', 'dout' : '00 00 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 C0' }" }
{ "id" : 18314, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(    976)Power saving = on " }
{ "id" : 18313, "ts" : "2023/11/20 15:05:33.788", "cat" : "H", "code" : "hist", "aux" : "(=Stamp=)[2023/11/20 15:05:33](+299996445us) " }
{ "id" : 18312, "ts" : "2023/11/20 15:05:33.787", "cat" : "N", "code" : "5", "aux" : "{ 'pc' : '20/3/1' }" }
{ "id" : 18267, "ts" : "2023/11/20 15:00:33.791", "cat" : "H", "code" : "hist", "aux" : "(   2001)    .end ;(P20/S3/F1) " }
{ "id" : 18266, "ts" : "2023/11/20 15:00:33.789", "cat" : "H", "code" : "hist", "aux" : "( 738785)S3  .move P,spd=500mm/sec,accu=4,tool=0 " }
```

### Example

<blockquote>

```python
request url:
GET /logManager/search?cat_p=O&id_max=24258&id_min=24253

response-body:
{
    { "id" : 24258, "ts" : "2023/11/28 16:53:31.239", "cat" : "O", "code" : "K.Click", "aux" : "Right" }
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
```# 8. file_manager

- This covers functions such as reading file information from the controller, changing file names, and transferring files.
- Functions for checking the existence of a directory or creating and deleting it are also covered.## 8.1 file_manager/get

- Send a GET request for file information from the controller.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 8.1.1 `files`

### Description

`files`

- `GET` : The file contents are responded to from the controller.

### path-parameter

```python
GET /file_manager/files
```

### query-parameter

query-parameter must be entered.  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : File name to get

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|Return file contents|
|`404 Not Found`| Return error status code when file does not exist|


### Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job   <- target
    |-- lads
    |-- log
    |-- vars   
    |-- ...
    `-- hi6_proj.json
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
```## 8.1.2 `file_info`

### Description

`file_info`

- `GET` : Obtain information about that file based on the file path.

### path-parameter

```python
GET /file_manager/file_info
```

### query-parameter

query-parameter must be entered.  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : target file path

### response-body

- [file information](../../99-schema/file_info)
- If the file does not exist, `404 Not Found`

### Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job <- target 
    |-- lads
    |-- log
    |-- vars
    |-- ...
    `-- hi6_proj.json
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

Python Script Example

```python
# test.py
import requests

def get_file_info() -> dict:
    base_url         = "http://192.168.1.150:8888"
    path_parameter   = "/file_manager/file_info"
    query_parameter  = {"pathname": "project/hi6_proj.json"}

    response = requests.get(url = base_url + path_parameter, params = query_parameter)

    return response.json()

print(get_file_info())
```
```sh
$python test.py
{'mday': 31, 'sec': 40, 'fname': 'hi6_proj.json', 'wday': 2, 'size': 130551, 'year': 2023, 'hour': 7, 'readonly': False, 'month': 10, 'is_dir': False, 'min': 57}
```## 8.1.3 `file_list`

### Description

`file_list`

- `GET` : Obtain a list of files and directories.

### path-parameter

```python
GET /file_manager/file_list
```

### query-parameter

query-parameter must be entered.  

```text
?path=project/jobs&incl_file=true&incl_dir=false
```

|key|description|
|:---|:---|
|`path`|Target path you want to check|
|`incl_file`|Whether to include files when outputting the list|
|`incl_dir`|Whether to include directories when outputting the list|


### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|return [file information](../../99-schema/file_info) `list`|
|`404 Not Found`| no file exists |


### Example

<blockquote>

```
hi6
`-- project     <- target
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
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
		"fname": "hi6_proj.json",
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
```## 8.1.4 `file_exist`

### Description

`file_exist`

- `GET` : Obtain the existence of the target file.

### path-parameter

```python
GET /file_manager/file_exist
```

### query-parameter

query-parameter must be entered.  

```text
?pathname=project/jobs/0001.job
```

- `pathname` : target file path

### response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`|`true` (file exists)|
|`200 OK`|`false` (no file exist)|


### Example

<blockquote>

```python
request url:
GET /file_manager/file_exist?pathname=project/jobs/1234.job

response-body: 
false
```
```
hi6
`-- project
    |-- jobs
    |   `-- 0001.job
    `-- hi6_proj.json
```

</blockquote>

Python Script Example

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
```## 8.2 file_manager/post

- Sends a POST request for file information from the controller.
- You must write the correct request-body for each API.# 8.2.1 `rename_file`

## Description

`rename_file`

- `POST` : Change the file name of the target file.

## path-parameter

```python
POST /file_manager/rename_file
```

## request-body

```json
{
	"pathname_from" : "project/jobs/0001.job",
	"pathname_to"   : "project/jobs/4321.job"
}
```
- `pathname_from` : File path before change
- `pathname_to` : File path after change

## response-body

|HTTP Status|description|
|:---|:---|
|`200`| Works fine. |
|`400`| No file exists to rename. |


## Example

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
hi6
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
```# 8.2.2 `mkdir`

## Description

`mkdir`

- `POST` : Create a directory in the target path.

## path-parameter

```python
GET /file_manager/mkdir
```

## request-body

|key|value|description|
|:---|:---|:---|
|`path`|`str`|Where to create the directory|

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| Directory creation completed in target location|
|`500 Internal Server Error`| When directory names are duplicated in the target location |


## Example

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
hi6
`-- project
    |-- jobs
    |   `-- special    <- target
    `-- hi6_proj.json
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
```# 8.2.3 `files`

## Description

`files`

- `POST` : Transfer the file to the target path.

## path-parameter

```python
POST /file_manager/files/{target_filepath}
```

## path-variable

- `target_filepath` : Target file path including extension.

## request-body

- `Content-Type` must be `application/octet-stream`.

## response-body

|HTTP Status|description|
|:---|:---|
|`200 OK`| Transfer completed |


## Example

<blockquote>

```
hi6
`-- project
    |-- jobs
    |   `-- test.job    <- target
    `-- hi6_proj.json
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
    path_value      = '/project/jobs/test.job' # target

    target_file     = base_url + path_parameter + path_value
    source_file     = 'D:\\temp\\test.job' # source (path for WindowOS)

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
```## 8.3 file_manager/delete

- Send a DELETE request for file information from the controller.## 8.3.1 `files`

### Description

`files`

- `DELETE` : Deletes the target file or directory.

### path-parameter

```python
DELETE /file_manager/files/{target-filepath}
```

### response-body
|HTTP Status|description|
|:---|:---|
|`200 OK`| Target deletion completed, 200 returned even if there is no target |


### Example

<blockquote>

```python
request url:
DELETE /file_manager/files/project/jobs/special
```
```
hi6
`-- project
    `-- jobs
        `-- test.job   <- target
```

</blockquote>

Python Script Example

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
```# 9.task

- It covers content related to the task.
- You can reset a specific task or all tasks.
- You can read values from local or global variables of the current task or declare new variables.
- During task execution, specific actions (e.g. release) can be taken for a specific work flow (e.g. wait).## 9.1 task/get

- Send a GET request for information related to the task.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 9.2 task/post

- Sends a POST request for information related to the task.
- You must write the correct request-body for each API.## 9.2.1 `task/cur_prog_cnt`

### Description

`cur_prog_cnt` (current program counter)

- `POST` : Sets the current program counter for the task.

### path-parameter

```python
POST /project/context/tasks[0]/cur_prog_cnt
```

### request-body

- [cur_prog_cnt request parameter](../../99-schema/cur_prog_cnt.md)

### response-body

- [cur_prog_cnt response parameter](../../99-schema/cur_prog_cnt.md)

### Example

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
```## 9.2.2 `task/reset`

### Description

- `POST` : Perform a reset on the task. (Same operation as R.. 0 ENTER)

### path-parameter

```python
# reset all the tasks
POST /project/context/tasks/reset 

# reset the selected task
POST /project/context/tasks[{task index}]/reset 
```

### request-body

```json
{}
```

### Example

reset task 0

```python
request url:
GET /project/context/tasks[0]/reset
```

Python Script

```python
import requests

def post_task_reset() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/reset'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_task_reset()}")
```
```sh
$python test.py
response: 200
```## 9.2.4 `assign_var_expr`

### Description

`assign_var_expr`

- `POST` : Reassigns a variable in the current task statement.

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_expr
```

### request-body

- `name` : variable name
- `expr` : expression to substitute into variable
- `save` : Whether to save (true/false). This is to save the data in the variable file.
- `scope` : Setting the effective scope of the variable
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|


```json
{
    "name" : "a",
    "scope": "local",
    "expr" : "14 + 2",
    "save" : "true"
}
```

### Example

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

When the above job file is executed and a local variable `a` is declared in the task

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

Python Script Example

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
```## 9.2.5 `assign_var_json`

### Description

`assign_var_json`

- `POST` : Reassigns a variable in the current task statement.  

### path-parameter

```python
POST /project/context/tasks[0]/assign_var_json
```

### request-body

- `name` : variable name
- `json` : A json format `string` to be substituted into a variable.
- `save` : Save contents (true/false). That is until you save that data to your activity file.
- `scope` : Setting the effective scope of the variable
	|`local`|`global`|`Not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|


```json
{
    "name" : "a",
    "scope": "local",
    "json" : "{\"test\": 10}",
    "save" : "true"
}
```

### Example

<blockquote>

```text
Hyundai Robot Job File;
    var a = 1234
    end
```

When the above job file is executed and a local variable `a` is declared in the task

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

Python Script Example

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
```## 9.2.6 `release_wait`

### Description

`release_wait`

- `POST` : release syntax
- Requirements: TP > system > 1: User environment > `wait(di/wi) release` > `Enable` click

### path-parameter

```python
POST /project/context/tasks[0]/release_wait
```

### request-body

```json
{}
```

### response-body

- `200` : request success
- `403` : Failure to meet the above requirements

### Example

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python Script Example

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
```## 9.2.3 `set_cur_pc_idx`

### Description

`set_cur_pc_idx`

- `POST` : Function that positions the current cursor at the index line

### path-parameter

```python
POST /project/context/tasks[0]/set_cur_pc_idx
```

### request-body
```json
{
  "idx": 1
}
```

### Example

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

Python Script Example

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
response 200 # Cursor position on TP changed
```## 9.2.7 `solve_expr`

### Description

`solve_expr`

- `POST` : Solve the expression and set the resulting value to a local or global variable of the task.

### path-parameter

```python
POST /project/context/tasks[0]/solve_expr
```

### request-body
- `expr` : Enter the expression you want to solve
- `scope` : Sets the scope for `expr`.

	|`local`|`global`|`not set`|
	|:---|:---|:---|
	|local variable|global variable|Full scope (local and global are set automatically)|

```json
{
	"expr" : "a",
	"scope" : "local"
}
```

### response-body

```json
13 // Reads the expr value within the currently specified scope.
```

### Example

<blockquote>

```python
# 1. Read the value of “local” variable a declared in the current Task
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
# 2. Read the value of “global” variable a declared in the current Task
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
# 3. Add -234 to the value of local variable a
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
- Execute the following code with the local and global variable a values set in the task area of the robot controller.

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
```# 10. etc

- It covers system version, event log, clock, etc.# 10.1 clock

- You can read and set the controller's system time.## 10.1.1 clock/get

- Send a GET request for the controller system time.
- Receive a response by setting the correct path-parameter and query-parameter for each API.## 10.1.1.1 `date_time`

### Description

`date_time`

- `GET` : Obtain the set system time.

### response-body

- [date time](../../../99-schema/date_time.md)

### Example

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

Python Script Example

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
```## 10.1.2 clock/put

- Sends a PUT request to the controller system time.
- You must write the correct request-body for each API.## 10.1.2.1 `date_time`

### Description

`date_time`

- `PUT` : Change the system time.

### request-body

- [date time](../../../99-schema/date_time.md)

### Example

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

Python Script Example

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
```# Schema

This chapter contains references to various enumerations and structures used in Open API.

## crdsys

### Description

This is an enumeration that specifies the coordinate system.
|value|description|
|:---:|:---|
|`-1`|`Next` coordinate system|
|`0`|`axis` coordinate system|
|`1`|`orthogonal`(= `robot`) coordinate system|
|`2`|`user` coordinate system|
|`3`|`tool` coordinate system|
## cur_prog_cnt

### Description
Sets the current program counter for the task.

### request body
|key|type|description|
|:---|:---|:---|
|`pno`|int|Program number (if -1, keep current number)|
|`sno`|int|Step number (if -1, keep current number)|
|`fno`|int|Function number (if -1, keep current number)|
|`ext_sel`|int|`0` : Internal selection (prohibited in remote mode) <br> `1` : External selection (only allowed in remote mode)|

### response body
|key|type|description|
|:---|:---|:---|
|`sno_new`|int|Newly moved step number|
|`fno_new`|int|Newly moved function number|
|`ln_new`|int|Newly moved line number (program header is 0, first statement is 1)|## date_time

### Description

Indicates system time-related information.
|value|type|description|
|:---:|:---|:---|
|"year"|`int`|Year of current system|
|"mon"|`int`|Month of current system|
|"day"|`int`|Day of current system|
|"hour"|`int`|Hour of current system|
|"min"|`int`|Minute of current system|
|"sec"|`int`|Second of current system|
## file_info

### Description

This parameter is returned when requesting file information.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|file name|
|size|`int`|file size(B, Byte)|
|year|`int`| `year` the file was modified |
|month|`int`| `month` the file was modified` |
|mday|`int`| `day` the file was modified |
|wday|`int`| `Day of the week` on which the file was modified (0: Sun, 1: Mon, 2: Tue, ...) |
|hour|`int`| `hour` the file was modified |
|min|`int`| `minute` the file was modified |
|sec|`int`| `second` the file was modified |
|is_dir|`bool`| Check if current file is a directory |
|readonly|`bool`| Check if the file is read-only |
## jobs_info

### Description

This is a job file information parameter.

|key|type|description|
|:---:|:---|:---|
|fname|`str`|name of job file|
|job_comment|`str`|comment|
|n_step|`int`|number of steps|
|n_total_ax|`int`|number of axes|
|n_aux_ax|`int`|Number of additional axes|
## mechinfo

### Description

Mechanism info
Celebrate with a bit-field which activities are used.

- bit 0 : M0
- bit 1 : M1
- bit 2 : M2
- bit 3 : M3
- bit 4 : M4
- bit 5 : M5
- bit 6 : M6
- bit 7 : M7

### Example

```python
0x13 = 0b00010011 = M4 | M1 | M0
# Specify mechanisms M0, M1, and M4.
```
## op_cnd

### Description
op_cnd (operation condition) : value of `Condition setting`  
You can check the values when you press the `Condition setting` button in TP.  

<br>

|key|value|description|
|:---|:---|:---|
|playback_mode| `1` : 1 cycle <br> `2` : repeat|Automatic operation cycle mode|
|step_goback_max_spd|`10` ~ `250` (mm/sec)|Maximum speed when stepping forward/reverse|
|step_go_func_ex|`0` : invalid <br> `1` : valid <br> `2` : I ON (=DI signal)|Function execution when advancing step|
|func_reexe_on_trace| `0` : invalid <br> `1` : valid |After stepping backwards, re-execute the function when moving forward|
|path_recov_confirm|`0` : invalid <br> `1` : valid|Path recovery when stepping forward/backward|
|playback_spd_rate|`1` ~ `100` (%)|Automatic operation speed ratio|
|robot_lock|`0` : invalid <br> `1` : valid |Robot Lock|
|intp_base|`0` : robot tool <br> `1` : stationary tool|Interpolation criteria|
|ucrd_num|`0` ~ `20`|Specify user coordinate system|
|plc_mode|`0` : Off -> Stop <br> `1` : Stop -> Remote Stop <br> `2` : Remote Stop -> Remote Stop <br> `3` : Remote Run -> Remote Stop <br> `4` : Run -> Off|PLC operation mode|

<br>

### Example

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
## Pose

### Description

Pose Data.

|key|description|
|:---|:---|
|x|X position (mm)|
|y|Y position (mm)|
|z|Z position (mm)|
|rx|RX Angle (deg.)|
|ry|RY Angle (deg.)|
|rz|RZ Angle (deg.)|
|j1~j16|1~16 axis values(mm or deg.)|
|crd|[Coordinate system](./crdsys.md)|
|mechinfo|[Mechanism information](./mechinfo.md)|
|nsync|Number of sensor synchronization values (0~2)|
|sync|Sensor synchronization value (string). e.g. `"sync(220.5,195.3)"`|## tool_data

### Description

Robot's tool data.

|key|description|
|:---:|:---|
|`x`|X position (mm)|
|`y`|Y position (mm)|
|`z`|Z position (mm)|
|`rx`|RX Angle (deg.)|
|`ry`|RY Angle (deg.)|
|`rz`|RZ Angle (deg.)|
|`mass`|weight (kg.)|
|`cx`|Center of gravity at X position (mm)|
|`cy`|Center of gravity at Y position (mm)|
|`cz`|Center of gravity at Z position (mm)|
|`ixx`| inertial X (kgm2)|
|`iyy`| inertial Y (kgm2)|
|`izz`| inertial Z (kgm2)|
|`mass_esti`|Load estimate weight (kg.)|

