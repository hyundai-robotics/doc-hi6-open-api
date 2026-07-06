#### 8.2.5 `release_wait`

##### Description

- `POST` : release syntax
- Requirements: After entering `[2: system] - 1: User environment`, click `[Enable]` for `wait(di/wi) release`

##### path-parameter

```python
POST /project/context/tasks[0]/release_wait
```

##### request-body

```json
{}
```

##### status code

- 200 : Request succeeded
- 403 : Request failed
  -  Failure to meet the above requirements

##### error code
- -1442069 : User environment configuration error. Please ensure that all prerequisite requirements are satisfied

##### Example

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
