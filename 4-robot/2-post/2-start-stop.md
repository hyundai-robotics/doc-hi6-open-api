#### 4.2.2 `start / stop`

##### 描述

- `POST` : 执行机器人启动和机器人停止。

##### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

##### request-body

```json
{}
```

##### response-body

1. 状态码

- 200 : OK
- 400 : 错误请求
   - 请求体验证失败。
- 403 : 禁止
    - 在非远程模式下尝试了 ` (start)` 请求 (自 v60.30-07 起生效)。
- 404 : 未找到

2. 响应体

```json
{
    "_type": "JObject"
}
```
3. 错误码

- -38500: API 请求被拒绝，因为控制器不在远程模式

##### 示例

```python
POST /project/robot/start or /project/robot/stop

request-body:
{}
```

Python 脚本示例

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # 需要自动模式和电机开启设置
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
```