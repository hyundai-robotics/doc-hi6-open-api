#### 5.2.2 `start / stop`

##### Description

- `POST` : Performs robot start and robot stop.

##### path-parameter

```python
POST /project/robot/start
POST /project/robot/stop
```

##### request-body

```json
{}
```

##### response-body

1. status code

- 200 : OK
- 400 : Bad Request
   - The request body failed validation.
- 403 : Forbidden
    - A `start` request was attempted while not in Remote Mode (effective from v60.30-07).
- 404 : Not Found

2. response-body

```json
{
    "_type": "JObject"
}
```
3. error code

- -38500: API request rejected because the controller is not in Remote Mode

##### Example

```python
POST /project/robot/start or /project/robot/stop

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
