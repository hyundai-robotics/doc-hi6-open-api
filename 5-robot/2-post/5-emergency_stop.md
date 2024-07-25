## 5.2.5 `emergency_stop`

### Description

- Supported version : `60.28-00` &uparrow;
- `POST` : Executes an emergency stop.  

### path-parameter

```python
POST /project/robot/emergency_stop
```

### request-body
-  |key|type|contents|validation|
	|---|---|---|---|
	|`step_no`| int | Target step number for emergency stop, within the total step number of the current job | 1 ~ 999 |
	|`stop_at`| double | Set the percentage of the specified position to stop at | 1 ~ 100 |
	|`stop_at_corner`| int | 0: Normal stop, 1: Corner stop | 0 or 1 |
	|`category`| int | 0: Immediate stop, 1: Deceleration stop, 2: Pause | 0 or 1 or 2 |

- `0: Immediate stop`  
  &rightarrow; Same as when the controller turns off during robot playback. The motor turns off after stopping.  
- `1: Deceleration stop`  
	&rightarrow;  Acts as if the emergency stop button is pressed. The motor turns off after stopping.   
- `2: Pause`  
	&rightarrow;  Temporarily stops the robot motion. The motor does not turn off after stopping.  

### response-body

- 200 : Request successful    
- 400 : Request failed     
	- Request body failed validation    
- 403 : Request failed    
	- Requested an API that is not serviced  


### Usage Example  

```emergency_stop
POST /project/robot/emergency_stop

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


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "step_no": 2,
        "stop_at": 20,
        "stop_at_corner": 0,
        "category": 1,
    }

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {post_emergency_stop()}")
```
```sh
$python test.py
response: 200
```