#### 5.1.1 `motor_on_state`

##### 描述

`motor_on_state`

- `GET` : 获取电机开启状态。

##### 路径参数

```python
GET /project/robot/motor_on_state
```

##### 响应体

- val :
  - `0` : 开
  - `翻译 (1)` : 关
  - `翻译 (2)` : 忙 (过渡状态)

##### 示例
```python
请求 URL:
GET /project/robot/motor_on_state

响应体:
{
    "_type" : "JObject",
    "val" : 1
}
```

Python 脚本示例

```python
# test.py
import requests

def get_motor_on_state() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on_state'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(f"电机开启状态: {get_motor_on_state()['val']}")
```
```sh
$python test.py
电机开启状态: 1
```
