## 5.2.3 `tool_no`

### Description

- POST : Set the current tool number.

### path-parameter

```python
POST /project/robot/tool_no
```

### request-body

- `val` : Tool number
  - `robot tools` : `0` ~ `31`
  - `stationary tool` : `0` ~ `3`

### response-body

```json
{
    "_type": "JObject"
}
```

### Example

```json
POST /project/robot/tool_no

request-body
{
  "val": 1
}
```

Python Script Example

```python
import requests

def post_tool_no(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/tool_no'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_tool_no(1)}")
```
```sh
$python test.py
response: 200
```