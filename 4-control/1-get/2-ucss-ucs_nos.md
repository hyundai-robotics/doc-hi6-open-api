#### 4.1.2 `ucss/ucs_nos`

##### 描述

- `GET` : 获取当前使用的用户坐标系统列表。
- 打印通过 `system > 2: Control parameter > 6: Coordinate registration` 注册的用户坐标系统列表。

##### 路径参数

```python
GET /project/control/ucss/ucs_nos
```

##### 示例

```python
请求 URL:
GET /project/control/ucss/ucs_nos

响应主体:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python 脚本示例

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