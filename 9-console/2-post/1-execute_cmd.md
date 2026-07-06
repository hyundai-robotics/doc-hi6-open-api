<div style="width: fit-content;">

#### 9.2.1 `execute_cmd`


##### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : Executes console commands for the ${cont_model} controller.  
- You can perform [CLI robot language commands](../.././99-schema/robotlang.md).  

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

- 200: Request successful  
	- Needs to apply [CLI robot language commands](../.././99-schema/robotlang.md) rules  
	- If a command violates the robot language rules, ecode 1 will be returned as shown below.
		<div style = "width: fit-content;">  
		
		```python
		{'_type': 'JObject', 'ecode': 1}
		```
		</div>
- 400: Request failed
	- Request body failed validation
- 403/4: Request failed
	- Requested an API that is not serviced

##### Example

</blockquote>

Python Script Example
- Commands can be executed in the `motor on` and `remote mode` state.  
- It can be executed when the move command matches the current robot axes.  

```python
# test.py
import time
import requests


class ExecuteCmds:
    request_to = {
        "com": [
            "rl.stop",  # External stop
            "rl.reinit",  # Restart
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 0, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, -10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [-10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 10, 0, 0, 0]",
            "rl.i move P,spd=500mm/sec,accu=4,tool=0  [10, 90, 0, 0, 0, 0]",
            "rl.i end",
            "rl.start",  # Play
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
</div>