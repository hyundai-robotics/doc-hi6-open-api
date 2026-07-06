#### 4.2.6 `emergency_stop_test`

- <b style="color:orange"> 此 API 在版本 60.28-00 之前作为 `emergency_stop` API 使用。 </b>  

##### Description

- Supported version : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  

##### path-parameter


<div style="max-width:fit-content">


```python
POST /project/robot/emergency_stop_test
```

</div>

##### request-body

  <div style="max-width:fit-content">

-  |key|type|contents|validation|
	|---|---|---|---|
	|`step_no`| int | 紧急停止的目标步骤编号，在当前作业的总步骤编号内 | 1 ~ 999 |
	|`stop_at`| double | 设置停止时的指定位置的百分比 | 1 ~ 100 |
	|`stop_at_corner`| int | 0: 正常停止, 1: 转角停止 | 0 或 1 |
	|`category`| int | 0: 立即停止, 1: 减速停止, 2: 暂停 | 0 或 1 或 2 |

- `0: 立即停止`  
  &rightarrow; 与机器人回放时控制器关闭时相同。电机在停止后关闭。  

    {% hint style="warning" %}
    规格更改

    - V60.29-08 ~ V60.30-10: 仅能在目标步骤调用立即停止 API。
    - V60.32-00 及以后: 可在任何步骤调用立即停止 API。

    {% endhint %}

- `1: 减速停止`  
	&rightarrow;  像是按下紧急停止按钮一样。电机在停止后关闭。   
- `2: 暂停`  
	&rightarrow;  暂时停止机器人运动。电机在停止后不会关闭。  

</div>

##### status code

- 200 : 请求成功    
- 400 : 请求失败     
	- 请求体验证失败    
- 403 : 请求失败    
	- 请求了未提供服务的 API  


##### Usage Example  

<div style="max-width:fit-content">

```emergency_stop_test
POST /project/robot/emergency_stop_test

request-body
{
  "step_no": 1,
  "stop_at": 50,
  "stop_at_corner": 0,
  "category": 1,
}
```

Python Script Example

```python
import requests


def emergency_stop_test() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop_test"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "step_no": 2,
        "stop_at": 20,
        "stop_at_corner": 0,
        "category": 1,
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {emergency_stop_test()}")
```
```sh
$python test.py
response: 200
```

</div>