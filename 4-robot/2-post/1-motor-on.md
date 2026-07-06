#### 4.2.1 `motor_on`

##### Description

- `POST` : 执行电机开启。
- `motor_off` API 已被弃用，并从 `v60.30-00` 开始不再支持。

##### path-parameter

```python
POST /project/robot/motor_on
```

##### request-body

```json
{}
```

##### response

1. status code

- 200 : OK
- 400 : 错误请求
  - 请求体未通过验证
- 403 : 禁止
  - 在非远程模式下尝试了 API 请求（自 v60.30-09 起生效）。
- 404 : 未找到


2. response-body

```json
{
    "_type": "JObject"
}
```

3. error code

- -38500 : 由于系统不在远程模式，API 请求被拒绝

##### Example

```python
POST /project/robot/motor_on

request-body:
{}
```

Python Script Example

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
```
```sh
$python test.py
Motor-ON  response: 200
```