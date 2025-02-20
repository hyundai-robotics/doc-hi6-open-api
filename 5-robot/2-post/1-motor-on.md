## 5.2.1 `motor_on`

### Description

- `POST` : Performs motor ON.
- The `motor off API` has been deprecated as of [v60.30-00](../../1-release-note/60-30.md).

### path-parameter

```python
POST /project/robot/motor_on
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
POST /project/robot/motor_on

request-body:
{}
```

Python Script Example

```python
import requests

def post_motor_on() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/motor_on'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"Motor-ON  response: {post_motor_on()}")
```
```sh
$python test.py
Motor-ON  response: 200
```