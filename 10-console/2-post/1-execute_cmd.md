#### 10.2.1 `execute_cmd`


##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : 执行 ${cont_model} 控制器的控制台命令。  
- 您可以执行 [CLI 机器人语言命令](../.././99-schema/robotlang.md)。  

##### path-parameter

```python
POST /console/execute_cmd
```

##### request-body

```json
{
    "cmd_line" : "rl.reinit"
}
```

##### status code

- 200: 请求成功  
	- 需要应用 [CLI 机器人语言命令](../.././99-schema/robotlang.md) 规则  
	- 如果命令违反机器人语言规则，则会返回 ecode 1，如下所示。
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400: 请求失败
	- 请求体验证失败
- 403/4: 请求失败
	- 请求的 API 未提供服务

##### Example

</blockquote>

Python 脚本示例
- 命令可以在 ` (motor on)` 和 `remote mode` 状态下执行。  
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
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: <Response [200]>
response: 200
```