#### 11.1.2.1 `date_time`

##### 描述

- `PUT` : 更改系统时间。

##### request-body

- [日期时间](../../../99-schema/date_time.md)

##### 示例

<blockquote>

```python
请求 URL:
PUT /clock/date_time

请求体:
{
    "year": 2023,
    "mon": 10,
    "day": 30,
    "hour": 18,
    "min": 30,
    "sec": 0
}
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def put_system_time() -> int:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'
    head            = {'Content-Type': 'application/json; charset=utf-8'}
    body 			= {"year": 2023, "mon": 11, "day": 20, "hour": 21, "min": 2, "sec": 0}

    response = requests.put(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"响应: {put_system_time()}")
```
```sh
$python test.py
响应: 200
```
