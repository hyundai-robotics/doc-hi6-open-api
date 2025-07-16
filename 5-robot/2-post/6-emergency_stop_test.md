## 5.2.6 `emergency_stop_test`

- <b style="color:orange"> This API was used as the `emergency_stop` API up until version 60.28-00. </b>  

### Description

- Supported version : `60.30-00` &uparrow;
- `POST` : Executes an emergency stop.  

### path-parameter


<div style="max-width:fit-content">


```python
POST /project/robot/emergency_stop_test
```

</div>

### request-body

  <div style="max-width:fit-content">

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

</div>

### status code

- 200 : Request successful    
- 400 : Request failed     
	- Request body failed validation    
- 403 : Request failed    
	- Requested an API that is not serviced  


### Usage Example  

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