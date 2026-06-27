#### 6.2.2 `ios/dio/{do_val}`

##### 描述

- `POST` : 更改数字输出。

##### path-parameter

```python
POST /project/control/ios/dio/do_val
```

##### request-body

```json
{
    "type": "do",
    "blk_no": 1,
    "sig_no": 1,
    "val": 1
}
```


##### query-parameter

- `类型 (type)` : io值类型
  - do : 位
  - dob : 有符号字节
  - dow : 有符号字 (2byte)
  - dol : 有符号双字 (4yte)
  - dof : 浮点数
- `blk_no` : 块编号 (0~9)
- `sig_no` : 信号索引 (0~)
- `val` : 你想要更改的设置值


##### 示例

```python
request url:
POST /project/control/ios/dio/do_val

request-body:
{
    "type": "do",
    "blk_no": 2,
    "sig_no": 3,
    "val": -99
}
```

Python 脚本示例

- 请参阅 [here](https://developer.mozilla.org/zh-US/docs/Web/HTTP/Status/200) 以获取响应 HTTP 状态码。
```python
# test.py
import requests

def post_do_val() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ios/dio/do_val'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"type": "dob", "blk_no": 2, "sig_no": 3,"val": -99}

    response = requests.post(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {post_do_val()}")
```
```sh
$python test.py
response: 200
```