#### 4.1.6 `emergency_stop`

##### 描述

- `GET` : 获取关于紧急停止按钮被按下的状态的信息。  
- 当通过 API 请求紧急停止时，控制器在收到 API 请求的瞬间返回值 1。   

##### path-parameter

```python
GET /project/robot/emergency_stop
```

##### response-body

- 0: 紧急按钮释放
- 1: 紧急按钮被按下 

##### 示例

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "val": 0,
}
```

Python 脚本示例

```python
# test.py
import requests

def get_emergency_stop() -> Optional[dict]:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}

    try:
        response = requests.get(url=base_url + path_parameter, headers=head)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error in get_emg_state: {e}")
        return None

print(f"{get_emergency_stop()}")
```
```sh
$python test.py
{'_type': 'JObject', 'val': 0}
```