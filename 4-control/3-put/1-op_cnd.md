#### 4.3.1 `op_cnd`

##### Description

- `PUT` : 更改机器人的状态设置值。
- 如果在 TP 中打开 `condition setting window(cond.set)` 并请求相应的方法，  
您必须关闭并重新打开窗口，以使值反映出来。

##### path-parameter

```python
PUT /project/control/op_cnd
```

##### request-body

- [Condition Setting parameter](../../99-schema/op_cnd.md)


##### Example

```python
request url:
PUT /project/control/op_cnd

request-body:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}
```

Python Script Example

```python
# test.py
import requests 

def put_op_cnd() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/op_cnd'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = { 
                          "playback_mode": 1,
                          "step_goback_max_spd": 130,
                          "ucrd_num": 2
                     }

    response = requests.put(url = base_url + path_parameter, headers = head,  json = body)
    return response.status_code

print(f"response: {put_op_cnd()}")
```
```sh
$python test.py
response: 200 
```