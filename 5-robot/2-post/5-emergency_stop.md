## 5.2.5 `emergency_stop`

- <b style="color:orange"> For versions prior to ***<u>60.30-00</u>***, refer to ***<u>[emergency_stop_test](./6-emergency_stop_test.md)</u>*** instead of emergency_stop. </b>  

### Description

- Supported Version : `60.30-00` &uparrow;
- `POST` : Executes an emergency stop.  
- The same deceleration profile as pressing the emergency stop button is applied.  
- Due to network latency or request processing time, the API may respond slower than a physical button.  


### path-parameter

```python
POST /project/robot/emergency_stop
```

### request-body
```python 
{}
```

### response-body

- 200 : Request successful  
- 400 : Request failed (Emergency stop sequence execution failed)    

### Example

```emergency_stop
POST /project/robot/emergency_stop

request-body
{}
```

Python Script Example

```python
import requests


def post_emergency_stop() -> int:
    base_url = "http://192.168.1.150:8888"
    path_parameter = "/project/robot/emergency_stop"
    head = {"Content-Type": "application/json; charset=utf-8"}
    body = {}

    response = requests.post(url=base_url + path_parameter, headers=head, json=body)

    return response.status_code


print(f"response: {post_emergency_stop()}")
```
```sh
$python test.py
response: 200
```