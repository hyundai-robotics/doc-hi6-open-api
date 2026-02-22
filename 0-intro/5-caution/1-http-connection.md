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