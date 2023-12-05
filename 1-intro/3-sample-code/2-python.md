### 1.3.2 Sample code - python

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

## a. Synchronous request
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

## b. Asynchronous request  
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
```