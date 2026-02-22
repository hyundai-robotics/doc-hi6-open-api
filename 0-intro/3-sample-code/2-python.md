#### 0.3.2 示例代码 - python

示例代码主要描述 `a. 同步请求`。


||同步|异步|
|:---|:---|:---|
|阻塞|`a. 同步请求`||
|非阻塞||`b. 异步请求`|

这两种方法之间的差异可能对TP和控制器产生严重后果，例如：
1. 由于UI线程中频繁调用同步函数，UI可能无法流畅运行并可能会冻结 (`挂起问题`)。
2. 如果由于服务器（控制器）端的问题未收到响应，则应用程序UI可能会冻结 (`挂起问题`)。

因此，在开发实际应用时，请以异步方式编写代码。  
- 请注意，${cont_model} Open API 描述中编写的python脚本示例是为了便于理解而同步编写的。  


<br>

##### a. 同步请求
同步是一种阻塞状态的请求方法，在一个请求完成并收到响应之前，无法执行其他任务。  
在Python中，`synchronous` HTTP请求的广泛使用库是 `requests`。
如果您没有 `requests` 库，可以通过Python包管理器进行安装。  

- 请记住，如果在通信时未收到响应或收到响应需要很长时间，可能出现挂起问题的可能性非常高。

```python
# sync.py - 同步，获取和设置用户IO输出值
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
print('[post]', hex(val), '设置到 fb2.do3', f"耗时: {end_time - start_time} 秒")

# (GET) 获取 fb2.do3 值
total_start_time = time.time()
for _ in range(5):
    start_time = time.time()
    resp = requests.get(url + path, headers=head, params=query)
    end_time = time.time()
    resp_body = resp.json()
    print('[get]', hex(resp_body['val']), '从 fb2.do3 获取', f"耗时: {end_time - start_time} 秒")
total_end_time = time.time()
print(f"总请求时间 : {total_end_time - total_start_time} 秒")
```
```bash
$python sync.py
[post] 0x79 到 fb2.do3 耗时: 0.004312038421630859 秒
[get] 0x79 从 fb2.do3 耗时: 0.05764031410217285 秒
[get] 0x79 从 fb2.do3 耗时: 0.06277251243591309 秒
[get] 0x79 从 fb2.do3 耗时: 0.0634009838104248 秒
[get] 0x79 从 fb2.do3 耗时: 0.06106710433959961 秒
[get] 0x79 从 fb2.do3 耗时: 0.04711771011352539 秒
总请求耗时 : 0.292741060256958 秒
```