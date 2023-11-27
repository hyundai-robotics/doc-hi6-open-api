## 4.2.4 crd_sys

### 설명

- POST : 현재 조그(jog) 좌표계를 설정합니다.

### path-parameter

```python
POST /project/robot/crd_sys
```

### request-body

- [좌표계](../../99-schema/crdsys.md)

### response-body

```json
{
  "_type": "JObject",
  "cur_crd": 1,
  "ucrd_no": 1
}
```


### 사용 예

```json
POST /project/robot/crd_sys

request-body
{
  "val": 1
}
```

Python Script 예시

```python
import requests

def post_crd_sys(x: int = 0) -> int:
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/robot/crd_sys'
    head           = {'Content-Type': 'application/json; charset=utf-8'}
    body           = {"val": x}

    response = requests.post(url = base_url + path_parameter, headers = head, json = body)
    return response.status_code

print(f"response: {post_crd_sys(1)}")
```
```sh
$python test.py
response: 200
```