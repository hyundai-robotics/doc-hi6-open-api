## 9.2.6 `release_wait`

### Description

`release_wait`

- `POST` : release syntax
- Requirements: TP > system > 1: User environment > `wait(di/wi) release` > `Enable` click

### path-parameter

```python
POST /project/context/tasks[0]/release_wait
```

### request-body

```json
{}
```

### response-body

- `200` : request success
- `403` : Failure to meet the above requirements

### Example

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python Script Example

```python
import requests

def post_release_wait() -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/context/tasks[0]/release_wait'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)

    return response.status_code

print(f"response: {post_release_wait()}")
```
```sh
$python test.py
response: 200
```