#### 4.3.1 `op_cnd`

##### 描述

- `PUT` : 更改机器人的状态设置值。
- 如果您在 TP 中打开 `条件设置窗口(cond.set)` 并请求相应的方法，  
则必须关闭并重新打开窗口以使值生效。

##### 路径参数

```python
PUT /project/control/op_cnd
```

##### 请求体

- [条件设置参数](../../99-schema/op_cnd.md)


##### 示例

```python
请求网址:
PUT /project/control/op_cnd

请求体:
{
    "playback_mode": 1,
    "step_goback_max_spd": 130,
    "ucrd_num": 2
}
```

Python 脚本示例

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
```
$python test.py
响应：200 
```