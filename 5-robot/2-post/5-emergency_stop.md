#### 5.2.5 `emergency_stop`

- <b style="color:orange"> 对于版本低于 ***<u>60.30-00</u>*** 的，请参考 ***<u>[emergency_stop_test](./6-emergency_stop_test.md)</u>*** 而不是 emergency_stop。 </b>  

##### 描述

- 支持版本 : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  
- 应用与按下紧急停止按钮相同的减速曲线。  
- 由于网络延迟或请求处理时间，API 的响应速度可能比物理按钮慢。  


##### 路径参数

```python
POST /project/robot/emergency_stop
```

##### 请求体
```python 
{}
```

##### 状态码

- 200 : 请求成功  
- 400 : 请求失败（紧急停止序列执行失败）    

##### 示例

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

Python 脚本示例

```python
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {post_emergency_stop()}")
```
```sh
$python test.py
响应: 200
```