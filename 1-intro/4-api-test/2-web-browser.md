## 1.4.2 Calling API from web browser  

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

<img src="../../_assets/06_Talend_api_tester.png" height="850vh">

<blockquote>

`(1) Requests/Senarios` : You can set whether to test calls to one API or create a scenario with multiple APIs and test them sequentially.<br>
`(2) Request` : Enter your request.  
`(3) Response` : You can check the response to your request.  
`(4) History` : Prints request history.   
`(5) Side History Tab` : This tab allows you to check a larger amount of history than the request history list in `(4)`, which can be opened and closed.

</blockquote>