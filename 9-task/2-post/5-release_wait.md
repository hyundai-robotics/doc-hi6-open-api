#### 9.2.5 `release_wait`

##### 描述

- `POST` : release 语法
- 要求：TP > 系统 > 1: 用户环境 > `wait(di/wi) release` > `启用 (Enable)` 点击

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
- -1442069 : 用户环境配置错误。请确保满足所有先决条件

##### 示例

<blockquote>

```json
请求 URL:
POST /project/context/tasks[0]/release_wait

请求体
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