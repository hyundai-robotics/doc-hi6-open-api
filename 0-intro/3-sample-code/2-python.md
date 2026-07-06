#### 0.3.2 示例代码 - python

示例代码主要描述 `a. 同步请求`。

||同步|异步|
|:---|:---|:---|
|阻塞|`a. 同步请求`||
|非阻塞||`b. 异步请求`|

这两种方法之间的差异可能对 TPs 和控制器产生严重后果，如：
1. 由于 UI 线程中频繁的同步函数调用，UI 可能无法流畅运行并可能冻结（`挂起问题`）。
2. 如果由于服务器（控制器）端的问题未收到响应，应用程序 UI 可能冻结（`挂起问题`）。

因此，在开发实际应用程序时，请以异步方式编写代码。  
- 请注意，在 ${cont_model} 开放 API 描述中编写的 python 脚本示例是同步编写的，以便于理解。

<br>

##### a. 同步请求
同步是一种阻塞状态的请求方法，在完成一个请求并收到响应之前，无法执行其他任务。  
在 Python 中用于 `同步` HTTP 请求的广泛使用的库是 `requests`。  
如果没有 `requests` 库，可以通过 Python 包管理器进行安装。

```sh
$pip install requests
```

- 请记住，如果在通信时未收到响应或者需要很长时间才能收到响应，发生挂起问题的可能性可能非常高。

```python
# sync.py - 同步，获取和设置用户 IO 输出值
import requests
import time

url='http://192.168.1.150:8888'
head = {'Content-Type': 'application/json; charset=utf-8'}
path = '/project/control/ios/dio/do_val'
query = {'type': 'dob', 'blk_no': 2, 'sig_no': 3 }

# (POST) 设置 fb2.do3 值
val = 0x79
req_body = { 'type': 'dob', 'blk_no': 2, 'sig_no': 3, 'val' : val }
start_time = time.time()
resp = requests.post(url + path, headers=head, json=req_body)
end_time = time.time()
print('[post]', hex(val), '到 fb2.do3', f"耗时: {end_time - start_time} 秒")

# (GET) 获取 fb2.do3 值
total_start_time = time.time()
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), '来自 fb2.do3', f"耗时: {end_time - start_time} 秒")
total_end_time = time.time()
print(f"总请求时间 : {total_end_time - total_start_time} 秒")
```
```bash
$python sync.py
[post] 0x79 到 fb2.do3 耗时: 0.004312038421630859 秒
[get] 0x79 来自 fb2.do3 耗时: 0.05764031410217285 秒
[get] 0x79 来自 fb2.do3 耗时: 0.06277251243591309 秒
[get] 0x79 来自 fb2.do3 耗时: 0.0634009838104248 秒
[get] 0x79 来自 fb2.do3 耗时: 0.06106710433959961 秒
[get] 0x79 来自 fb2.do3 耗时: 0.04711771011352539 秒
总请求时间 : 0.292741060256958 秒
```