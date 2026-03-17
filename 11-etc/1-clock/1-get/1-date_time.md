#### 11.1.1.1 `date_time`

##### 描述

- `GET` : 获取系统设置时间。

##### 响应主体

- [date time](../../../99-schema/date_time.md)

##### 示例

<blockquote>

```python
请求 URL:
GET /clock/date_time

响应主体:
{
    "_type": "JObject",
    "year": 2023,
    "mon": 11,
    "day": 20,
    "min": 40,
    "hour": 19,
    "sec": 54
}
```
</blockquote>

Python 脚本示例

```python
# test.py
import requests

def get_system_time() -> str:
    base_url        = 'http://192.168.1.150:8888'
    path_parameter  = '/clock/date_time'

    response = requests.get(url = base_url + path_parameter).json()

    t = f'[{response["mon"]}/{response["day"]}] {response["hour"]}:{response["min"]}'

    return t

print(get_system_time())
```
```sh
$python test.py
[11/20] 19:55
```
