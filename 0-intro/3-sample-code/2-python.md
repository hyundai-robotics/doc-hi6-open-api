### 1.3.2 Sample code - python

The example code mainly describes `a. synchronous request`.


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