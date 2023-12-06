## 5.1.1 `motor_on_state`

### Description

`motor_on_state`

- `GET` : Obtain the motor on status.

### path-parameter

```python
GET /project/robot/motor_on_state
```

### response-body

- val :
  - `0` : on
  - `1` : busy (Transitioning state)
  - `2` : off

### Example
```python
request url:
GET /project/robot/motor_on_state

response-body:
{
    "_type" : "JObject",
    "val" : 1
}
```

Python Script Example

```python
# test.py
import requests

def get_motor_on_state() -> dict:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on_state'

    response = requests.get(url = base_url + path_parameter).json()

    return response

print(f"Motor On status: {get_motor_on_state()['val']}")
```
```sh
$python test.py
Motor On status: 1
```