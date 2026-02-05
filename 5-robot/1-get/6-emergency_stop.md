#### 5.1.6 `emergency_stop`

##### Description

- `GET` : Retrieves information about the state of the emergency stop button being pressed.  
-  When an emergency stop is requested via the API, the controller returns a value of 1 at the moment it receives the API request.   

##### path-parameter

```python
GET /project/robot/emergency_stop
```

##### response-body

- 0: emergency button released
- 1: emergency button pressed 

##### Example

```python
request url:
GET /project/robot/tools/t_1

response-body:
{
    "val": 0,
}
```

Python Script Example

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
