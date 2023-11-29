## 9.2.6 `release_wait`

### 설명

`release_wait`

- `POST` : 구문 정지해제
- 필요 조건 : TP > 시스템 > 1: 사용자 환경 > `wait(di/wi) 강제 해제` > `유효` 선택

### path-parameter

```python
POST /project/context/tasks[0]/release_wait
```

### request-body

```json
{}
```

### response-body

- `200` : 정상 동작
- `403` : 상기 필요 조건 불충족

### 사용 예

<blockquote>

```json
request url:
POST /project/context/tasks[0]/release_wait

request-body
{}
```

</blockquote>

Python Script 예시

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