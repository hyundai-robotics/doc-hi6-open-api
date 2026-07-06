#### 4.2.1 `motor_on`

##### Description

- `POST` : Performs motor ON.
- The `motor_off` API has been deprecated and is no longer supported starting from [v60.30-00](../../1-release-note/60-30.md).

##### path-parameter

```python
POST /project/robot/motor_on
```

##### request-body

```json
{}
```

##### response

1. status code

- 200 : OK
- 400 : Bad Request
  - The request body failed validation
- 403 : Forbidden
  - An API request was attempted while not in Remote Mode (effective from v60.30-09).
- 404 : Not Found


2. response-body

```json
{
    "_type": "JObject"
}
```

3. error code

- -38500 : API request rejected because the system is not in Remote Mode

##### Example

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
