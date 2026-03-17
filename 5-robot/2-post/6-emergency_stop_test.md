#### 5.2.6 `emergency_stop_test`

- <b style="color:orange"> 此 API 在版本 60.28-00 之前用作 `emergency_stop` API。 </b>  

##### 描述

- 支持版本 : `60.30-00` &uparrow;
- `POST` : 执行紧急停止。  

##### 路径参数


<div style="max-width:fit-content">


```python
POST /project/robot/emergency_stop_test
```

</div>

##### 请求体

  <div style="max-width:fit-content">

-  |key|type|contents|validation|
	|---|---|---|---|
	|`step_no`| int | 紧急停止的目标步骤编号，当前作业的总步骤编号内 | 1 ~ 999 |
	|`stop_at`| double | 设置指定位置的停止百分比 | 1 ~ 100 |
	|`stop_at_corner`| int | 0: 正常停止, 1: 角落停止 | 0 或 1 |
	|`category`| int | 0: 立即停止, 1: 减速停止, 2: 暂停 | 0 或 1 或 2 |

- `0: 立即停止`  
  &rightarrow; 与控制器在机器人播放期间关闭时相同。电机在停止后关闭。  

    {% hint style="warning" %}

    规格变更

    * V60.29-08 ~ V60.30-10：立即停止 API 只能在目标步骤调用。  
    * V60.32-00 及以后版本：立即停止 API 可以在任意步骤调用。

    {% endhint %}

- `1: 减速停止`  
	&rightarrow; 表现得仿佛按下了紧急停止按钮。电机在停止后关闭。   
- `2: 暂停`  
	&rightarrow; 暂时停止机器人运动。电机在停止后不关闭。  


</div>

##### 状态码

- 200 : 请求成功    
- 400 : 请求失败     
	- 请求体未通过验证    
- 403 : 请求失败    
	- 请求了未提供服务的 API  
##### 使用示例  

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

Python 脚本示例

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
