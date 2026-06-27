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