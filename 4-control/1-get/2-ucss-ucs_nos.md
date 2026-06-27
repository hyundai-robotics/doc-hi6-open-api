#### 4.1.2 `ucss/ucs_nos`

##### Description

- `GET` : 获取当前使用的用户坐标系列表。
- 打印通过 `[F2: 系统] - 2: 控制参数 - 6: 坐标系注册 ([F2: system] - 2: Control parameter - 6: Coordinate registration)` 注册的用户坐标系列表。

##### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

##### Example

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python Script Example

```python
# test.py
import requests

def get_ucs_nos():
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ucss/ucs_nos'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(f"{get_ucs_nos()}")
```
```sh
$python test.py
[1, 2, 3]
```