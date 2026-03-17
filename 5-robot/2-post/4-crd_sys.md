#### 5.2.4 `crd_sys`

##### 描述

- `POST` : 设置当前的关节坐标系。

##### 路径参数

```python
POST /project/robot/crd_sys
```

##### 请求体

- [坐标系](../../99-schema/crdsys.md)

##### 响应体

```json
{
  "_type": "JObject",
  "cur_crd": 1,
  "ucrd_no": 1
}
```


##### 示例

```json
POST /project/robot/crd_sys

请求体
{
  "val": 1
}
```

Python 脚本示例

```python
import requests

def post_crd_sys(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/crd_sys'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_crd_sys(1)}")
```
```sh
$python test.py
响应：200
```