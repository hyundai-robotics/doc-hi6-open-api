#### 9.2.5 `release_wait`

##### 描述

- `POST` : release 语法
- 要求：在输入 `[2: system] - 1: 用户环境 ([2: system] - 1: User environment)` 后，点击 `[Enable]` 以进行 `wait(di/wi) release`

##### 路径参数

```python
POST /project/context/tasks[0]/release_wait
```

##### 请求体

```json
{}
```

##### 状态码

- 200 : 请求成功
- 403 : 请求失败
  - 未满足上述要求

##### 错误代码
- -1442069 : 用户环境配置错误。请确保满足所有前提要求

##### 示例

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python 脚本示例

```python
import requests

def post_release_wait() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/release_wait'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_release_wait()}")
```
```sh
$python test.py
response: 200
```