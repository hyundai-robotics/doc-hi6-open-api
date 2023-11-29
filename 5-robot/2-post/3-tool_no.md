## 5.2.3 `tool_no`

### 설명

- POST : 현재 툴 번호를 설정합니다.

### path-parameter

```python
POST /project/robot/tool_no
```

### request-body

- `val` : 툴 번호
  - `로봇 툴` : `0` ~ `31`
  - `정치 툴` : `0` ~ `3`

### response-body

```json
{
    "_type": "JObject"
}
```

### 사용 예

```json
POST /project/robot/tool_no

request-body
{
  "val": 1
}
```

Python Script 예시

```python
import requests

def post_tool_no(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/tool_no'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    # 자동모드 및 모터 온 설정 필요
    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_tool_no(1)}")
```
```sh
$python test.py
response: 200
```