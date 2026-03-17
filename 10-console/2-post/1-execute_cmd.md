#### 10.2.1 `execute_cmd`

##### 描述

- 支持的版本 : `60.28-00` &uparrow;
- `POST` : 为 ${cont_model} 控制器执行控制台命令。  
- 您可以执行 [CLI 机器人语言命令](../.././99-schema/robotlang.md)。  

##### 路径参数

```python
POST /console/execute_cmd
```

##### 请求主体

```json
{
    "cmd_line" : "rl.reinit"
}
```

##### 状态代码

- 200: 请求成功  
	- 需要应用 [CLI 机器人语言命令](../.././99-schema/robotlang.md) 规则  
	- 如果命令违反机器人语言规则，将返回 ecode 1，如下所示。
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400: 请求失败
	- 请求主体验证失败
- 403/4: 请求失败
	- 请求了未提供服务的 API

##### 示例

</blockquote>

Python 脚本示例
- 命令可以在 `电机 开 (motor on)` 和 `远程模式` 状态下执行。  
- 当移动命令与当前机器人轴匹配时，可以执行。  

```python
# test.py
import time
import requests


class ExecuteCmds:
    request_to = {
        "com": [
            "rl.stop",  # 外部停止
            "rl.reinit",  # 重启
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i end",
            "rl.start",  # 播放
        ],
    }


def post_execute_cmd() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/console/execute_cmd"
    head = {"Content-Type": "application/json; charset=utf-8"}

    execute_cmds = ExecuteCmds.request_to["com"]

    response: int = None
    for cmd in execute_cmds:
        data = {"cmd_line": cmd}
        response = requests.post(url=base_url + path_parameter, headers=head, json=data)
        print(f"response: {response}")
        time.sleep(0.1)

    return 200


print(f"response: {post_execute_cmd()}")
```
```sh
$python test.py 
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: <Response [200]>
响应: 200
```