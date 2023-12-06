## 4.1.4 `ucss/ucs_nos`

### 설명

`ucss/ucs_nos` (user coordinate system numbers)

- `GET` : 현재 사용 중인 사용자 좌표계들을 리스트로 얻습니다.
- `시스템 > 2: 제어 파라미터 > 6: 좌표계 등록` 을 통해 등록한 사용자 좌표계 리스트를 출력합니다.

### path-parameter

```python
GET /project/control/ucss/ucs_nos
```

### 사용 예

```python
request url:
GET /project/control/ucss/ucs_nos

response-body:
{
    "_type" : "JObject",
    "val" : [1],
}
```

Python Script 예시

```python
# test.py
import requests

def get_ucs_nos():
    base_url       = 'http://192.168.1.150:8888'
    path_parameter = '/project/control/ucss/ucs_nos'
 
    response = requests.get(url = base_url + path_parameter)

    return response.json()

print(f"{get_ucs_nos()}")
```
```sh
$python test.py
[1, 2, 3]
```