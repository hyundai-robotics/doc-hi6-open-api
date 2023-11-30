## 5.2.2 `start / stop`

### Description

- POST : Performs robot start and robot stop.

### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

### request-body

```json
{}
```

### response-body

```json
{
    "_type": "JObject"
}
```

### Example

```python
POST /project/robot/motor_off

request-body: 
{}
```

Python Script Example

```python
import requests

def post_start() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/start'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    # Requires automatic mode and motor on settings
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

def post_stop() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/stop'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Start response: {post_start()}")
print(f"Stop  response: {post_stop()}")
```
```sh
$python test.py
Start response: 200
Stop  response: 200
```