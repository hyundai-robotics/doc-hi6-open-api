## 9.2.8 `execute_move`

### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : Moves to the specified pose.  

### path-parameter

```python
POST /project/context/tasks[{task index}]/execute_move
```

### request-body
- `stmt` : Key value in the request body, referring to the statement.  
- For details on how to write move statements, please refer to [HRBook](https://hrbook-hrc.web.app/#/view/doc-hrscript/korean/5-moving-robot/4-move).

```json
{
    "stmt" : "move SP,spd=1sec,accu=0,tool=1 [0 90 0 0 0 0]"
}
```

### response-body

- 200 : Request successful   
- 400 : Request failed    
	- Request body failed validation    
- 403 : Request failed    
	- Requested an API that is not serviced  

Python Script Example  
- Input pose command when the motor is on and matches the current robot axes.  

```python
# test.py
import requests
import time

def post_execute_move(in_pose: str) -> int:
    # base_url = "http://192.168.1.150:8888" # for Hi6COM 
    base_url = "http://127.0.0.1:8888" # for HRSpace - virtual robot controller
    path_parameter = "/project/context/tasks[0]/execute_move"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {"stmt": f"move SP,spd=1sec,accu=0,tool=1  {str(in_pose)}"}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code

poses = [
    "[-10, 90, -10, 0, 0, 0]",
    "[-5, 90, 5, 0, 0, 0]",
    "[0, 90, 0, 0, 0, 0]"
]

for idx, pose in enumerate(poses):
    print(f"Request {idx + 1}: Sending pose {pose}")
    status_code = post_execute_move(pose)
    print(f"Status code: {status_code}")
    if idx < len(poses) - 1:  
        time.sleep(1.5)

```
```sh
$python test.py 
Request 1: Sending pose [-10, 90, -10, 0, 0, 0]
Status code: 200
Request 2: Sending pose [-5, 90, 5, 0, 0, 0]
Status code: 200
Request 3: Sending pose [0, 90, 0, 0, 0, 0]
Status code: 200
```