#### 5.2.1 `motor_on`

##### 描述

- `POST` : 执行电机开启。
- `motor_off` API 已被弃用，并从 [v60.30-00](../../1-release-note/60-30.md) 开始不再支持。

##### 路径参数

```python
POST /project/robot/motor_on
```

##### 请求体

```json
{}
```

##### 响应

1. 状态码

- 200 : OK
- 400 : 错误请求
  - 请求体未通过验证
- 403 : 禁止
  - 在非远程模式下尝试进行 API 请求（自 v60.30-09 起生效）。
- 404 : 未找到


2. 响应体

```json
{
    "_type": "JObject"
}
```

3. 错误代码

- -38500 : API 请求被拒绝，因为系统不在远程模式

##### 示例

```python
POST /project/robot/motor_on

request-body:
{}
```
Python 脚本示例

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"电机开启响应: {post_motor_on()}")
```
```sh
$python test.py
电机开启响应: 200
```