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